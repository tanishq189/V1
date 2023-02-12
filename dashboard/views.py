from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render , get_object_or_404, redirect

from item.models import Item

@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {
        'items': items, 
    }) 

def logout_user(request):
    logout(request)
    return render (request, 'core/index.html')
