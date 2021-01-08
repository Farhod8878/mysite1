from django.shortcuts import render

def index(request):
	return render(request, '../templates/index.html')

def after(request):
	return render(request, '../templates/a.html')