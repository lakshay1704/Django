from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('add',views.addtodo,name='add'),# this route should only be posted this means that when we submit the form then the post request should point to this path
	#or we can also say that when we submit the form or post it tot eh server than only this path should be called    
	#for this we will import a decorator in the views.py file
	path('complete/<todo_id>',views.completetodo,name='complete'),
	path('deletecompleted',views.deletecompleted,name='deletecompleted'),
	path('deleteall',views.deleteall,name='deleteall')
]