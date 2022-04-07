from django.shortcuts import render
from Sparql_queries.queries import get_data
import numpy as np
import pandas as pd
from django.http import HttpResponse
from io import StringIO
# Create your views here.


def index(request):
    return render(request , 'main/index.html')

def athlete(request):
    return render(request , "main/athlete.html")

def medal_athlete(request):
        sparqlQueries = get_data()
        athlete , medals = sparqlQueries.top10_medals()
        print(medals)
        data = {
            "name":zip(athlete,medals),
            'flag':True,
            'suffix':'medal',
            'title':'TOP 10 ATHLETE'
            
           
        }
    
        return render(request,'main/athlete.html',context = data)

def height_athlete(request):
        sparqlQueries = get_data()
        athlete , height = sparqlQueries.top_10_height()
        data = {
            "name":zip(athlete,height),
            'flag':True ,
            'suffix':'cm',
            'title':'TOP 10 TALLEST ATHLETE'
           
        }
    
        return render(request,'main/athlete.html',context = data)

def weight_athlete(request):
        sparqlQueries = get_data()
        athlete , weight = sparqlQueries.top_10_weight()
        data = {
            "name":zip(athlete,weight),
            'flag':True ,
            'suffix':'Kg',
            'title':'TOP 10 HEAVIEST ATHLETE'
           
        }
    
        return render(request,'main/athlete.html',context = data)

def age_athlete_old(request):
        sparqlQueries = get_data()
        athlete , age = sparqlQueries.top10_ages_old()
        data = {
            "name":zip(athlete,age),
            'flag':True,
            'suffix':'years',
            'title':'TOP 10 OLDEST ATHLETE'
           
        }
    
        return render(request,'main/athlete.html',context = data)

def age_athlete_young(request):
        sparqlQueries = get_data()
        athlete , age = sparqlQueries.top10_ages_young()
        data = {
            "name":zip(athlete,age),
            'flag':True,
            'suffix':'years',
            'title':'TOP 10 YOUNGEST ATHLETE'
           
        }
    
        return render(request,'main/athlete.html',context = data)
def athlete_search(request):
        context = {'flag2':True}
        if request.method == "POST" :
           sparqlQueries = get_data()
           name = request.POST.get("new")
           athlete , medals = sparqlQueries.search_match(name.title())
           data = {
            "name":zip(athlete,medals),
            "flag2":True
           
            }
           return render(request,'main/athlete.html',context = data)
        return render(request,'main/athlete.html',context=context)

def athlete_stat_search(request):
        context = {'flag2':True}
        if request.method == "POST" :
           sparqlQueries = get_data()
           name = request.POST.get("new")
           athlete , medals = sparqlQueries.search_match(name.title())
           data = {
            "name":zip(athlete,medals),
            "flag3":True
           
            }
           return render(request,'main/athlete.html',context = data)
        return render(request,'main/athlete.html',context=context)


def ath_profile(request,name):
    sparqlQueries = get_data()
    medals_count  = sparqlQueries.ath_age_medals(name)
    sports_name , at_ages = sparqlQueries.athlete_Info(name.title())
    _ , total_medals = sparqlQueries.search_match(name.title())
    avg_age , avg_height , avg_weight = sparqlQueries.athlete_stat(name)
    
    
    
    
    context ={
        'sportsname': " ".join(x for x in np.unique(sports_name)),
        'at_age' : np.unique(at_ages),
        'total_medal':medals_count,
        'all_age':" ".join(str(x) for x in np.unique(np.array(at_ages)).astype('float')),
        'average_height': float(avg_height[0]) , 
        'average_weight':float(avg_weight[0]),
        'average_age':float(avg_age[0]),
        'name':name,
       

    }
    
    return render(request,"main/athlete_profile.html" , context=context)


def ath_stats(request,name):
    sparqlQueries = get_data()
    avg_age = sparqlQueries.avg_age(name.title())
    _ , avg_height , avg_weight = sparqlQueries.athlete_stat(name)
    all_avg_age , all_avg_height , all_avg_weight = sparqlQueries.other_athlete_stat(name)

    
    context ={
       
       
        'average_height': float(avg_height[0]) , 
        'average_weight':float(avg_weight[0]),
        'average_age':float(avg_age),
        'all_average_height': float(all_avg_height[0]) , 
        'all_average_weight':float(all_avg_weight[0]),
        'all_average_age':float(all_avg_age[0]),
        'name':name,
       

    }
    
    return render(request,"main/athlete_statics.html" , context=context)




def country(request):   #country page
    return render(request,"main/country.html")

def medal_country(request): #use case 1 countries by number of medal
        sparqlQueries = get_data()
        country , medals = sparqlQueries.top10_medals_country()
        
        data = {
            "name":zip(country,medals),
            'flag':True,
            'suffix':'medal',
            'title':'TOP 10 Countries With Highest Medal Count'
            
           
        }
    
        return render(request,'main/country.html',context = data)

def female_country(request): #use case 1 countries by number of medal
        sparqlQueries = get_data()
        country , count = sparqlQueries.top10_country_femalecount()
        
        data = {
            "name":zip(country,count),
            'flag':True,
            'suffix':'',
            'title':'TOP 10 Countries With Highest Female Athlete'
        }
    
        return render(request,'main/country.html',context = data)

def male_country(request): #use case 1 countries by number of medal
        sparqlQueries = get_data()
        country , count = sparqlQueries.top10_country_malecount()
        
        data = {
            "name":zip(country,count),
            'flag':True,
            'suffix':'',
            'title':'TOP 10 Countries With Highest male Athlete'
        }
    
        return render(request,'main/country.html',context = data)



def country_search(request):
    
    context = {
        'flag2':True,
    }
    
    if request.method == "POST" :
           sparqlQueries = get_data()
           name = request.POST.get("new")
           country_list = sparqlQueries.search_country_match(name.title())
           countries = [ x for x in country_list if "/" not in x ]
           context = {
            'countries':countries,
            'flag2':True
            }
           return render(request,'main/country.html',context = context)
    return render(request,'main/country.html',context=context)


def country_profile(request, name):
    sparqlQuery = get_data()
    avg_age , avg_height , avg_weight = sparqlQuery.get_country_stat(name.title())
    gold_count =sparqlQuery.no_of_gold(name)
    athlete_count =sparqlQuery.athlete_count(name)
    
    
    context = {
        'avg_age': round(avg_age,3),
        'avg_height':round(avg_height,3),
        'avg_weight':round(avg_weight,3),
        'country':name ,
        'no_of_gold':gold_count,
        'athlete_count':athlete_count,
        
        
    }
    return render(request,'main/country_profile.html',context)

def country_search_stat(request):
    
    context = {
        'flag3':True,
    }
    
    if request.method == "POST" :
           sparqlQueries = get_data()
           name = request.POST.get("new")
           country_list = sparqlQueries.search_country_match(name.title())
           countries = [ x for x in country_list if "/" not in x ]
           context = {
            'countries':countries,
            'flag3':True
            }
           return render(request,'main/country.html',context = context)
    return render(request,'main/country.html',context=context)

def country_statatics(request, name):
    sparqlQuery = get_data()
    avg_age , avg_height , avg_weight = sparqlQuery.get_country_stat(name.title())
    
    other_age , other_height , other_weight =  sparqlQuery.stats_other_country(name)
    years , avg_female_age , avg_female_height , avg_female_weight = sparqlQuery.average_female_stats_country(name.title())
    _ , avg_male_age , avg_male_height , avg_male_weight = sparqlQuery.average_male_stats_country(name.title())
    
    
    context = {
        'avg_age': round(avg_age,3),
        'avg_height':round(avg_height,3),
        'avg_weight':round(avg_weight,3),
        'country':name ,
        "other_age":other_age , 
        "other_height":other_height ,
        "other_weight":other_weight ,
        'years':years, 
        "avg_male_height":avg_male_height,
        "avg_male_age":avg_male_age,
        "avg_male_weight":avg_male_weight,
        "avg_female_height":avg_female_height,
        "avg_female_age":avg_female_age,
        "avg_female_weight":avg_female_weight,
        
    }
    return render(request,'main/country_statics.html',context)

def query_endpoint(request): #for quering data from the olympics rdf
    common_prefixes = """
    PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX gen: <http://wallscope.co.uk/resource/olympics/gender/>
    PREFIX dbo: <http://dbpedia.org/ontology/>
    PREFIX na: <http://wallscope.co.uk/resource/olympics/athlete/>
    PREFIX dbp: <http://dbpedia.org/property/>
    SELECT * 
    WHERE {
        ?A ?B ?C
    }
    LIMIT 20
    """
    context = {
        "preload":common_prefixes
        }
    if request.method == "POST" :
        sparq_query = request.POST.get('query')
        
        query = get_data()
        output = query.run_query(sparq_query)
        df = pd.read_table(StringIO(output),sep=",")
        length = df.shape[0]
        html = df.to_html(classes=["border border-gray-800",'table-fixed'],render_links = True)
        context['preload'] = sparq_query
        context['length'] = length
            
        context['output'] = html
            
        return render(request,'main/query.html',context=context)
    return render(request,'main/query.html',context=context)

def sparql_endpoint(request):
    return render(request,'main/sparql.html')

    
def ontology(request):
    with open('main/olympic.owl','r') as f:
        lines = f.readlines()
    return HttpResponse(lines,content_type='text/xml')

def sports(request):
    return render(request,'main/sports.html')

def all_event(request,sport):
    name = "".join(x for x in sport if x.isalnum())
    sparqlQ = get_data()
    events = sparqlQ.get_evenets(sport)
    context = {
        'events':events,
        'flag3':True,
        'title':'All Events in '+sport
    }
    return render(request,'main/sports.html',context)


def all_sports(request):
    sparqlQ = get_data()
    events = sparqlQ.all_sports()
    context = {
        'sports':events,
        'flag':True,
        'title':"ALL SPORTS"
    }
    
    return render(request,'main/sports.html',context)

def all_sports_forevents(request):
    sparqlQ = get_data()
    events = sparqlQ.all_sports()
    events = [x for x in events if x.isalnum()]
    context = {
        'sports':events,
        'flag':True,
        'flag2':True,
        'title':"ALL SPORTS"
    }
    
    
    return render(request,'main/sports.html',context)
def all_sports_fortopplayer(request):
    sparqlQ = get_data()
    events = sparqlQ.all_sports()
    events = [x for x in events if x.isalnum()]
    context = {
        'sports':events,
        'flag':True,
        'flag4':True,
        'title':"ALL SPORTS"
    }
    
    
    return render(request,'main/sports.html',context)

def top_athlete(request,sport):
    sparqlQ = get_data()
    name,medal = sparqlQ.top_scorer(sport)
    context = {
        'name':zip(name,medal),
        'flag5':True,
        'title':'Top 10 Player in '+sport,
    }
    return render(request,'main/sports.html',context)
