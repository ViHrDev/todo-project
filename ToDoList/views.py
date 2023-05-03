from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm

from .models import ToDo


# Create your views here.


def index(request):
    if request.user.is_authenticated:
        context = ToDo.objects.filter(author=request.user)

        return render(request, 'ToDoApp/index.html', {'context_list': context})
    return render(request, 'ToDoApp/index.html')


@require_http_methods(['POST'])
def add(request):
    title, desc = request.POST['title'], request.POST['desc']
    author = User.objects.get(id=request.user.id)
    todo = ToDo(title=title, desc=desc, author=author)
    todo.save()
    return redirect('index')


def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')


def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')


class RegisterView(FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
