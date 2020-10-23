from django.shortcuts import render


def index(request):
    return render(request, "myapp/index.html", context={})
