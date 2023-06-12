from tastypie.resources import ModelResource
from shop.models import Category, Courses


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        name = 'categories'
        allowed_methods = ['get']


class CoursesResource(ModelResource):
    class Meta:
        queryset = Courses.objects.all()
        name = 'courses'
        allowed_methods = ['get', 'post', 'delete']
