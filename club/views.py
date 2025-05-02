from django.shortcuts import render
from .models import Club,ClubPost,ClubMember
from .forms import ClubForm,ClubPostForm, Club
# Create your views here.

def clubView(request):
    obj = Club.objects.all()
    return render(request,'club.html', {'form':obj})
def clubMemberView(request,p_id):
    obj = ClubMember.objects.all(pk=p_id)
    return render(request, 'clubDetails.html', {'form2':obj})