from django.shortcuts import render, redirect
from .models import Url, ClickDate
import random
import string

def random_url(length = random.randint(8,12),
            upper = random.choice([False, True]),
            digits = random.choice([False, True])):
    
    chars =   string.ascii_lowercase 

    if upper:
        chars += string.ascii_uppercase
   
    if digits:
        chars += string.digits
    
    rndstr = ""
    for i in range(length):
        rndstr += random.choice([*chars])
    
    return rndstr

def home(request):
    if request.method == 'POST':
        org_url = request.POST['original_url']
        if org_url.startswith('http://'):
            pass
        else:
            org_url = 'http://' + org_url
        short_url = random_url()
        Url.objects.create(original_url=org_url, shortened_url=short_url)
    else:
        org_url = ''
        short_url = ''

    return render(request, 'home.html', 
                {'original_url': org_url,
                 'shortened_url': short_url})

def detail(request):
    urls = Url.objects.order_by('id')
    return render(request, 'detail.html', {'urls': urls})


def goto(request, shortened_url):
    url = Url.objects.get(shortened_url= shortened_url)
    url.clicked += 1
    url.save()
    ClickDate.objects.create(url_id=url.id)
    go = url.original_url
    return redirect(go)

def filterbyday(request):
    return render(request, 'byday.html')

def filterbyweek(request):
    return render(request, 'byweek.html')

def filterbymonth(request):
    return render(request, 'bymonth.html')