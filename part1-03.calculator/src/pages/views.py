from unittest import result
from django.http import HttpResponse


# Create your views here.
def addPageView(request):
	second = request.GET.get('second')
	first = request.GET.get('first')
	rs = int(first) + int(second)
	return HttpResponse(rs)
	

def multiplyPageView(request):
	second = request.GET.get('second')
	first = request.GET.get('first')
	rs = int(first) * int(second)
	return HttpResponse(rs)
