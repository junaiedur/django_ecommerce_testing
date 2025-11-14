from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'order.html')

def search(request):
    query = request.GET.get('q')
    return render(request, 'search_results.html', {'query': query})

def cart(request):
    return render(request, 'cart.html')

# 🔐 Login View
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        # ⚙️ You can integrate Django auth later here
        # For now, just a placeholder for UI testing
        if email == "test@example.com" and password == "1234":
            messages.success(request, "Login successful!")
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password")

    return render(request, 'registration/login.html')

def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
        else:
            # ⚙️ You can integrate user creation logic here later
            messages.success(request, "Signup successful! Please log in.")
            return redirect('login')

    return render(request, 'registration/signup.html')
