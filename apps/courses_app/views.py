from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
	context = {
		"courses": Course.objects.all()
	} 
	return render(request, 'courses_app/index.html', context)


def add(request):
	Course.objects.create(name = request.POST['user_name'], description = request.POST['user_description'])
	return redirect('/')


def remove(request, id):
	context = {
		"selected_course": Course.objects.filter(id = id)
	}

	if 'yes' in request.POST:
		Course.objects.filter(id = id).delete()
		return redirect('/')

	if 'no' in request.POST:
		return redirect('/')




	return render(request, 'courses_app/remove.html', context)




