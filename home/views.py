from django.shortcuts import render, HttpResponse

def index(request):
    myvariable = {'name':'Palash'}
    return render(request, 'index.html',myvariable)
    # return  HttpResponse("This is my new home page now")

def about(request):
    return  HttpResponse("This is my new about page now")
def contact(request):
    return render(request, 'contact.html')