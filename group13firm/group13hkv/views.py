
from django.shortcuts import render, redirect
from .models import Investment
from django.utils.timezone import now

def hkvhome(request):
    if request.method == 'POST':
        
        member_name = request.POST.get('member_name')
        member_cpm = request.POST.get('member_cpm')
        investment_amount = request.POST.get('investment')

       
        if member_name and member_cpm and investment_amount:
            Investment.objects.create(
                member_name=member_name,
                member_cpm=member_cpm,
                investment=investment_amount,
                investment_date=now()
            )
            return redirect('hkvhome') 

    return render(request, 'hkv/HKVhome.html', {})
from django.shortcuts import render

def funding_view(request):
    return render(request, '/hkv/funding.html')

