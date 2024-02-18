from django.test import TestCase
from faker import Faker
from apps.category.models import Category
class Tester(TestCase):
	def SetUp(self):
		fake =Faker()
		for _ in range(50):
			name_category = fake.word()
			slug_categoty = fake.slug(name_category, allow_unicode=True)
			print(name_category)



			Category.objects.create(
				name = name_category,
				slug = slug_categoty
				)