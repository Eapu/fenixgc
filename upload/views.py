from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms

from .forms import UsuariosForm


def create(request):
    if request.method == 'POST':
        form = UsuariosForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, 'upload/thanks.html', {'form': form})

    else:
        form = UsuariosForm()

    return render(request, 'upload/fenixupload.html', {
        'form': form,
    })


def created(request):

    return redirect('green:fenixgram')
