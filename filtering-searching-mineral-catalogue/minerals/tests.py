from django.test import TestCase
from django.urls import reverse

# Create your tests here.

from .models import Mineral

class MineralModelTests(TestCase):
	def test_new_mineral_created(self):
		mineral = Mineral.objects.create(
				name =  "Abelsonite",
				image_filename =  "240px-Abelsonite_-_Green_River_Formation%2C_Uintah_County%2C_Utah%2C_USA.jpg",
				image_caption =  "Abelsonite from the Green River Formation, Uintah County, Utah, US",
				category = "Organic",
				formula = "C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni",
				strunz_classification = "10.CA.20",
				crystal_system =  "Triclinic",
				unit_cell= "a = 8.508 Å, b = 11.185 Åc=7.299 Å, α = 90.85°β = 114.1°, γ = 79.99°Z = 1",
				color = "Pink-purple, dark greyish purple, pale purplish red, reddish brown",
				crystal_symmetry =  "Space group: P1 or P1Point group: 1 or 1",
				cleavage =  "Probable on {111}",
				mohs_scale_hardness =  "2–3",
				luster =  "Adamantine, sub-metallic",
				streak =  "Pink",
				diaphaneity = "Semitransparent",
				optical_properties = "Biaxial",
				group =  "Organic Minerals"
			)
		self.assertIn(mineral, Mineral.objects.all())


class MineralViewTests(TestCase):
	def setUp(self):
		self.mineral = Mineral.objects.create(
			  name = "Abhurite",
			  image_filename = "240px-Abhurite_-_Shipwreck_Hydra%2C_South_coast_of_Norway.jpg",
			  image_caption = "Brownish tabular crystals of abhurite from Shipwreck \"Hydra\", South coast of Norway",
			  category =  "Halide",
			  formula = "Sn<sub>21</sub>O<sub>6</sub>(OH)<sub>14</sub>Cl<sub>16</sub>",
			  strunz_classification = "03.DA.30",
			  crystal_symmetry =  "Trigonal",
			  group = "Halides"

			)


	def test_minerals_view(self):
		resp = self.client.get(reverse('minerals:mineral_list'))
		self.assertEqual(resp.status_code,200)
		self.assertIn(self.mineral, resp.context['minerals'])
		self.assertTemplateUsed(resp, 'minerals/minerals.html')


	def test_minerals_detail_view(self):
		resp = self.client.get(reverse('minerals:mineral_detail',
										kwargs={'pk':self.mineral.id }))
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(self.mineral, resp.context['mineral'])
		self.assertTemplateUsed(resp, 'minerals/mineral_detail.html')


	def test_search_by_letter(self):
		letter = "A".lower()
		resp = self.client.get(reverse('minerals:search_by_letter',
										kwargs={'letter':letter}))
		self.assertEqual(resp.status_code,200)
		self.assertIn(self.mineral,resp.context['minerals'])
		self.assertTemplateUsed(resp,'minerals/minerals.html')


	def test_search_by_text(self):
		resp = self.client.post("/minerals/search/text/",{'search':'ab'})
		self.assertEqual(resp.status_code,200)
		self.assertIn(self.mineral,resp.context['minerals'])
		self.assertTemplateUsed(resp,'minerals/minerals.html')


	def test_search_by_group(self):
		group = "Halides"
		resp = self.client.get(reverse('minerals:search_by_group',
										kwargs={'group':group}))
		self.assertEqual(resp.status_code,200)
		self.assertIn(self.mineral,resp.context['minerals'])
		self.assertTemplateUsed(resp,'minerals/minerals.html')
