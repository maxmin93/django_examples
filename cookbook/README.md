# cookbook plain

[Official Tutorial](https://docs.graphene-python.org/projects/django/en/latest/tutorial-relay/)

[Github examples](https://github.com/graphql-python/graphene-django/tree/master/examples)

참고문서

- [Graphene 튜토리얼 따라하기](https://jonnung.dev/graphql/2019/08/05/python-graphql-graphene-tutorial/)


## How to run

0) 웹서버 기동

```
python manage.py runserver 0.0.0.0:8000
```

1) 내장 graphiql 띄우기

open browser [http://localhost:8000/graphql/]

<p align="center">
<img height="400" src="https://github.com/maxmin93/graphene_examples/blob/master/cookbook/doc/graphene_examples-cookbook-graphi.png">
</p>

2) Postman 으로 쿼리하기

POST [http://localhost:8000/graphql/api]

- parameter 사용
- alias 사용

<p align="center">
<img height="400" src="https://github.com/maxmin93/graphene_examples/blob/master/cookbook/doc/graphene_examples-cookbook-Postman.png">
</p>

## webapp urls

urls.py 
```
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 입력된 graphql 을 검증하기 위한 schema 를 무엇을 할 것인지 설정이 필요한데
    #   1) GraphQLView.as_view(schema=schema) 에서 하거나
    #   2) settings.py 에서 GRAPHENE.SCHEMA 에 등록하거나 (공식 튜토리얼)
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    
    # for Postman (CSRF 검사 안하도록 우회)
    path('graphql/api', csrf_exempt(GraphQLView.as_view())),
]
```
