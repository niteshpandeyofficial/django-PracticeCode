#created by own
from django.db.models.fields import return_None
from django.http import HttpResponse
from django.shortcuts import render
import re

def index(request):
#     # param={"name":"Jhone","language":"english"}
    return render(request,'index.html')

def analyze(request):

    requested_text=request.POST.get('text','default')
    is_remove_punc_flag=request.POST.get('removePunc','off')
    is_capitalized_flag=request.POST.get('capitalizestring','off')
    is_spaceremover_flag=request.POST.get('spaceremover','off')
    is_newline_remover_flag=request.POST.get('newlineremover','off')
    # analyzed=requested_text
    if is_remove_punc_flag=='on':
        analyzed = ''
        punctuation_string = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        for char in requested_text:
            if char not in punctuation_string:
                analyzed+=char
        params={'purpose':'Removed Punctuation','analyzed_text':analyzed}
        requested_text=analyzed

    if is_capitalized_flag=='on':
        analyzed = ''
        for char in requested_text:
            analyzed+=char.capitalize()
        params={'purpose':'Capitalized Value of String','analyzed_text':analyzed}
        requested_text=analyzed

    if is_spaceremover_flag=='on':
        analyzed = ''
        analyzed=' '.join(requested_text.split())
        # result = re.sub(r'\s+', ' ', requested_text) we can use regex,replace method also to replace the double space with single space
        params={'purpose':'Space Remover from given sentences','analyzed_text':analyzed}
        requested_text=analyzed
    if is_newline_remover_flag=='on':
        analyzed = ''
        for char in requested_text:
            if char!='\n' and char!='\r':
                analyzed+=char
        params = {'purpose': 'Remove the new line from given sentences', 'analyzed_text': analyzed}
        requested_text = analyzed

    if is_remove_punc_flag!='on' and is_capitalized_flag!='on' and is_spaceremover_flag!='on' and is_newline_remover_flag!='on':
        return HttpResponse("Please select atleast one operation and try again!!")
    return render(request,'analyze.html',params)

#
# def about(request):
#     param={"name":"Nitesh","language":"python"}
#     # return HttpResponse("hello this is about ")
#     return render(request,'index.html',param)

# def removepunc(request):
#     request_text=request.GET.get('text','default')
#     return HttpResponse("you are inside the removepunc function")
#     # return render(request,'index.html')
#
# def capitalizestring(request):
#     return HttpResponse("you are inside the capitalizestring function")
#
# def newlineremover(request):
#     return HttpResponse("you are inside the newlineremover function")
#
# def spaceremover(request):
#     return HttpResponse("you are inside the spaceremover function")
#
# def countchar(request):
#     return HttpResponse("you are inside the charcount function")
