from re import template
from django.shortcuts import redirect, render 
from .models import *
from django.views.generic import CreateView 
from .forms import *
from django.contrib.auth import authenticate,login

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
        return redirect('/')

class student_signup_view(CreateView):
    model = User
    form_class = student_signup
    template_name = 'sign_up.html'

    def get_context_data(self, **kwargs):
        kwargs ['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('/')

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
