from django.shortcuts import redirect, render
from lists.models import Item

def home_page(request):
    """
    Home page view
    :param request:
    :return:
    """
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)

        return redirect('/lists/the-only-list-in-the-world/')

    context = {
    }
    return render(request, 'home.html', context)


def view_list(request):
    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'lists/list.html', context)