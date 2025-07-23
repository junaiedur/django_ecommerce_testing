from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def search(request):
    query = request.GET.get('q')
    return render(request, 'search_results.html', {'query': query})

def cart(request):
    return render(request, 'cart.html')