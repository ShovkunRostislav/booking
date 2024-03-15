from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import BookingForm
from django.shortcuts import render, redirect

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

def book_flight(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            user = User.objects.get(pk=request.user.pk)
            new_booking = form.save(commit=False)
            new_booking.user = user
            new_booking.save()
            return redirect('main')
    else:
        form = BookingForm()

    return render(request, 'book_flight.html', {'form': form})