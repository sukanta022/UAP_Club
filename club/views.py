from django.shortcuts import render, get_object_or_404
from .models import Club,ClubPost,ClubMember
from .forms import ClubForm,ClubPostForm, ClubMemberForm
# Create your views here.

def clubView(request):
    obj = Club.objects.all()
    return render(request,'club.html', {'form':obj})


def create_club(request):
     if request.method == 'POST':
         form = ClubForm(request.POST, request.FILES)
         if form.is_valid():
             form.save()
             return render(request, 'home.html') # Redirect to the product list page after successful creation
     else:
         form = ClubForm()
     return render(request, 'form.html', {
         'form': form,
         'data': "Create Club"
     })


def edit_club(request, club_id):
    product = Club.objects.get(pk=club_id)
    if request.method == 'POST':
        form = ClubForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')  # Redirect to the product list page after successful update
    else:
        form = ClubForm(instance=product)
    return render(request, 'form.html', {
        'form': form,
        'data' : "Edit Club Details"
    })


def clubDataView(request,club_id):
    club = get_object_or_404(Club, id=club_id)
    post = ClubPost.objects.filter(club=club)
    members = ClubMember.objects.filter(club=club)
    return render(request, 'clubDetails.html', {
        'form3': post,
        'form2': members
    })

def create_post(request):
    if request.method == 'POST':
        form = ClubPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')  # Redirect to the product list page after successful creation
    else:
        form = ClubPostForm()
    return render(request, 'form.html', {
        'form': form,
        'data': "Create post"
    })

def edit_post(request, post_id):
    product = ClubPost.objects.get(pk=post_id)
    if request.method == 'POST':
        form = ClubPostForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    else:
        form = ClubPostForm(instance=product)
    return render(request, 'form.html', {
        'form': form,
        'data': "Edit Post"
    })

def edit_member(request, member_id):
    product = ClubMember.objects.get(pk=member_id)
    if request.method == 'POST':
        form = ClubMemberForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return render(request, 'clubDetails.html')  # Redirect to the product list page after successful update
    else:
        form = ClubMemberForm(instance=product)
    return render(request, 'form.html', {
        'form': form,
        'data': "Edit Member Details"
    })

def post_delete(request, post_id):
    data = ClubPost.objects.get(pk=post_id)
    if request.method == "POST":
        data.delete()
        return clubView(request)
    return render(request,'delete.html', {'data':data})