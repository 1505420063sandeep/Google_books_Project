

from django.shortcuts import render
import requests

def search_books(query, api_key):
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        'q': query,
        'key': api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        books = response.json().get('items', [])
        return books
    else:
        return None

def book_search_view(request):
    books = None
    query = request.GET.get('q', '')
    if query:
        api_key = 'AIzaSyBzITHJMLzH_sneng3amxlAWehvFEAWPr4'  # Replace with your API key
        books = search_books(query, api_key)
    return render(request, 'ggapp/book_search_view.html', {'books': books, 'query': query})
