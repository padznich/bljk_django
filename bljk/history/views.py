from django.shortcuts import render

from models import Summary, Detail, Description
from forms import PlayerFilterEmailForm


def summary(request):

    s = Summary.objects.all()
    form = PlayerFilterEmailForm()

    if request.method == "POST":
        print "=" * 100
        print request.POST.get('email')
        print "=" * 100





    context = {
        's': s,
        'form': form
    }

    return render(request, 'summary.html', context)
