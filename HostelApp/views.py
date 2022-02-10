from re import template
from django.shortcuts import redirect, render 
from .models import *
from django.views.generic import CreateView 
from .forms import *

# Create your views here.
def index (request):
    return render(request,'index.html')
def signup(request):
    return render(request,'register.html' )

class matron_signup_view (CreateView):
    model = User
    form_class = matron_signup
    template_name = 'sign_up.html'

    def form_valid(self, form):
        user = form.save()

        return redirect('/')
