from django.shortcuts import render
from item.models import Category, Item

def index(request):
    Items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'index.html', {
       'categories': categories,
       'Items': Items,
    })
   

def contact(request):
    return render(request, 'contact.html')  
