from django.contrib import admin
from .models import Club, ClubMember, ClubPost
# Register your models here.
admin.site.register(Club)
admin.site.register(ClubMember)
admin.site.register(ClubPost)