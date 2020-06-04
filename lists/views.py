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

        return redirect('/')

    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'lists/home.html', context)
