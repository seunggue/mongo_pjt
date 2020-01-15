from django.shortcuts import render, redirect
from .models import Partner

# Create your views here.

def index(request):
    
    return render(request, 'page/index.html')

def partner(request):
    if request.method == 'POST':
        print('gggg')
        partner = Partner.objects.create(
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            duedate = request.POST.get('duedate'),
            password = request.POST.get('password'),
        
        )
        return redirect('page:partner')

    else:
        partners = Partner.objects.all()
        context = {
            'partners':partners,
        }
        
        return render(request, 'page/partner.html', context)
        
def detail(request):
    return render(request, 'page/detail.html')

def write(request):
    if request.method == 'POST':
        partner = Partner.objects.create(
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            duedate = request.POST.get('duedate'),
            password = request.POST.get('password'),
        
        )
        return redirect('page:partner')
    else:


        return render(request, 'page/write.html')
