import math
from types import MethodType

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import FachForm
from .models import Fach, Antwort
loginURL = "login"


# Create your views here.

#@login_required(login_url='login')
@permission_required("main.view_fach", login_url=loginURL)
def index(req):
    faecher_data = []
    faecher = Fach.objects.all()
    print(req.user.has_perm("main.view_fach"))

    for fach in faecher:
        antworten = Antwort.objects.filter(fach=fach)
        total_votes = antworten.count()
        zu_niedrig_percentage = (math.floor(antworten.filter(choice=0).count() / total_votes * 10000)/100) if total_votes > 0 else 0
        genau_richtig_percentage = (math.floor(antworten.filter(choice=1).count() / total_votes * 10000)/100) if total_votes > 0 else 0
        zu_hoch_percentage = (math.floor(antworten.filter(choice=2).count() / total_votes * 10000)/100) if total_votes > 0 else 0

        faecher_data.append({
            'fach': fach,
            'zu_niedrig': round(zu_niedrig_percentage, 2),
            'genau_richtig': round(genau_richtig_percentage, 2),
            'zu_hoch': round(zu_hoch_percentage, 2),
            'total_votes': total_votes
        })


    content = {
        'nav_active': 'Fächer',
        'faecher': faecher,
        'faecher_data': faecher_data,
    }
    return render(req, "faecher.html", content)

@permission_required(["main.view_fach", "main.view_antwort", "main.add_antwort"], raise_exception=True)
def detail(req, fach_id):
    fach = get_object_or_404(Fach, id=fach_id)

    if req.method == 'POST':
        aufwand = req.POST['aufwand']
        if aufwand is not None:
            aufwand = int(aufwand)
            if 0 <= aufwand <= 2:
                Antwort(fach=fach, choice=aufwand).save()


            return redirect('Ergebinsse', fach_id=fach_id)

    content = {
        'nav_active': 'Detail',
        'nav_extra': 'Detail',
        'fach': fach,
    }
    return render(req, "detail.html", content)

@permission_required(["main.view_fach", "main.view_antwort"], raise_exception=True)
def results(req, fach_id):
    fach = get_object_or_404(Fach, id=fach_id)
    antworten = Antwort.objects.filter(fach=fach)

    total_votes = antworten.count()
    zu_niedrig_percentage = (math.floor(antworten.filter(choice=0).count() / total_votes * 10000)/100) if total_votes > 0 else 0
    genau_richtig_percentage = (math.floor(antworten.filter(choice=1).count() / total_votes * 10000)/100) if total_votes > 0 else 0
    zu_hoch_percentage = (math.floor(antworten.filter(choice=2).count() / total_votes * 10000)/100) if total_votes > 0 else 0
    content = {
        'nav_active': 'Ergebinsse',
        'nav_extra': 'Ergebnis',
        'fach': fach,
            'zu_niedrig': round(zu_niedrig_percentage, 2),
            'genau_richtig': round(genau_richtig_percentage, 2),
            'zu_hoch': round(zu_hoch_percentage, 2),
            'total_votes': total_votes
    }
    return render(req, "results.html", content)

@permission_required(["main.view_fach", "main.add_fach"], raise_exception=True)
def fachadd(req):
    if req.method == 'POST':
        form = FachForm(req.POST)
        print("POST")
        if form.is_valid():
            form.save()
            print("isvalid")
            return redirect('Fächer')
    else:
        form = FachForm()
    content = {
        'nav_active': 'Fach hinzufügen',
        'nav_extra': 'Erstellen',
        'form': form
    }
    return render(req, "fachadd.html", content)

def vlogin(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req, username=username, password=password)
        if user:
            login(req, user)
            next_url = req.GET.get("next") or "index"
            return redirect(next_url)
    else:
        return render(req, "login.html",{'login': True})

@login_required(login_url='login')
def vlogout(req):
    logout(req)
    return redirect("/")