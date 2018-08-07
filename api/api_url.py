from app01 import views
from django.urls import path
from api.views import course

from app01 import views as app01_view
urlpatterns = [
    path('index/',app01_view.index),
    path('courses/',course.CourseView.as_view()),
    path('degreeCourse/',course.DegreeCourseView.as_view()),
    path('degreeCourse2/',course.DegreeCourseView2.as_view()),
    path('courses2/',course.CourseView2.as_view()),
    path('degreeCourse3/',course.DegreeCourseView3.as_view()),
    path('courses3/',course.CourseView3.as_view()),
    path('courses4/',course.CourseView4.as_view()),
    path('courses5/',course.CourseView5.as_view()),
    path('courses6/',course.CourseView6.as_view()),
]

