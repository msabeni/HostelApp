from django.shortcuts import redirect, render , get_object_or_404
from django.views import View
from HostelApp.models  import *
from django.views.generic import CreateView 
from HostelApp.forms  import *
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib import auth


# Create your views here.
def index (request):
    return render(request,'index.html')
    
def signup(request):
    return render(request,'register.html' )

class matron_signup_view (CreateView):
    model = User
    form_class = matron_signup
    template_name = 'sign_up.html'

    def get_context_data(self, **kwargs):
        kwargs ['user_type'] = 'matron'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('/login')

class student_signup_view(CreateView):
    model = User
    form_class = student_signup
    template_name = 'sign_up.html'

    def get_context_data(self, **kwargs):
        kwargs ['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('/login')

def login_view(request):
  form = login_form(request.POST or None)
  if request.method == 'POST':
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username,password=password)
      if user is not None and user.is_matron:
        login(request, user)
        return redirect('/')
      elif user is not None and user.is_student:
        login(request, user)
        return redirect('/')
  return render (request, 'login.html',{'form':form})

@login_required
def logout(request):
    auth.logout(request)
    return redirect ('/')

@login_required
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request, "profile.html", {"profile": profile})

@login_required
def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id = user)
    edit_form = edit_profile(instance=profile)
    if request.method == "POST":
            edit_form = edit_profile(request.POST,request.FILES,instance=profile)
            if edit_form.is_valid():  
                
                profile = edit_form.save(commit=False)
                profile.save()
                return redirect('profile')           
    return render(request, 'edit_profile.html', {"edit_form":edit_form, 'profile':profile})

@login_required
def list_rooms(request):
    rooms = Room.objects.all()
    return render(request,"rooms.html", {"rooms":rooms})

@login_required(login_url = '/login')
def book_room(request, id):
    room = get_object_or_404(Room,id = id)
    request.user.profile.room = room
    request.user.profile.save()
    return redirect('/room')

@login_required
def leave_room(request, id):
    room = get_object_or_404(Room, id=id)
    request.user.profile.room = None
    request.user.profile.save()
    return redirect('/room')

@login_required
def waiting_list(request):
    waiting_list = Notification.objects.all()
    return render(request, "waiting_list.html", {"waiting_list":waiting_list})

@login_required
def notification(request,id):
    user = User.objects.get(id=id)
    notification = Notification.objects.all()
    form = notification_form(instance=user)
    if request.method == "POST":
            form = notification_form(request.POST)
            if form.is_valid():  
                notification = form.save(commit=False)
                notification.save()
                return redirect('/')      
    return render(request, 'notification_form.html', {"form":form,"notification":notification})

@login_required
def upload_announcement(request,id):
    user = User.objects.get(id=id)
    announcements = Announcement.objects.all()
    form = post_announcement(instance=user)
    if request.method == "POST":
        form = post_announcement(request.POST,request.FILES)
        if form.is_valid():
            announcements = form.save(commit = False)
            announcements.save()
            return redirect('/announcements')
    return render(request,'post_announcement.html',{'form':form,'announcements':announcements})

@login_required
def announcements(request):
    announcements = Announcement.objects.all()
    return render(request,'announcements.html',{"announcements":announcements})

