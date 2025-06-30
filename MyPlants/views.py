from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login as auth_login, get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages


def login_view(request):
    if request.method == "POST":
        if "otp" in request.POST:
            # Secondo step: verifica OTP
            otp_input = request.POST.get("otp")
            otp_session = request.session.get("otp_code")
            user_id = request.session.get("pre_2fa_user_id")
            if otp_input == otp_session and user_id:
                User = get_user_model()
                user = User.objects.get(id=user_id)
                auth_login(request, user)
                # Pulisci la sessione
                request.session.pop("otp_code", None)
                request.session.pop("pre_2fa_user_id", None)
                return redirect("profile")
            else:
                messages.error(request, "Codice OTP non valido")
                return render(request, "otp.html")
        else:
            # Primo step: verifica email e password
            email = request.POST.get("email")
            password = request.POST.get("password")
            User = get_user_model()
            try:
                user_obj = User.objects.get(email=email)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None
            if user is not None:
                # Genera OTP (qui statico, in produzione genera random e invia)
                otp_code = "123456"
                request.session["otp_code"] = otp_code
                request.session["pre_2fa_user_id"] = user.id
                # Qui dovresti inviare otp_code via email o altro canale
                return render(request, "otp.html")
            else:
                messages.error(request, "Credenziali non valide")
    return render(request, "login.html")

def profile_view(request):
    return render(request, 'profile.html')

def signup_view(request):
    return render(request, 'signup.html')


def profile_view(request):
    return render(request, 'profile.html')

def add_plant_view(request):
    return render(request, 'add_plant.html')


