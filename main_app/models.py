from django.db import models
from django.urls import reverse


RARITIES = (
  ('r-1', 'More than 5,000 in existence'),
  ('r-2', 'Between 2,000 and 5,000 in existence'),
  ('r-3', 'Between 500 and 2,000 in existence'),
  ('r-4', 'Between 200 and 500 in existence'),
  ('r-5', 'Between 75 and 200 in existence'),
  ('r-6', 'Between 20 and 75 in existence'),
  ('r-7', 'Between 10 and 20 in existence'),
  ('r-8', 'Between 5 and 10 in existence'),
  ('r-9', 'Between 2 and 4 in existence'),
  ('r-10', 'Unique, only one known example')
)

METALS = (
  ('0', 'Silver'),
  ('1', 'Gold'),
  ('2', 'Copper'),
  ('3', 'Brass'),
  ('4', 'Zinc'),
  ('5', 'Nickel')
)

# Create your models here.
class Case(models.Model):
  type = models.CharField(max_length=100)

  def __str__(self):
    return self.type

  def get_absolute_url(self):
    return reverse('case_detail', kwargs={'pk': self.id})

class Coin(models.Model):
  name = models.CharField(max_length=150)
  rarity = models.CharField(
    max_length=150
    #max_length=4,
    #choices=RARITIES,
    #default=RARITIES[0][0]
  )
  value = models.IntegerField()
  cases = models.ManyToManyField(Case)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    print(self)
    return reverse('coin_details', kwargs={'coin_id': self.id})

  
class Material(models.Model):
  material = models.CharField(
    max_length=1,
    choices=METALS,
    default=METALS[0][0]
    )
  coin = models.ForeignKey(Coin, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_material_display()}"





