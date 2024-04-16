from django.shortcuts import render, get_list_or_404
from recipes.models import Recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by("-id")
    return render(
        request,
        "recipes/pages/home.html",
        context={"recipes": recipes, "title": "Home"},
    )


def category(request, category_id):
    # recipes = Recipe.objects.filter(category__id=category_id,is_published=True)

    # if not recipes:
    #     raise Http404("Not found")
    recipes = get_list_or_404(
        Recipe.objects.filter(category__id=category_id, is_published=True).order_by(
            "-id"
        )
    )

    return render(
        request,
        "recipes/pages/home.html",
        context={
            "recipes": recipes,
            "title": f"{recipes[0].category.name} - Category",
        },
    )


def recipe(request, recipe_id):
    print(f"Received recipe_id: {recipe_id}")
    # Verifica se recipe_id está definido corretamente
    if recipe_id:
        recipe = Recipe.objects.filter(id=recipe_id, is_published=True).first()
        print(f"Recipe query result: {recipe}")
    else:
        print("recipe_id is empty or None")

    return render(
        request,
        "recipes/pages/recipe-view.html",
        context={"recipe": recipe, "is_detail_page": True, "title": recipe.title},
    )
