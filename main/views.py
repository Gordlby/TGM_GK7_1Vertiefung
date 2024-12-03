import math

from django.shortcuts import render, redirect, get_object_or_404

from .forms import FachForm
from .models import Fach


# Create your views here.

def index(req):
    faecher_data = []
    faecher = Fach.objects.all()

    for fach in faecher:
        total_votes = fach.zu_niedrig + fach.genau_richtig + fach.zu_hoch
        zu_niedrig_percentage = (math.floor(fach.zu_niedrig / total_votes * 10000)/100) if total_votes > 0 else 0
        genau_richtig_percentage = (math.floor(fach.genau_richtig / total_votes * 10000)/100) if total_votes > 0 else 0
        zu_hoch_percentage = (math.floor(fach.zu_hoch / total_votes * 10000)/100) if total_votes > 0 else 0

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

def detail(req, fach_id):
    fach = get_object_or_404(Fach, id=fach_id)

    if req.method == 'POST':
        aufwand = req.POST['aufwand']
        if aufwand is not None:
            aufwand = int(aufwand)
            if aufwand is 0:
                zn = fach.zu_niedrig
                fach.zu_niedrig = zn + 1
            elif aufwand is 1:
                zn = fach.genau_richtig
                fach.genau_richtig = zn + 1
            elif aufwand is 2:
                zn = fach.zu_hoch
                fach.zu_hoch = zn + 1
            fach.save()


            return redirect('Ergebinsse', fach_id=fach_id)

    content = {
        'nav_active': 'Detail',
        'nav_extra': 'Detail',
        'fach': fach,
    }
    return render(req, "detail.html", content)

def results(req, fach_id):
    fach = get_object_or_404(Fach, id=fach_id)

    total_votes = fach.zu_niedrig + fach.genau_richtig + fach.zu_hoch
    zu_niedrig_percentage = (math.floor(fach.zu_niedrig / total_votes * 10000)/100) if total_votes > 0 else 0
    genau_richtig_percentage = (math.floor(fach.genau_richtig / total_votes * 10000)/100) if total_votes > 0 else 0
    zu_hoch_percentage = (math.floor(fach.zu_hoch / total_votes * 10000)/100) if total_votes > 0 else 0
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