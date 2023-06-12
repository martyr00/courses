from tastypie.resources import ModelResource
from shop.models import Category, Courses
from .authentication import CustomAuthentication
from tastypie.authorization import Authorization


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']


class CourseResource(ModelResource):
    class Meta:
        queryset = Courses.objects.all()
        resource_name = 'courses'
        allowed_methods = ['get', 'post', 'delete']
        authorization = Authorization()
        authentication = CustomAuthentication()
