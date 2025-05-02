from .models import Club,ClubMember,ClubPost
from django import forms

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['convener', 'name', 'logo', 'moto', 'cover_picture','description']

class ClubMemberForm(forms.ModelForm):
    class Meta:
        model = ClubMember
        fields = ['club', 'user', 'position', 'email', 'profile_picture']

class ClubPostForm(forms.ModelForm):
    class Meta:
        model = ClubPost
        fields = ['club', 'posted_by', 'title', 'description','post_type', 'start_date','end_date', 'location','cover_photo', 'pic1', 'pic2','pic3', 'pic4','pic5']