from django.urls import path
from .import views


urlpatterns = [
    path('',views.book_search_view,name='book_search_view')
]
