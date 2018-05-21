from django.views.generic import ListView
from django.shortcuts import render
from django.db.models import Count, Q
from .models import Data
from django.http import JsonResponse
import json
# Create your views here.

def Home(request):
    return render(request, 'graph.html')

def GraphA(request):
    sex_dataset = Data.objects.values('sex').exclude(sex='')\
    .annotate(total=Count('sex')).order_by('sex')
    
    categories = list()
    count_data = list()
    

    for data in sex_dataset:
        categories.append('%s Class' % data['sex'])
        count_data.append(data['total'])
    print(categories)
        
        
    female_data = {
        'name': 'female',
        'data': [count_data[0]],
        'color': 'blue'
    }

    male_data = {
        'name': 'male',
        'data': [count_data[1]],
        'color': 'red'
    }

    # categories = ['sex_dataset[0]['sex']', 'sex_dataset[1]['sex']]

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Distribution based on sex'},
        'xAxis': {'categories': ['Female Class', 'Male Class']},
        'series': (female_data, male_data)
    }

    return JsonResponse(chart)




def GraphB(request):
    relationship_dataset = Data.objects.values('relationship').exclude(relationship='')\
    .annotate(total=Count('relationship')).order_by('relationship')
    
    categories = list()
    count_data = list()
    

    for data in relationship_dataset:
        categories.append('%s Class' % data['relationship'])
        count_data.append(data['total'])
    print(categories)
    print(count_data)
        
        
    husband = {
        'name': 'husband',
        'data': [count_data[0]],
        'color': 'green'
    }

    not_in_family = {
        'name': 'not_in_family',
        'data': [count_data[1]],
        'color': 'yellow'
    }

    other_relative = {
        'name': 'other_relative',
        'data': [count_data[2]],
        'color': 'orange'
    }

    own_child = {
        'name': 'own_child',
        'data': [count_data[3]],
        'color': 'red'
    }

    unmarried = {
        'name': 'unmarried',
        'data': [count_data[4]],
        'color': 'black'
    }

    wife = {
        'name': 'wife',
        'data': [count_data[5]],
        'color': 'blue'
    }

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Distribution based on relationship'},
        'xAxis': {'categories': categories},
        'series': (wife, own_child, husband, not_in_family, other_relative, unmarried)
    }

    return JsonResponse(chart)


class LoadData(ListView):
    model = Data
    context_object_name = 'all_data'
    template_name='data_list.html'