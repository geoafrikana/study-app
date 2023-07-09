from django.contrib import admin
from  embed_video.admin  import  AdminVideoMixin
from .models import CustomUser, Course, CourseContent, Assessment, Question, Option


class  CourseContentAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass

admin.site.register(CustomUser)
admin.site.register(Course)
admin.site.register(CourseContent, CourseContentAdmin)
admin.site.register(Assessment)
admin.site.register(Question)
admin.site.register(Option)

