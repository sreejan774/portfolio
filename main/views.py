from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.conf import settings

# Create your views here.
def index(request):
	context = {
		"name" : settings.DATA["NAME"],
		"title" : settings.DATA["TITLE"],
		"about_me" : settings.DATA["ABOUT_ME"],
		"experience" : settings.DATA["EXPERIENCE"],
		"projects" : settings.DATA["PROJECTS"]  
	}
	return render(request,'main/index.html',context=context)

