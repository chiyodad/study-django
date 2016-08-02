# Django ORM


### Query Set
#### SQL  확인하기
```
query_set = Item.objects.all()
print(query_set.query)
>> Select * from item
```
#### Model Name 으로 object 가져오기

`django.apps.apps.get_model()` 사용

```
from django.apps import apps
model_obj = apps.get_model(app_name, model_name);
query_sets = model_obj.objects.all()
print(query_sets.query)
```
