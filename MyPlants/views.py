from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")  # Sostituisci con la tua home
        else:
            return render(request, "login.html", {"error": "Credenziali non valide"})
    return render(request, "login.html")



def signup_view(request):
    return render(request, 'signup.html')


def profile_view(request):
    return render(request, 'profile.html')

def add_plant_view(request):
    return render(request, 'add_plant.html')


