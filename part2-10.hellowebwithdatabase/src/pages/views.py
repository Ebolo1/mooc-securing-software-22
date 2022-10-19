from django.http import HttpResponse
from .models import Message


# Create your views here.

def homePageView(request):
	content = 'Hello Web!';
	id = request.GET.get('id')

	if id:
		id = int(id)
		content = Message.objects.get(pk=id).content
		
	return HttpResponse(content)