## A web application that catalogs minerals, allows you to search the mineral catalogs by groups, letters and text searches 

## Example  code

```python

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


	def search_by_group(request,group):
		minerals = Mineral.objects.filter(group__icontains=group)
		return render(request, 'minerals/minerals.html',{'minerals': minerals})


	def random_mineral(request):
		random_index = random.randint(1, Mineral.objects.count())
		mineral = Mineral.objects.all()[random_index]
		return render(request, 'minerals/mineral_detail.html', {'mineral': mineral})

```

### This application was one of the projects from my TeamTreehouse python web development degree


## Installation

###### create a virtualenv that uses python3 and then the command pip install -r requirements.txt 

## Contributors

Just myself




