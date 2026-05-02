from django.contrib import admin
from .models import Category, Tag,Todo,SubTask,Comment,Attachment,Grade
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Todo)
admin.site.register(SubTask)
admin.site.register(Comment)
admin.site.register(Attachment)
admin.site.register(Grade)