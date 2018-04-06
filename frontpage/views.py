from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1> This is the frontpage app homepage </h1>")
