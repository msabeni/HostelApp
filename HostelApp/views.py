from django.shortcuts import redirect, render , get_object_or_404
from HostelApp.models  import *
from django.views.generic import CreateView 
from HostelApp.forms  import *
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .permissions import *
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
def logout(request):
    auth.logout(request)
    return redirect ('/')

@login_required
def list_rooms(request):
    rooms = Room.objects.all()
    return render(request,"rooms.html", {"rooms":rooms})

@login_required
def book_room(request, id):
    room = Room.objects.get(id = id)
    current_user = request.user
    current_user.profile.room = room
    current_user.profile.save()
    return redirect('/room')
# permission_classes= (IsReadOnly,)


@login_required
def leave_room(request, id):
    room = get_object_or_404(Room, id=id)
    request.user.profile.room = None
    request.user.profile.save()
    return redirect('/room')



