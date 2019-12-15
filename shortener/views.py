from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
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
        
        Url.objects.create(original_url=org_url, shortened_url=short_url, user=request.user)
    else:
        org_url = ''
        short_url = ''

    return render(request, 'home.html', 
                {'original_url': org_url,
                 'shortened_url': short_url})
@login_required
def links(request):
    urls = Url.objects.order_by('id').filter(user=request.user)
    return render(request, 'links.html', {'urls': urls})


def goto(request, shortened_url):
    if 'Mobile' in request.META['HTTP_USER_AGENT']:
        mobile = True
    else:
        mobile = False
    url = Url.objects.get(shortened_url= shortened_url)
    ClickDate.objects.create(url_id=url.id, is_mobile=mobile)
    go = url.original_url
    return redirect(go)


def lastday():
    day = datetime.now().day - 1
    year = datetime.now().year
    month = datetime.now().month
    return datetime(year, month, day)

def lastweek():
    day = datetime.now().day - 7
    year = datetime.now().year
    month = datetime.now().month
    return datetime(year, month, day)

def lastmonth():
    day = datetime.now().day
    year = datetime.now().year
    month = datetime.now().month - 1 
    return datetime(year, month, day)

def filterbyday(request):
    url = ClickDate.objects.filter(date__gt=lastday())
    return render(request, 'byday.html', 
    {
        'url': url,
        'count': url.count()
        })

def filterbyweek(request):
    url = ClickDate.objects.filter(date__gt=lastweek())
    return render(request, 'byday.html',
    {
        'url': url,
        'count': url.count()
        })

def filterbymonth(request):
    url = ClickDate.objects.filter(date__gt=lastmonth())
    return render(request, 'byday.html',
    {
        'url': url,
        'count': url.count()
        })

@login_required
def linkdetail(request, shortened_url):
    url = Url.objects.get(shortened_url= shortened_url)
    click = ClickDate.objects.filter(url_id=url.id)
    mobile = click.filter(is_mobile=True)
    desktop = click.filter(is_mobile=False)
    day = click.filter(date__gt=lastday())
    week = click.filter(date__gt=lastweek())
    month = click.filter(date__gt=lastmonth())

    return render(request, 'linkdetail.html',
    {
        'url': url,
        'day': day.count(),
        'week': week.count(),
        'month': month.count(),
        'mobile': mobile.count(),
        'desktop': desktop.count(),
        'total': click.count()
    }
    )