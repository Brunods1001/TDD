from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render

from lists.forms import ItemForm
from lists.models import Item, List

def home_page(request):
    context = {
        'form': ItemForm(),
    }
    return render(request, 'home.html', context)


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            form.save(for_list=list_)
            return redirect(list_)
    context = {
        'list': list_,
        'form': form,
    }
    return render(request, 'lists/list.html', context)


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        form.save(for_list=list_)
        return redirect(list_)  # works because of get_absolute_url
    return render(request, 'home.html', {'form': form})
