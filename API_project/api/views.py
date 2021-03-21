from django.shortcuts import render, HttpResponse


# This is when we use django as frontend, in this project we will be using React!
# def index(request):
#     return render(request, 'index.html')

# This is when we use django as frontend, in this project we will be using React!
def index(request):
    return HttpResponse("It is working.")