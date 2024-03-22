from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import BookingForm
from django.shortcuts import render, redirect

def Album(request):
    context = {
        "render_strin": 'Це альбом нашої Авіакомпанії'
    }
    return render(request, template_name='album.html', context=context)

def main(request):
    context = {
        "render_string": 'Rostics Aviation - выдающаяся авиакомпания, где безопасность и комфорт находятся в центре каждого полета. Современный авиапарк, тщательно обученный персонал и персональный подход к каждому клиенту делают наши перевозки непревзойденными.\nСпециализируясь в регулярных и чартерных рейсах, Rostics предоставляет гибкие воздушные услуги для корпоративных клиентов и частных лиц. Наша постоянная преданность инновациям и устойчивости подчеркивает наше стремление к экологически ответственной авиации.\nВыберите Rostics Aviation для уникального воздушного опыта, где качество и индивидуальный подход объединяются, чтобы сделать каждый момент в небесах незабываемым.'
    }
    return render(request, template_name='main.html', context=context)

def place_list(request):
    places = Place.objects.all()
    context = {
        "place": places
    }
    return render(request, template_name='place_lis.html', context=context)

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = BookingForm()
    
    return render(request, 'book_flight.html', {'form': form})

def alb1(request):
    return render(request, 'link1.html')

def alb2(request):
    return render(request, 'link2.html')

def alb3(request):
    return render(request, 'link3.html')