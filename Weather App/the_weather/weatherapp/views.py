import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

#well you need to import all the models and forms so that it can be viewed in the templates of the html

def index(request):
	print('#################################################')
	print(request)
	#api_key = '1e598dc08b05cc1c246251e11eaa40cd'
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=1e598dc08b05cc1c246251e11eaa40cd'
	#here q = {} is a placeholder
	#city = 'london'

	if request.method == 'POST':
		#print(request.POST)
		form = CityForm(request.POST)
		form.save()
	#creating an object for the CityForm class inherited form the ModelForm class
	form = CityForm() #this will clear the form once the page has been refressed



	cities = City.objects.all() #this will return all the objects of the model 
	#the name of the objects will be the city name as in the app's models.py file we defined in __str__ function
	#and using the below statement we are formating the string url along with city know as string formatting
	
	#the above statement requests the url using the get method of the requests library and with .json() method 
	#the json response from the api gets converted to a dictionary
	#print(r)
	weather_data = [] #list of dictionaries of city_weather
	for city in cities:
		r = dict(requests.get(url.format(city)).json()) 
		#print(r)
		#print(city.name)
		city_weather={
			'city': city.name ,
			'temperature':r['main']['temp'],
			'description':r['weather'][0]['description'],
			'icon': r['weather'][0]['icon'],
		}
		weather_data.append(city_weather)
		#print(city_weather)
		#making a context dictionary so that it can be injected into the templates
	#print('###################################################################################')
	#print(weather_data)
	context = {'weather_data':weather_data,'form':form}
	#also need to pass the form object so that it can recieve input from the user and enter it to the database
	#DICTIONARY PASSED AN OBJECT
		
	return render(request,'weatherapp/weather.html',context,)
	
	#passing the context dictionary along with the template
	#here the dictionary will be treated as an object i think 'context_object_type(cbv jose portia)'
	#so to access the values of the context dictionary in the above like the name of the city to inject in the template
	#using template tagging we use <dictionary name here city_weather>.<name of the key here city>
