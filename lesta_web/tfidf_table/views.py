from django.shortcuts import render
from .utils import compute_tfidf
from django.views.generic.edit import FormView
from .forms import UploadFilesForm


class UploadFilesView(FormView):
    form_class = UploadFilesForm
    template_name = 'tfidf_table/index.html'

    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Анализ tfidf',
            'form': self.form_class,
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            files = request.FILES.getlist('file_field')
            results = compute_tfidf(files)
            context = {
                'title': 'Результаты анализа',
                'tfidf_table': results,
            }
            return render(request, 'tfidf_table/result.html', context=context)
        context = {
            'title': 'Анализ tfidf',
            'form': self.form_class,
        }
        return render(request, self.template_name, context=context)
