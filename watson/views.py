from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import mylib.logic.watson.language_translator_logic as ltlogic
import mylib.logic.watson.tone_analyzer_logic as talogic


@login_required
def top(request):

    context = {}
    template = "watson/watson_top.html"

    return render(request, template, context)


@login_required
def language_translator(request):

    input_text = ""
    result_text = ""

    if request.method == "POST":
        input_text = request.POST['input_text']
        input_before_language = request.POST['input_before_language']
        input_after_language = request.POST['input_after_language']
        result_text = ltlogic.translate(
            input_text, input_before_language, input_after_language)

    else:
        pass

    context = {
        "method_type": request.method,
        "input_text": input_text,
        "result_text": result_text,
    }

    template = "watson/language_translator.html"

    return render(request, template, context)


@login_required
def tone_analyzer(request):

    input_text = ""
    tone_list = []

    if request.method == "POST":
        input_text = request.POST['input_text']

        tone_list = talogic.tone_analyze(input_text)

    context = {
        "method_type": request.method,
        "input_text": input_text,
        "tone_list": tone_list,
    }

    template = "watson/tone_analyzer.html"

    return render(request, template, context)
