from django.db import models


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
# Create your models here.
class Coin(models.Model):
  name = models.CharField(max_length=1)
  rarity = models.CharField(
    max_length=4,
    choices=RARITIES,
    default=RARITIES[0][0]
  )
  value = models.IntegerField()

