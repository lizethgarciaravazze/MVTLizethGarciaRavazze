from django.http import HttpResponse
from .models import Familiares
from django.template import loader

# Create your views here.


def familiar(request):
    familiar = Familiares(nombre="Diana Gizella", edad=58, fecha="1963-10-03")
    familiar2 = Familiares(nombre="Juan Carlos", edad=61, fecha="1960-11-19")
    familiar3 = Familiares(nombre="Tatiana", edad=20, fecha="2002-02-25")
    familiar.save()
    familiar2.save()
    familiar3.save()
    plantilla = loader.get_template("template1.html")
    context = {"fam1": familiar, "fam2": familiar2, "fam3": familiar3}
    documento = plantilla.render(context)
    return HttpResponse(documento)
