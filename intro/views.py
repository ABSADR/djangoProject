from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def hello(request):
    return HttpResponse('Hello World')


def name(request):
    return HttpResponse('Alexx')

@login_required()
def cars(request):
    list_cars = {
        'all_cars': [
            {
                'brand': 'VW',
                'model': 'Golf6',
                'year': 2020
            },
            {
                'brand': 'BMW',
                'model': 530,
                'year': 2021
            },
            {
                'brand': 'audi',
                'model': 'a6',
                'year': 2023
            },
            {
                'brand': 'BMW',
                'model': 530,
                'year': 2021
            },
            {
                'brand': 'audi',
                'model': 'a6',
                'year': 2023
            },
            {
                'brand': 'BMW',
                'model': 530,
                'year': 2021
            },
            {
                'brand': 'audi',
                'model': 'a6',
                'year': 2023
            },
            {
                'brand': 'BMW',
                'model': 530,
                'year': 2021
            },
            {
                'brand': 'audi',
                'model': 'a6',
                'year': 2023
            }
        ]
    }

    return render(request, 'intro/list_of_cars.html', list_cars)

@login_required()
def movies(request):
    movies_lib = {

        "all_movies": [

            {
                "name": "Saw3",
                "category": "horror",
                "year": 2012

            },
            {
                "name": "Out-Laws",
                "category": "comedy",
                "year": 2023

            },
            {
                "name": "Insidious3",
                "category": "horror",
                "year": 2023
            },
            {
                "name": "Out-Laws",
                "category": "comedy",
                "year": 2023

            },
            {
                "name": "Insidious3",
                "category": "horror",
                "year": 2023
            },
            {
                "name": "Out-Laws",
                "category": "comedy",
                "year": 2023

            },
            {
                "name": "Insidious3",
                "category": "horror",
                "year": 2023
            },
            {
                "name": "Out-Laws",
                "category": "comedy",
                "year": 2023

            },
            {
                "name": "Insidious3",
                "category": "horror",
                "year": 2023
            },
            {
                "name": "Out-Laws",
                "category": "comedy",
                "year": 2023

            },
            {
                "name": "Insidious3",
                "category": "horror",
                "year": 2023
            },
            {
                "name": "Out-Laws",
                "category": "comedy",
                "year": 2023

            },
            {
                "name": "Insidious3",
                "category": "horror",
                "year": 2023
            }
        ]
    }

    return render(request, 'intro/list_of_movies.html', movies_lib)
