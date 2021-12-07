from django.contrib import admin
from projects.models import *
# Register your models here.

admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Comment)

admin.site.register(Donation)
admin.site.register(Rate)
admin.site.register(CommentReport)
admin.site.register(ProjectReport)
admin.site.register(ProjectPicture)
