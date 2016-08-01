# Django ORM

### Query Set
#### SQL  확인하기
```
query_set = Item.objects.all()
print(query_set.query)
>> Select * from item
```
