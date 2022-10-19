from django.shortcuts import render

# Create your views here.

def addPageView(request):
	content = request.POST.get("content")
	items = request.session.get('items', [])
	if len(items) < 10:
			items.append(content)
	elif len(items) == 10:
		items.remove(items[0])
		items.append(content)
	
	request.session["items"] = items

	return render(request, 'pages/index.html', {'items' : items})


def erasePageView(request):
	items = request.session.get('items', [])
	items.clear()
	request.session["item"] = items

	return render(request, 'pages/index.html', {'items' : items})


def homePageView(request):
	# use sessions (the data is stored in a database db.sqlite that is then accessed using a cookie)
	try:
		if items:
			items = request.session["items"]
	except NameError:
		items = []
		request.session["items"] = items

	# shorter way of writing instead of loader
	return render(request, 'pages/index.html', {'items' : items})
