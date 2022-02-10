from django.shortcuts import render,redirect
from .models import *
from django.views.generic import CreateView

def index(request):
  return render(request,'index.html')


# # Create your views here.
# class MatronSignUpView(CreateView):
#     model = User
#     form_class = MatronSignUpForm
#     template_name = 'signup.html'

#     def get_context_data(self, **kwargs):
#         kwargs ['user_type'] = 'matron'
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         user = form.save()
#         return redirect('/login_view')

# class StudentSignUpView(CreateView):
#     model = User
#     form_class = StudentSignUpForm
#     template_name = 'signup.html'

#     def get_context_data(self, **kwargs):
#         kwargs ['user_type'] = 'institution'
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         user = form.save()
#         return redirect('/login_view')

# def login_view(request):
#   form = LoginForm(request.POST or None)
#   if request.method == 'POST':
#     if form.is_valid():
#       username = form.cleaned_data.get('username')
#       password = form.cleaned_data.get('password')
#       user = authenticate(username=username,password=password)
#       if user is not None and user.is_employer:
#         login(request, user)
#         return redirect('employer')
#       elif user is not None and user.is_institution:
#         login(request, user)
#         return redirect('institution')
#   return render (request, 'login.html',{'form':form})

# def logout(request):
#   auth.logout(request)
#   return redirect ('/')

