"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('club', views.clubView, name="club"),
    path('details/<int:club_id>',views.clubDataView,name="details"),
    path("Club_create", views.create_club, name = "Club_create"),
    path("Post_create", views.create_post, name = "post_create"),
    path("Club_edit/<int:club_id>", views.edit_club, name= "Club_edit"),
    path("Post_edit/<int:post_id>", views.edit_post, name="Post_edit"),
    path("Member_edit/<int:member_id>", views.edit_member, name="Member_edit"),
    path("Delete_post/<int:post_id>", views.post_delete, name="Delete_post"),
    path("Member_add", views.add_member, name="AddMember")
]
