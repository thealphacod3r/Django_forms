from django.shortcuts import render
from . import forms

def index(request):
    return render(request, 'index.html')

def form_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print('Name: ' + form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('Comment: ' + form.cleaned_data['comment'])

    return render(request, 'forms.html', {'form':form})
