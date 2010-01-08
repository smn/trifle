from django.http import HttpResponse
# Create your views here.
def test(request):
    name = request.GET.get('name','')
    return HttpResponse("Hello %s" % name)