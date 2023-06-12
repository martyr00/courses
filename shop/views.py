from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Category, Courses


def index(request):
    courses = Courses.objects.all()
    return render(request, 'shop/courses.html', {'courses': courses})


def single_course(request, course_id):
    # # Option 1
    # try:
    #     course = Courses.objects.get(pk=course_id)
    #     return render(request, 'shop/single_course.html', {'course': course})
    # except Courses.DoesNotExist:
    #     raise Http404()

    # Option 2
    course = get_object_or_404(Courses, pk=course_id)
    return render(request, 'shop/single_course.html', {'course': course})



