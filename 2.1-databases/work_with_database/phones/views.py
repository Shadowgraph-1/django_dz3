from django.shortcuts import render, get_object_or_404
from .models import Phone


def catalog(request):
    sort = request.GET.get('sort', 'name')

    # Определяем варианты сортировки
    sort_options = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price'
    }

    # Получаем значение сортировки или дефолтное 'name'
    order_by = sort_options.get(sort, 'name')
    phones = Phone.objects.all().order_by(order_by)

    context = {
        'phones': phones,
        'current_sort': sort
    }
    return render(request, 'catalog.html', context)


def phone_detail(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    context = {
        'phone': phone
    }
    return render(request, 'product.html', context)
