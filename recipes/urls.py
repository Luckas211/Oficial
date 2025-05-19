from django.urls import path
from recipes.views import home, contato, sobre


# dominio/recipes/home
urlpatterns = [
    path('', home),            # Home
    path('sobre/', sobre),     # Sobre
    path('contato/', contato), # Contato
]
