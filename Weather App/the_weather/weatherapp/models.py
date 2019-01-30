from django.db import models

class City(models.Model):
	name = models.CharField(max_length=25)

	def __str__(self):
		return (self.name) #this is usually the name of the object in the model class

	class Meta:
		verbose_name_plural = 'cities'
