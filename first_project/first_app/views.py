from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.
def first_app_main(request):
    return render(request, 'first_app/index.html')
