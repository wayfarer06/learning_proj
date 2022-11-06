from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views import View


# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['nbar'] = 'home'
        return context

class MyView(View):
    def post(self, request):
        context = {}
        input = request.POST.get("input_text", None)
        punctuation = request.POST.get("punctuation", None)
        context['input'] = input
        context['nbar'] = 'output'
        print(input)
        return render(request, 'output.html', context)
