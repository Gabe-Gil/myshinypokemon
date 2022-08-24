from secrets import choice
from django.db import models
import requests
from django.contrib.auth.models import User
from django.urls import reverse

#Extra pokemon to add and remove
extra_forms = ['rattata-alola', 'raticate-alola', 'raichu-alola', 'sandshrew-alola', 'sandslash-alola',\
    'vulpix-alola', 'ninetails-alola', 'diglett-alola', 'dugtrio-alola', 'meowth-alola', 'marowak-alola',\
    'persian-alola', 'geodude-alola', 'graveler-alola', 'golem-alola', 'grimer-alola', 'muk-alola', 'exeggutor-alola',\
    'ponyta-galar', 'rapidash-galar', 'slowpoke-galar', 'slowbro-galar', 'farfetchd-galar', 'darmanitan-galar-standard',\
    'weezing-galar', 'mr-mime-galar', 'articuno-galar', 'zapdos-galar', 'moltres-galar', 'yamask-galar',\
    'slowking-galar', 'corsola-galar', 'zigzagoon-galar', 'linoone-galar', 'darumaka-galar', 'stunfisk-galar',\
    'rotom-heat', 'rotom-wash', 'rotom-fan', 'rotom-mow', 'rotom-frost', 'tornadus-therian', \
    'thundurus-therian', 'landorus-therian', 'kyurem-white', 'kyurem-black', 'calyrex-shadow',\
    'oricorio-pom-pom', 'oricorio-sensu', 'oricorio-baile', 'oricorio-pau', 'necrozma-ultra', 'calyrex-ice',\
    'lycanroc-midday', 'lycanroc-midnight', 'lycanroc-dusk', 'minior-red', 'necrozma-dusk', 'necrozma-dawn'\
    'giratine-altered', 'basculin-red-striped', 'darmanitan-standard', 'zygarde-50', 'mimikyu-disguised',
    'burmy-plant', 'burmy-sandy', 'burmy-trash', 'wormadam-plant', 'wormadam-sandy',\
    'wormadam-trash', 'shellos-west', 'shellos-east', 'gastrodon-west', 'pumpkaboo-average',\
    'gastrodon-east', 'shaymin-land', 'keldeo-ordinary', 'meloetta-aria', 'gourgeist-average',\
    'wishiwashi-school', 'toxtricity-amped', 'eiscue-ice', 'morpeko-full', 'urshifu-single-strike',\
    'urshifu-rapid-strike', 'basculin-blue-striped', 'basculin-white-striped']

remove_list = ['oricorio', 'lycanroc', 'minior', 'giratina', 'burmy', 'wormadam', 'shellos',\
    'gastrodon', 'shaymin', 'basculin', 'darmanitan', 'keldeo', 'meloetta', 'pumpkaboo', 'gourgeist',\
    'zygarde', 'wishiwashi', 'mimikyu', 'toxtricity', 'eiscue', 'morpeko', 'urshifu']

# Create your models here.
class Shiny(models.Model):
    method_choices = [
        ('Eggs Hatched', 'Eggs Hatched'),
        ('Soft Resets', 'Soft Resets'),
        ('Chain Encounters', 'Chains Encounters'),
        ('Wild Encounters', 'Wild Encounters'),
        ('Dynamax Adventures', 'Dynamax Adventures'),
        ('Other Method', 'Other Method')
    ]

    url = 'https://pokeapi.co/api/v2/pokemon-species/?limit=20000'
    temp = requests.get(url).json().get('results')
    pokemon_choices = [(i['name'], i['name']) for i in temp]

    for pokemon in remove_list:
        pokemon_choices.remove((pokemon, pokemon))

    for i in extra_forms:
        pokemon_choices.append((i, i))

    pokemon_choices = sorted(pokemon_choices)

    nickname = models.CharField(max_length=12)
    species = models.CharField(max_length=30, choices=pokemon_choices)
    attempts = models.PositiveIntegerField(default=0)
    method = models.CharField(max_length=30, choices=method_choices, default='Breeding')
    date_caught = models.DateField()
    author = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname

    def get_absolute_url(self):
        return reverse('shiny-detail', kwargs={'pk':self.pk})
