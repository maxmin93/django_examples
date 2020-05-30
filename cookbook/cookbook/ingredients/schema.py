import graphene
from graphene_django.types import DjangoObjectType

from cookbook.ingredients.models import Category, Ingredient

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient

# GraphQL 질의 함수 정의
class Query(object):
    # 낙타 표기법으로 variable 사용
    all_categories = graphene.List(CategoryType)        # allCategories
    all_ingredients = graphene.List(IngredientType)     # allIngredients

    # Field(id:<value>) 또는 Field(name:<value>) 질의 가능
    category = graphene.Field(CategoryType, id=graphene.Int(), name=graphene.String())
    ingredient = graphene.Field(IngredientType, id=graphene.Int(), name=graphene.String())

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_ingredients(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related('category').all()

    def resolve_category(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Category.objects.get(pk=id)
        if name is not None:
            return Category.objects.get(name=name)
        return None

    def resolve_ingredient(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Category.objects.get(pk=id)
        if name is not None:
            return Category.objects.get(name=name)
        return None