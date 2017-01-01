from django.db import models

# Create your models here.

class Mineral(models.Model):
	name = models.CharField(max_length = 250, default = '')
	image_filename =  models.CharField(max_length = 250,default = '')
	image_caption = models.CharField(max_length = 250,default = '')
	category = models.CharField(max_length = 250,default = '')
	formula = models.CharField(max_length = 250,default = '')
	strunz_classification = models.CharField(max_length = 250,default = '')
	crystal_system = models.CharField(max_length = 250,default = '')
	unit_cell = models.CharField(max_length = 250,default = '')
	color =  models.CharField(max_length = 250,default = '')
	crystal_symmetry =  models.CharField(max_length = 250,default = '')
	cleavage =  models.CharField(max_length = 250,default = '')
	mohs_scale_hardness = models.CharField(max_length = 250,default = '')
	luster =  models.CharField(max_length = 250,default = '')
	streak =  models.CharField(max_length = 250,default = '')
	diaphaneity = models.CharField(max_length = 250,default = '')
	optical_properties = models.CharField(max_length = 250,default = '')
	refractive_index = models.CharField(max_length = 250,default = '')
	crystal_habit = models.CharField(max_length = 250,default = '')
	specific_gravity = models.CharField(max_length = 250,default = '')
	group = models.CharField(max_length = 250,default = '')

	class Meta:
		ordering = ['name']


	def __str__(self):
		return self.name

