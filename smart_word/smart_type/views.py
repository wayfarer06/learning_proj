from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from help_functions import (
    rm_punctuation,
    make_uppercase,
    make_lowercase,
    rm_newline,
    rm_extra_spaces,
    spell_check,
    stop_words,
    wiki_summary
)


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
        input = input.replace('\n', '\n\n')
        punctuation = request.POST.get("punctuation", None)
        uppercase = request.POST.get("uppercase", None)
        lowercase = request.POST.get("lowercase", None)
        newline = request.POST.get("newline", None)
        extraspace = request.POST.get("extraspace", None)
        countchar = request.POST.get("countchar", None)
        spellcheck = request.POST.get("spellcheck", None)
        stopwords = request.POST.get("stopwords", None)
        summary = request.POST.get("summary", None)
        context['nbar'] = 'output'
        attribute_dict = {"punctuation": [punctuation, rm_punctuation], "uppercase": [uppercase, make_uppercase],
                          "lowercase": [lowercase, make_lowercase], "newline": [newline, rm_newline],
                          "extraspace": [extraspace, rm_extra_spaces],
                          "spellcheck": [spellcheck, spell_check], "stopwords": [stopwords, stop_words]}
        for key in attribute_dict:
            if attribute_dict[key][0] == 'on':
                input = attribute_dict[key][1](input)

        context['output'] = input

        if summary == 'on':
            context['summary'] = wiki_summary(input)
            context['summary_on'] = 'yes'


        return render(request, 'output.html', context)
