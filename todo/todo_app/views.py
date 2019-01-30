from django.shortcuts import render,redirect
from .models import todo
from .forms import todo_form
from django.views.decorators.http import require_POST

def index(request):
	todo_list = todo.objects.order_by('id')
	form = todo_form
	context = {'todo_list':todo_list,'form' : form}
	return render(request,'todo_app/index.html',context) #write the path after templates folder
	#by this above statement the todo_lict containig all the objects will  get pass to the template
@require_POST #this only accepts POST requests
def addtodo(request):
	'''print(request.POST['text']) #'text' is the form field name #this will print out the text that the form has to accept and the user has entered'''
	form=todo_form(request.POST) #takes all the post data and initiate the form with it
	if form.is_valid():
		new_todo = todo(text = request.POST['text'])
		new_todo.save() 
	return redirect('index')


def completetodo(request,todo_id):
	completedtodo = todo.objects.get(pk=todo_id)
	completedtodo.complete = True
	completedtodo.save()

	return redirect('index')


def deletecompleted(request):
	todo.objects.filter(complete__exact=True).delete()

	return redirect('index')


def deleteall(request):
	todo.objects.all().delete()

	return redirect('index')
