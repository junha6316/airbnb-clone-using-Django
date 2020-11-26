"""
Using List View
"""

from math import ceil
from datetime import datetime

from django.http import Http404
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, View
from django.http import HttpResponse
from django_countries import countries

from . import models
from . import forms


class HomeView(ListView):

    """ Home View  Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5

    page_kwarg = "page"
    ordering = "created"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RoomDetail(DetailView):
    model = models.Room

class SearchView(View):

    def get(self, request):
        country = request.GET.get("country")

        if country:
            form = forms.SearchForm(request.GET) # form will remember your request
            print(form)
            if form.is_valid(): # if form has no error, return True

                city = form.cleaned_data.get('city')
                country = form.cleaned_data.get('country')
                room_type = form.cleaned_data.get('room_type')
                price = form.cleaned_data.get('price')
                guests = form.cleaned_data.get('guests')
                bedrooms = form.cleaned_data.get('bedrooms')
                beds = form.cleaned_data.get('beds')
                baths = form.cleaned_data.get('baths')
                instant_book = form.cleaned_data.get('instant_book')
                superhost = form.cleaned_data.get('superhost')
                amenities = form.cleaned_data.get('amenities')
                facilities = form.cleaned_data.get('facilities')

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city

                filter_args["country"] = country

                if room_type is not None:
                    filter_args["room_type"] = room_type
                if price is not None:
                    filter_args["price__lte"] = price
                if guests is not None:
                    filter_args["guests__gte"] = guests

                if bedrooms is not None:
                    filter_args["bedrooms__gte"] = bedrooms

                if beds is not None:
                    filter_args["beds"] = beds

                if beds is not None:
                    filter_args["baths"] = baths

                if instant_book is True:
                    filter_args["instant_book"] = True

                if superhost is True:
                    filter_args["host__superhost"] = True

                if amenities is not None:
                    for amenity in amenities:
                        filter_args["amenities"] = amenity

                if facilities is not None:
                    for facility in facilities:
                        filter_args["facilities"] = facility

                qs = models.Room.objects.filter(**filter_args).order_by("-created")
                paginator = Paginator(qs, 10, orphans=10)

                page = request.GET.get( "page", 1) #current page
                rooms = paginator.get_page(page)

                return render(request,"rooms/search.html",context={"forms": form, 
                'rooms':rooms})
               
        else:
            
            form = forms.SearchForm() 
            return render(request, "rooms/search.html", context={"forms": form},)
               

       
