from django.http import HttpResponse


def index(request):
    return HttpResponse("Business wins or IT failures.")