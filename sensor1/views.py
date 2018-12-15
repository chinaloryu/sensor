

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('Test for git.</br>'+'Test for release.')