from django.shortcuts import HttpResponse, render

def home_page(request):
    context = {
        'new_item_text': request.POST.get('item_text', ''),
    }
    return render(request, 'lists/home.html', context)
