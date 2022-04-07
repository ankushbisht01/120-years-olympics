from django.urls import path
from main import views




urlpatterns =[
    path('athlete/',views.athlete , name = "athlete"),
    path('medal_athlete/',views.medal_athlete , name = "medal-athlete"),
    path('height_athlete/',views.height_athlete , name = "height-athlete"),
    path('weight_athlete/',views.weight_athlete , name = "weight-athlete"),
    path('age_athlete_old/',views.age_athlete_old , name = "age-athlete"),
    path('age_athlete_young/',views.age_athlete_young , name = "age-athlete-young"),
    path('athlete_search/',views.athlete_search , name = "athlete-search"),
    path('athlete_stat_search/',views.athlete_stat_search , name = "athlete-stat-search"),
    path('athlete_profile/<str:name>',views.ath_profile , name = "athlete-profile"),
    path('athlete_stats/<str:name>',views.ath_stats , name = "athlete-stats"),

    path('country/',views.country , name = "country"),
    path('medal_country/',views.medal_country , name = "medal-country"),
    path('female_count_country/',views.female_country , name = "female-country-count"),
    path('male_count_country/',views.male_country , name = "male-country-count"),
    path('country_search/',views.country_search , name = "country-search"),
    path('country_search_statatics/',views.country_search_stat , name = "country-search-statatics"),
    path('country_profile/<str:name>',views.country_profile , name = "country-profile"),
    path('country_statatics/<str:name>',views.country_statatics , name = "country-statatics"),

    path('sparql/',views.sparql_endpoint,name='sparql'),
    
    path('ontology/',views.ontology,name='ontology'),


    path('sports/',views.sports ,name='sports'),
    path("allsports/",views.all_sports , name='allsports'),
    path("allsports_event/",views.all_sports_forevents , name='allsportsevent'),
    path("allsports_player/",views.all_sports_fortopplayer , name='allsportsplayer'),
    path('events/<str:sport>',views.all_event ,name='all_event'),
    path('top_player/<str:sport>',views.top_athlete ,name='top_athlete'),


    
    path('',views.index , name = "index")

]