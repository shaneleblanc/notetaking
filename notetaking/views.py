from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django import forms
from .models import Note
from .users.models import User
from django.contrib import auth


class NewNoteForm(forms.Form):
    title = forms.CharField(max_length=128)
    body = forms.CharField(widget=forms.Textarea)


class NewUserForm(forms.Form):
    username = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'],
            )
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            return redirect('/user/register')

    else:
        form = NewUserForm()
        context = {
            'form': form,
        }
        return render(request, 'registration/register.html', context)

def delete(request, note_id):
    note = Note.objects.filter(id=note_id)
    note.delete()
    return redirect('/')

def home(request):
    if request.method == "POST":
        form = NewNoteForm(request.POST)
        if form.is_valid():
            note = Note.objects.create(
                owner=request.user,
                title=form.cleaned_data['title'],
                body=form.cleaned_data['body']
            )
        return redirect('/')
    else:
        if request.user.is_authenticated:
            form = NewNoteForm()
            notes = Note.objects.all().filter(owner=request.user).order_by('-created')
            # Negative "created" for descending order

            context = {
                'hello': 'Welcome,',
                'notes': notes,
                'form': form
            }
        else:
            context = {
                'hello': 'Welcome! Please sign up or log in.',
                'notes': None,
                'form': None
            }
        return render(request, 'home.html', context)

