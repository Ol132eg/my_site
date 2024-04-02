from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from random import shuffle
# Create your views here.

data_posts = [
    {
        'title': 'Рыбалка',
        'description': 'Хорошо посидели',
        'date': '21 авг 2021',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Commodi distinctio doloremque et fuga iste neque, pariatur quod sit veritatis voluptates?'
    },
    {
        'title': 'Париж',
        'description': 'Незабываемое путешествие',
        'date': '5 сент 2020',
        'content': '''Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
                Commodi distinctio doloremque et fuga iste neque, pariatur quod sit veritatis voluptates?'''
    },
    {
        'title': 'Финал лиги чемпионов',
        'description': 'Реал опять выиграл ЛЧ',
        'date': '28 мая 2022',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Qui, rem.'
    },
    {
        'title': 'Охота на уток',
        'description': 'Ни одна утка не пострадала',
        'date': '7 дек 2019',
        'content': 'Lorem ipsum dolor sit amet.'
    },
    {
        'title': 'Фестиваль огурца',
        'description': 'Суздаль ждет тебя',
        'date': '12 июль 2021',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci consectetur id inventore odit recusandae!'
    },
    {
        'title': 'Нашествие',
        'description': 'Даешь рок, но в следующем году',
        'date': '29 июль 2021',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Est mollitia recusandae rem?'
    },
    {
        'title': 'Новый год',
        'description': 'Эх, еще один год пролетел',
        'date': '31 дек 2022',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. A architecto corporis fuga ipsam laboriosam, nesciunt non quae qui ut veniam.'
    },
]

def main(request):
    #response = render_to_string('blog/index.html')
    #return HttpResponse(response)
    shuffle(data_posts)
    context = {'dict_posts':data_posts[:3]}
    return render(request, 'blog/index.html', context = context)

def posts(request):
    response = render_to_string('blog/list_detail.html')
    return HttpResponse(response)

def name_rout_post(request,name_post):
    data = {'post_name': name_post}
    return render(request, 'blog/detail_by_name.html', context=data)

def number_rout_post(request,number_post:int):
    data = {"post_number": number_post}
    return render(request, 'blog/detail_by_number.html', context=data)

def name_actor(request):
    data_dict={
        'year_born':1964,'city_born':'Бейрут',
        'movie_name':'На гребне волны'
    }
    return render(request,'blog/actor.html',context=data_dict)

def get_guinness_world_records(request):
    context = {
        'power_man': 'Narve Laeret',
        'bar_name': 'Bob’s BBQ & Grill',
        'count_needle': 1790,
    }
    return render(request, 'blog/guinnesswoldrecords.html', context=context)