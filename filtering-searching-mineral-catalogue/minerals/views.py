from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Mineral
import random

# Create your views here.

def minerals(request):
	minerals = Mineral.objects.all()
	return render(request, 'minerals/minerals.html',{'minerals': minerals })


def mineral_detail(request, pk):
	mineral = get_object_or_404(Mineral, pk = pk)
	return render(request, 'minerals/mineral_detail.html', {'mineral': mineral})


def search_by_letter(request,letter):
	minerals = Mineral.objects.filter(name__startswith=letter)
	return render(request, 'minerals/minerals.html',{'minerals': minerals,'letter':letter })


def search_by_text(request):
	if request.method=='POST':
		text = request.POST['search']
		minerals = Mineral.objects.filter(
		 Q(name__icontains=text)|Q(category__icontains=text)|Q(formula__icontains=text)|
		 Q(strunz_classification__icontains=text)|Q(crystal_system__icontains=text)|
		 Q(unit_cell__icontains=text)|Q(color__icontains=text)|Q(crystal_symmetry=text)|
		 Q(cleavage__icontains=text)|Q(mohs_scale_hardness__icontains=text)|
		 Q(luster__icontains=text)|
		 Q(streak__icontains=text)|Q(diaphaneity__icontains=text)|
		 Q(optical_properties__icontains=text)|Q(refractive_index__icontains=text)|
		 Q(crystal_habit__icontains=text)|Q(specific_gravity__icontains=text)|
		 Q(group__icontains=text)


		)
	return render(request, 'minerals/minerals.html',{'minerals': minerals})


def search_by_group(request,group):
	minerals = Mineral.objects.filter(group__icontains=group)
	return render(request, 'minerals/minerals.html',{'minerals': minerals,
													'group':group})


def random_mineral(request):
	random_index = random.randint(1, Mineral.objects.count())
	mineral = Mineral.objects.all()[random_index]
	return render(request, 'minerals/mineral_detail.html', {'mineral': mineral})
