from django.shortcuts import render

from . import forms
from .utils import save_file


def index(request):
    context = {
        'title': 'Анализ tfidf',
        'form': forms.FileForm(),
    }
    return render(request, 'tfidf_table/index.html', context=context)


def result(request):
    context = {'title': 'Результат анализа'}
    if request.method == 'POST':
        form = forms.FileForm(request.POST, request.FILES)
        if form.is_valid():
            save_file(request.FILES['file'])
    return render(request, 'tfidf_table/result.html', context=context)
