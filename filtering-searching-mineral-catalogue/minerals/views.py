from django.shortcuts import render, get_object_or_404

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
		minerals = Mineral.objects.filter(name__icontains=text)
	return render(request, 'minerals/minerals.html',{'minerals': minerals})


def random_mineral(request):
	random_index = random.randint(1, Mineral.objects.count())
	mineral = Mineral.objects.all()[random_index]
	return render(request, 'minerals/mineral_detail.html', {'mineral': mineral})
