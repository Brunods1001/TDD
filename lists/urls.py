from django.urls import path
from lists.views import home_page, new_list, view_list


app_name = 'lists'
urlpatterns = [
    path('<list_id>/', view_list, name='view_list'),
    path('new', new_list, name='new_list'),
]
