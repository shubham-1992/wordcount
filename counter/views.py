from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    # return HttpResponse("HEllo There !")
    return render(request,'home.html',{"Hithere":"Hello Guys", "Contact":"whatz up !"})

# def about(request):
#     return HttpResponse("<h1>HEy That's me !</h1>")

def about(request):
    return render(request,'about.html',{"Me":"Shubham"})

def count(request):
    fulltext = request.GET['fulltext']
    # print(fulltext)

    wordtext=fulltext.split()

    worddictionary={}
    for each in wordtext:
        if each not in worddictionary.keys():
            worddictionary[each]=1
        else:
            worddictionary[each]+=1

    sorted_ = sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{"fulltext_":fulltext,"wordtext_":len(wordtext),"worddictionary":worddictionary.items(),"sorted_":sorted_})