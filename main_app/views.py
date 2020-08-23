from django.shortcuts import render

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Resource
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def resources_index(request):
    resources = Resource.objects.all()
    return render(request, 'resources/index.html', {'resources': resources})


class ResourceCreate(LoginRequiredMixin, CreateView):
    model = Resource
    fields = ['resource_name', 'org_name', 'category', 'hours',
              'notes', 'street', 'city', 'state', 'phone', 'long', 'lat', 'url']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
