from django.shortcuts import render

# Create your views here.

def post_principalPage():
    return render(request, 'principalPage.html',{})
