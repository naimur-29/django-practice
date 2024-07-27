from django.http import HttpResponse

def home(request):
	return HttpResponse("Hello World! I'm Back.")

def about(request):
	return HttpResponse("About Page!")
