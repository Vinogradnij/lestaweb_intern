from django.shortcuts import render


def index(request):
    context = {'title': 'Анализ tfidf'}
    return render(request, 'tfidf_table/index.html', context=context)


def result(request):
    context = {'title': 'Результат анализа'}
    return render(request, 'tfidf_table/result.html', context=context)
