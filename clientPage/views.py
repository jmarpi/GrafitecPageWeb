from django.shortcuts import render

# Create your views here.

def post_principalPage(request):
    return render(request, 'principal/principalPage.html',{})
