from django.shortcuts import render, HttpResponse


print("Hello Rahul")
# Create your views here.
def welcome_func(request):
    # print(request.build_absolute_url())
    # print(request.GET)

    # book_name = request.GET("book_title")
    # return HttpResponse("<h1>Welcome to our application</h1>")
    # return render(request,"home.html")
    return render(request,"home2.html")

# import requests
# def call_get_studs(request):


    