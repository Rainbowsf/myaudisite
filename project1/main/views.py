from django.shortcuts import render


def products(request):
    return render(request, 'main/products.html')


def news(request):
    return render(request, 'main/news.html')


def index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def etron(request):
    return render(request, 'main/e-tron.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def sitemap(request):
    return render(request, 'main/map.html')
