from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="recipes-home"),
    path(
        "recipes/categories/<int:category_id>/", views.category, name="recipes-category"
    ),
    path("recipes/<int:recipe_id>/", views.recipe, name="recipes-recipe"),
]
