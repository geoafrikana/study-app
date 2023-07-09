from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new/<str:portal_role>/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('new-course/', views.new_course, name='new-course'),
    path('view-course-content/<str:pk>/', views.view_course_content, name='view-course-content'),
    path('add-course-content/<str:pk>/', views.add_course_content, name='add-course-content'),
    path('view-all-courses/', views.CourseListView.as_view(), name='view_all_courses'),
    path('enroll/<str:pk>', views.enroll_student, name='enroll_student'),
    path('my-courses/', views.MyCourses.as_view(), name='my_courses'),
]