from django import template
import pokebase as pb
from django.core.cache import cache

register = template.Library()

@register.filter
def rep(value):
    return pb.pokemon(value).id

@register.filter
def cache_image_url(value):
    url = cache.get(value)

    if not url:
        pokemon_id = pb.pokemon(value).id
        url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/{pokemon_id}.png"

        cache.set(value, url, timeout=None)
    
    return url

@register.filter
def plurality(value, arg):
    pass
    #if attempts == 1: make method singular