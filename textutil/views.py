# Royal
from django.http import HttpResponse
from django.shortcuts import render


def home(request) :
    return render(request,'index.html')

def analyze(request):
    djtext = (request.POST.get('text','default'))
    removepunc = (request.POST.get('removepunc','off'))
    fullcaps = (request.POST.get('fullcaps','off'))
    newlineremover = (request.POST.get('newlineremoverbutton','off'))
    Space_remover = (request.POST.get('Spaceremover','off'))
    char_count = (request.POST.get('char_count','off'))

    print(fullcaps)
    print(djtext)
    print(removepunc)
    print(newlineremover)
    params ={}
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
           if char not in punctuations:
               analyzed += char
        params ={'purpose': ' Removed Punctuations ',
        'analyzed_text': analyzed }
        djtext = analyzed
        #return render(request,'analyze.html',params)
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params ={'purpose': ' Changed To UpperCase ',
             'analyzed_text': analyzed }
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            analyzed += char
        params ={'purpose': ' Removed newline',
             'analyzed_text': analyzed }
        djtext = analyzed

        #return render(request,'analyze.html',params)
    if(Space_remover == "on"):
        analyzed = ""
        for char in djtext:
            if(char != " "):
                 analyzed += char
        params ={'purpose': ' Spaces Removed',
             'analyzed_text': analyzed }
        djtext = analyzed

        #return render(request,'analyze.html',params)
    if(char_count == "on"):
        params ={'purpose': ' Total number of character',
             'analyzed_text': len(djtext) }
        djtext = analyzed

        #return render(request,'analyze.html',params)

    if(params == {} ):
        return HttpResponse("Error")
    
    return render(request,'analyze.html',params)
    
     