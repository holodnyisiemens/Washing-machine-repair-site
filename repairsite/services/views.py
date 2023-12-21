from django.shortcuts import render

menu = [
    {'url_title': 'Главная', 'url_name': 'home'},
    {'url_title': 'О сайте', 'url_name': 'about'},
    {'url_title': 'Каталог', 'url_name': 'catalog'},
]

def home(request):
    data = {
        'title': 'Главная',
        'menu': menu,
    }
    return render(request, 'services/home.html', context=data)

def about(request):
    data = {
        'title': 'О сайте',
        'menu': menu,
    }
    return render(request, 'services/about.html', context=data)

def catalog(request):
    data = {
        'title': 'Каталог услуг',
        'menu': menu,
    }
    return render(request, 'services/catalog.html', context=data)
