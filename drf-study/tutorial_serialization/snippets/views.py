from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

class JSONResponse(HttpResponse):
    """
    콘텐츠를 JSON으로 변환한 후 HttpResponse 형태로 반환합니다.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


    @csrf_exempt # 인증되지 않은 사용자도 이 뷰에 POST 가능
    def snippet_list(request):
        """
        코드 조각을 모두 보여주거나 새 코드 조각을 만듭니다.
        """
        if request.method == 'GET':
            snippets = Snippet.objects.all()
            serializer = SnippetSerializer(snippets, many=True)
            return JSONResponse(serializer.data)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = SnippetSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
            return JSONResponse(serializer.errors, status=400)

    @csrf_exempt
    def snippet_detail(request, pk):
        """
        코드 조각 조회, 업데이트, 삭제
        """
        try:
            snippet = Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = SnippetSerializer(snippet)
            return JSONResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = SnippetSerializer(snippet, data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data)
            return JSONResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            snippet.delete()
            return HttpResponse(status=204)
