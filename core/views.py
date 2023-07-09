from django.shortcuts import render, redirect
from .models import CustomUser
from .utils import email_username_authenticator
from django.contrib.auth import login as auth_login, logout as auth_logout
from .models import Course, CourseContent
from django.contrib import messages
from django.views.generic import ListView
from django.http import HttpResponseRedirect

def home(request):
    if request.user.is_authenticated:
        print('authenticated')
    return render(request, 'core/home.html')

def logout(request):
    auth_logout(request)
    return redirect('home')


def signup(request, portal_role):
    if request.method == 'POST':
        portal_role_dict = {
            'instructor': 'ins',
            'student': 'stu'
        }

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        CustomUser.objects.create_user(username, email, password, portal_role=portal_role_dict.get(portal_role))
    return render(request, 'core/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = email_username_authenticator(username, password)
        if user is not None:
            auth_login(request, user)
        return redirect('home')
        
    return render(request, 'core/login.html')

def new_course(request):
    if request.method == 'POST':
        user = request.user
        if user.portal_role == 'ins':
            course_name = request.POST['course-name']
            course = Course(name = course_name, instructor = request.user)
            course.save()
            messages.success(request, 'New Course Created')

    return render(request, 'core/new-course.html')

def add_course_content(request, pk):
    course = request.user.courses.get(pk=pk)
    if request.method == 'POST':
        content_title = request.POST['content-title']
        content_url = request.POST['content-url']
        new_course_content = CourseContent(title=content_title, course=course, content_video=content_url)
        new_course_content.save()
        messages.success(request, f'{content_title.capitalize()} added successfully')
        return redirect('view-course-content', pk=pk)
    return render(request, 'core/add-course-content.html', {'course': course})


def view_course_content(request, pk):
    if request.user.portal_role == 'ins':
        course = request.user.courses.get(pk=pk)
        is_instructor = course.instructor == request.user
        is_student =  False
    elif request.user.portal_role == 'stu':
        course = Course.objects.get(pk=pk)
        is_instructor = False
        is_student = True
    
    contents = course.contents.all()
    
    context= {'course':course,
              'contents':contents,
              'is_instructor': is_instructor,
              'is_student': is_student}
    return render(request, 'core/view-course-content.html', context = context)

class CourseListView(ListView):
    model = Course

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        student = self.request.user
        courses = Course.objects.all()
        for course in courses:
            if course.students.filter(pk=student.pk).exists():
                course.is_enrolled = True
        context['courses'] = courses
        return context

class MyCourses(ListView):
    model= Course
    context_object_name = 'my_courses'
    template_name = 'core/my_courses.html'

    def get_queryset(self, *args, **kwargs):
        # qs = super(MyCourses, self).get_queryset(*args, **kwargs)
        student_courses = self.request.user.student_courses.all()
        return student_courses

def enroll_student(request, pk):
    course = Course.objects.get(pk=pk)
    course.students.add(request.user)
    course.save()
    return redirect('view_all_courses')