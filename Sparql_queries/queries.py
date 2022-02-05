from SPARQLWrapper import SPARQLWrapper, JSON , CSV
import pandas as pd
import numpy as np
class get_data:

    def __init__(self):
        self.sparql = SPARQLWrapper('https://olympics120.herokuapp.com/olympics/sparql')

    def age_vs_medal(self):
        
        self.sparql.setQuery("""
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX dbp: <http://dbpedia.org/property/>
        PREFIX na: <http://wallscope.co.uk/resource/olympics/athlete/>
        SELECT ?age (COUNT(?medal) As ?noOfMedals)
        WHERE {
        ?instance walls:athlete ?athelete ;
                walls:medal ?medal .
        ?athelete foaf:age ?age
        
                    
        
        }
        GROUP BY ?age
        ORDER BY ?age

        """
        )
        
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        medals_count = []
        age= []
        for result in results["results"]["bindings"]:
            medals_count.append( result["noOfMedals"]["value"])
            age.append(result["age"]["value"])
        return [medals_count , age]

    def ath_age_medals(self,name):
        
            self.sparql.setQuery("""
            PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX dbp: <http://dbpedia.org/property/>
            PREFIX na: <http://wallscope.co.uk/resource/olympics/athlete/>
            SELECT  (COUNT(?medal) As ?noOfMedals)
            WHERE {
            ?instance walls:athlete ?athelete ;
                    walls:medal ?medal .
            ?athelete rdfs:label ?name .
            filter contains(?name , \""""+name+"""\")
            
                        
            
            }
            
            ORDER BY ?age

            """
            )
            
            self.sparql.setReturnFormat(JSON)
            results = self.sparql.query().convert()
            
            medals_count = None
            
            for result in results["results"]["bindings"]:
                medals_count = ( result["noOfMedals"]["value"])
                
            return medals_count

    def athlete_details(self,name):
        query = """
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX dbp: <http://dbpedia.org/property/>
        PREFIX na: <http://wallscope.co.uk/resource/olympics/athlete/>
        SELECT (COUNT(?medal) As ?noOfMedals)
        WHERE {
        ?instance walls:athlete  ?athlete .
        optional {  ?instance  walls:medal ?medal . }
        filter contains(?names,\""""+name+"""\")
        
        
                    
        
        }
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        
        for result in results["results"]["bindings"]:
            no_of_medal = ( result["noOfMedals"]["value"])
            
        return no_of_medal

    def get_game_name(self,name_of_athlete):
        query ="""
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX dbp: <http://dbpedia.org/property/>
        PREFIX na: <http://wallscope.co.uk/resource/olympics/athlete/>

        SELECT ?sportname
        WHERE {
        ?instance walls:athlete na:"""+name_of_athlete+""" ;
                walls:event   ?event .
         ?event rdfs:subClassOf ?sport .
          ?sport rdfs:label ?sportname        
        
        }
		Group by ?sportname
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        sportsname = []
        for result in results["results"]["bindings"]:
            sportsname.append( result["sportname"]["value"])
            
        return sportsname

    def top_male_athlete(self):
        query = """
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX gen: <http://wallscope.co.uk/resource/olympics/gender/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX na: <http://wallscope.co.uk/resource/olympics/athlete/>
        SELECT ?name  (COUNT(?medal) As ?noOfMedals)
        WHERE {
        ?instance walls:athlete ?athlete ;
                walls:medal ?medal .
        ?athlete rdfs:label ?name ;
                foaf:gender gen:M .
        
        
        }

        GROUPBY ?name 
        ORDERBY DESC(?noOfMedals) 
        LIMIT 3
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        sportsname = []
        medal_count = []
        for result in results["results"]["bindings"]:
            sportsname.append( result["name"]["value"])
            medal_count.append(result["noOfMedals"]["value"])
            
        return [sportsname,medal_count]


    def top_female_athlete(self):
        query = """
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX gen: <http://wallscope.co.uk/resource/olympics/gender/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX na: <http://wallscope.co.uk/resource/olympics/athlete/>
        SELECT ?name  (COUNT(?medal) As ?noOfMedals)
        WHERE {
        ?instance walls:athlete ?athlete ;
                walls:medal ?medal .
        ?athlete rdfs:label ?name ;
                foaf:gender gen:F .
        
        
        }

        GROUPBY ?name  
        ORDERBY DESC(?noOfMedals)
        LIMIT 3
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        sportsname = []
        medal_count = []
        for result in results["results"]["bindings"]:
            sportsname.append( result["name"]["value"])
            medal_count.append(result["noOfMedals"]["value"])
            
        return [sportsname,medal_count]

    
    def get_country_stat(self,country_name):
        query = """
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX gen: <http://wallscope.co.uk/resource/olympics/gender/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX tm: <http://wallscope.co.uk/resource/olympics/team/>
        PREFIX na: <http://wallscope.co.uk/resource/olympics/athlete/>
        PREFIX dbp: <http://dbpedia.org/property/>

        SELECT   (AVG(?age) as ?AVerage_age) (AVG(?height) as ?AVG_Hieght)  (AVG(?weight) as ?AVG_Weight)
        WHERE {
        ?instance walls:athlete ?athlete ;
                    walls:noc ?noc .
                
        ?athlete rdfs:label ?name ;
                    foaf:age  ?age ;
                dbo:height ?height ;
                dbo:weight ?weight .
        
        
            ?noc dbo:ground ?team.
  		?team rdfs:label ?teamname .
          filter contains(?teamname , \""""+country_name+"""\")
          
          
            
        
        
        }
		
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        
        average_age = None
        average_height = None
        average_weight = None
        for result in results["results"]["bindings"]:
            
            average_height= (result["AVG_Hieght"]["value"])
            average_age = (result["AVerage_age"]["value"])
            average_weight= (result["AVG_Weight"]["value"])
            
        return [float(average_age),float(average_height),float(average_weight)]

    def stats_other_country(self,name_of_the_excluding_country):
        query = """
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX gen: <http://wallscope.co.uk/resource/olympics/gender/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX tm: <http://wallscope.co.uk/resource/olympics/team/>
        PREFIX na: <http://wallscope.co.uk/resource/olympics/athlete/>
        PREFIX dbp: <http://dbpedia.org/property/>

        SELECT   (AVG(?age) as ?AVerage_age) (AVG(?height) as ?AVG_Hieght)  (AVG(?weight) as ?AVG_Weight)
        WHERE {
        ?instance walls:athlete ?athlete ;
                    walls:noc ?noc .
                
        ?athlete rdfs:label ?name ;
                    foaf:age  ?age ;
                dbo:height ?height ;
                dbo:weight ?weight .
        
        
            ?noc dbo:ground ?team .
          minus {?team rdfs:label \""""+name_of_the_excluding_country+"""\" . }
          
        }
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        average_age = None
        average_height = None
        average_weight = None
        for result in results["results"]["bindings"]:
            
            average_age = (result["AVerage_age"]["value"])
            average_height = (result["AVG_Hieght"]["value"])
            average_weight = (result["AVG_Weight"]["value"])
            
        return [average_age,average_height,average_weight]

    def average_female_stats(self):
        query= """
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX gen: <http://wallscope.co.uk/resource/olympics/gender/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX na: <http://wallscope.co.uk/resource/olympics/athlete/>
        PREFIX dbp: <http://dbpedia.org/property/>

        SELECT ?year (AVG(?age) as ?avg_age) (AVG(?height) as ?avg_height)  (AVG(?weight) as ?avg_weight)
        WHERE {
        ?instance walls:athlete ?athlete ;
                walls:games   ?games.
        ?games dbo:year  ?year .
        ?athlete rdfs:label ?name ;
                foaf:gender gen:F;
                    foaf:age  ?age ;
                dbo:height ?height ;
                dbo:weight ?weight .
        
        
        }

        GROUP BY ?year
        order by ?year
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        year = []
        average_age = []
        average_height = []
        average_weight = []
        for result in results["results"]["bindings"]:
            year.append( result["year"]["value"])
            average_height.append(result["avg_height"]["value"])
            average_age.append(result["avg_age"]["value"])
            average_weight.append(result["avg_weight"]["value"])
            
        return [year,average_age,average_height,average_weight]
    
    def average_male_stats(self):
        query= """
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX gen: <http://wallscope.co.uk/resource/olympics/gender/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX na: <http://wallscope.co.uk/resource/olympics/athlete/>
        PREFIX dbp: <http://dbpedia.org/property/>

        SELECT ?year (AVG(?age) as ?avg_age) (AVG(?height) as ?avg_height)  (AVG(?weight) as ?avg_weight)
        WHERE {
        ?instance walls:athlete ?athlete ;
                walls:games   ?games.
        ?games dbo:year  ?year .
        ?athlete rdfs:label ?name ;
                foaf:gender gen:M;
                    foaf:age  ?age ;
                dbo:height ?height ;
                dbo:weight ?weight .
        
        
        }

        GROUP BY ?year
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        year = []
        average_age = []
        average_height = []
        average_weight = []
        for result in results["results"]["bindings"]:
            year.append( result["year"]["value"])
            average_height.append(result["avg_height"]["value"])
            average_age.append(result["avg_age"]["value"])
            average_weight.append(result["avg_weight"]["value"])
            
        return [year,average_age,average_height,average_weight]
    # get top 10 eldest athlete 
    def top10_ages_old(self):
        query = """
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs:  <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        select ?names ?age
        where {
        ?instance walls:athlete ?athlete.
        ?athlete rdfs:label ?names ;
                 foaf:age ?age .
        }
        Group by ?names ?age
        Order by DESC (?age)
        LIMIT 10
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        athlete_name = []
        age = []
        
        for result in results["results"]["bindings"]:
            athlete_name.append( result["names"]["value"])
            age.append(result["age"]["value"])
        return [athlete_name , age]
    #top 10 youngest athlete
    def top10_ages_young(self):
        query = """
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs:  <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        select ?names ?age
        where {
        ?instance walls:athlete ?athlete.
        ?athlete rdfs:label ?names ;
                 foaf:age ?age .
        }
        Group by ?names ?age
        Order by  (?age)
        LIMIT 10
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        athlete_name = []
        age = []
        
        for result in results["results"]["bindings"]:
            athlete_name.append( result["names"]["value"])
            age.append(result["age"]["value"])
        return [athlete_name , age]

    #get top 10 athlete who won max medals
    def top10_medals(self):
        query = """
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs:  <http://www.w3.org/2000/01/rdf-schema#>
        select ?names (Count(?medal) as ?totalmedal)
        where {
        ?instance walls:athlete ?athlete.
        OPTIONAL { ?instance walls:medal ?medal . }
        ?athlete rdfs:label ?names .
        }
        group by ?names
        Order by DESC (?totalmedal)
        LIMIT 10
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        athlete_name = []
        medals = []
        
        for result in results["results"]["bindings"]:
            athlete_name.append( result["names"]["value"])
            medals.append(result["totalmedal"]["value"])
        
        return [athlete_name , medals]

    #get top 10 tallest athlete
    def top_10_height(self):
        query = """
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs:  <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        select ?names ?height
        where {
        ?instance walls:athlete ?athlete.
        ?athlete rdfs:label ?names ;
                dbo:height ?height.

        }
       
        Order by DESC (?height)
        LIMIT 10
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        athlete_name = []
        height = []
        
        for result in results["results"]["bindings"]:
            athlete_name.append( result["names"]["value"])
            height.append(result["height"]["value"])
        
        return [athlete_name , height]

    def top_10_weight(self):
        query = """
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs:  <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        select ?names ?weight
        where {
        ?instance walls:athlete ?athlete.
        ?athlete rdfs:label ?names ;
                dbo:weight ?weight.

        }
       
        Order by DESC (?weight)
        LIMIT 10
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        athlete_name = []
        weight = []
        
        for result in results["results"]["bindings"]:
            athlete_name.append( result["names"]["value"])
            weight.append(result["weight"]["value"])
        
        return [athlete_name , weight]

    def search(self,name):
        query = """
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs:  <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX ath: <http://wallscope.co.uk/resource/olympics/athlete/>
        select ?names (Count(?medal) as ?totalmedal)
        where {
        ?instance walls:athlete ath:"""+name+""" .
        OPTIONAL { ?instance walls:medal ?medal . }
        ath:"""+name+""" rdfs:label ?names
                               }
		group by ?names
        Order by DESC (?totalmedal)
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        athlete_name = []
        medals = []
        
        for result in results["results"]["bindings"]:
            athlete_name.append( result["names"]["value"])
            medals.append(result["totalmedal"]["value"])
        
        return [athlete_name , medals]

    def search_match(self,name):
        query = """
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs:  <http://www.w3.org/2000/01/rdf-schema#>
        select ?names (Count(?medal) as ?totalmedal)
        where {
        ?instance walls:athlete ?athlete.
        OPTIONAL { ?instance walls:medal ?medal . }
        ?athlete rdfs:label ?names .
        filter contains(?names,\""""+name+"""\")
        }
        group by ?names 
        Order by DESC (?totalmedal)
        LIMIT 100

        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        athlete_name = []
        medals = []
        
        for result in results["results"]["bindings"]:
            athlete_name.append( result["names"]["value"])
            medals.append(result["totalmedal"]["value"])
        
        return [athlete_name , medals]

    def athlete_Info(self,name):
        query = """
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX gen: <http://wallscope.co.uk/resource/olympics/gender/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX tm: <http://wallscope.co.uk/resource/olympics/team/>
        PREFIX na: <http://wallscope.co.uk/resource/olympics/athlete/>
        PREFIX dbp: <http://dbpedia.org/property/>

        SELECT   ?sportname ?age 
        WHERE {
        ?instance walls:athlete ?athlete ; 
                walls:event   ?event .
         ?event rdfs:subClassOf ?sport .
          ?sport rdfs:label ?sportname .
          
          ?athlete rdfs:label ?name;
				foaf:age ?age.
           filter contains(?name,\""""+name+"""\")
    
        }
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        sports_name = []
        ages = []
        
        for result in results["results"]["bindings"]:
            sports_name.append( result["sportname"]["value"])
            ages.append(result["age"]["value"])
        
        return [sports_name , ages]

    
	#get avergae age of an athlete 
    def avg_age(self , name ):
        query = """
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX gen: <http://wallscope.co.uk/resource/olympics/gender/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX tm: <http://wallscope.co.uk/resource/olympics/team/>
        PREFIX na: <http://wallscope.co.uk/resource/olympics/athlete/>
        PREFIX dbp: <http://dbpedia.org/property/>

        SELECT   (AVG(?age) as ?avg_age) 
        WHERE {
        ?instance walls:athlete ?athlete .
                
        ?athlete rdfs:label ?name ;
                    foaf:age  ?age .
                
          filter contains(?name, \""""+name+"""\")
        
        }
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        avg_ages = None
        
        
        for result in results["results"]["bindings"]:
            avg_ages = ( result["avg_age"]["value"])
            
        return avg_ages

	
    def athlete_stat(self,name):
        query = """
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX gen: <http://wallscope.co.uk/resource/olympics/gender/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX tm: <http://wallscope.co.uk/resource/olympics/team/>
        PREFIX na: <http://wallscope.co.uk/resource/olympics/athlete/>
        PREFIX dbp: <http://dbpedia.org/property/>

        SELECT   (AVG(?age) as ?avg_age) (AVG(?height) as ?avg_height)  (AVG(?weight) as ?avg_weight)
        WHERE {
        ?instance walls:athlete ?athlete .
                
        ?athlete rdfs:label ?name ;
                    foaf:age  ?age ;
                dbo:height ?height ;
                dbo:weight ?weight .
          filter contains(?name, \""""+name+"""\")
        
        }
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        avg_ages = []
        avg_height = []
        avg_weight = []
        
        for result in results["results"]["bindings"]:
            avg_ages.append( result["avg_age"]["value"])
            avg_height.append(result["avg_height"]["value"])
            avg_weight.append(result["avg_weight"]["value"])
        return [avg_ages , avg_height , avg_weight]

    def other_athlete_stat(self,name):
        query = """
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX gen: <http://wallscope.co.uk/resource/olympics/gender/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX tm: <http://wallscope.co.uk/resource/olympics/team/>
        PREFIX na: <http://wallscope.co.uk/resource/olympics/athlete/>
        PREFIX dbp: <http://dbpedia.org/property/>

        SELECT   (AVG(?age) as ?avg_age) (AVG(?height) as ?avg_height)  (AVG(?weight) as ?avg_weight)
        WHERE {
        ?instance walls:athlete ?athlete .
                
        ?athlete rdfs:label ?name ;
                    foaf:age  ?age ;
                dbo:height ?height ;
                dbo:weight ?weight .
          
        
        }
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        avg_ages = []
        avg_height = []
        avg_weight = []
       
        for result in results["results"]["bindings"]:
            avg_ages.append( result["avg_age"]["value"])
            avg_height.append(result["avg_height"]["value"])
            avg_weight.append(result["avg_weight"]["value"])
        return [avg_ages , avg_height , avg_weight]  

    # Get the list of all countries participated in olympics 
    def country_list(self):
        query = """
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX gen: <http://wallscope.co.uk/resource/olympics/gender/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX tm: <http://wallscope.co.uk/resource/olympics/team/>
        PREFIX na: <http://wallscope.co.uk/resource/olympics/athlete/>
        PREFIX dbp: <http://dbpedia.org/property/>

        SELECT   ?teamname
        WHERE {
        ?instance walls:noc ?noc .
           
            ?noc dbo:ground ?team .
            ?team rdfs:label ?teamname.
          
        }

        GROUP BY   ?teamname
        ORDER BY ?teamname
		

       """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        
        countries = []
        
        for result in results["results"]["bindings"]:
            countries.append( result["teamname"]["value"])
            
        return countries

    #search particular country
    def search_country_match(self,name):
        query = """
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX gen: <http://wallscope.co.uk/resource/olympics/gender/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX tm: <http://wallscope.co.uk/resource/olympics/team/>
        PREFIX na: <http://wallscope.co.uk/resource/olympics/athlete/>
        PREFIX dbp: <http://dbpedia.org/property/>

        SELECT   ?teamname
        WHERE {
        ?instance walls:noc ?noc .
           
            ?noc dbo:ground ?team .
            ?team rdfs:label ?teamname.
          filter contains(?teamname, \""""+name+"""\")
          
        }

        GROUP BY   ?teamname

        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        country = []
        
        
        for result in results["results"]["bindings"]:
            country.append( result["teamname"]["value"])
            
        
        return country

    #number of gold medal won by a country 
    def no_of_gold(self,country):
        query = """
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        
        PREFIX dbo: <http://dbpedia.org/ontology/>
        

        SELECT   (count(?medalname) as ?noofgold)
        WHERE {
        ?instance walls:athlete ?athlete ;
                    walls:noc ?noc .
                
        ?instance walls:medal ?medal .
                  ?medal rdfs:label ?medalname .
                             
        
        
        
            ?noc dbo:ground ?team . 
            ?team rdfs:label ?teamname . 
          filter (?teamname = \""""+country.title()+"""\")
          filter contains(?medalname , "Gold" )
          
          
            
        
        
        }
        
        """

        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        gold_count = None
        
        
        for result in results["results"]["bindings"]:
            gold_count = ( result["noofgold"]["value"])
            
        
        return gold_count
    
    #total Athlete particiapted in from that country in olympics 
    def athlete_count(self,country):
        query = """
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        
        PREFIX dbo: <http://dbpedia.org/ontology/>
        

        SELECT  ( count(?athlete) as ?athlete_count )
        WHERE {
        ?instance walls:athlete ?athlete ;
                    walls:noc ?noc .
             
            ?noc dbo:ground ?team .
            ?team rdfs:label ?teamname .
          filter (?teamname = \""""+country+"""\")
          
        }
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        athlete_count = None
        
        
        for result in results["results"]["bindings"]:
            athlete_count = ( result["athlete_count"]["value"])
            
        
        return athlete_count
    
    # Average female Statics of the country 
    def average_female_stats_country(self,country):
        query= """
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX gen: <http://wallscope.co.uk/resource/olympics/gender/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX na: <http://wallscope.co.uk/resource/olympics/athlete/>
        PREFIX dbp: <http://dbpedia.org/property/>

        SELECT ?year (AVG(?age) as ?avg_age) (AVG(?height) as ?avg_height)  (AVG(?weight) as ?avg_weight)
        WHERE {
        ?instance walls:athlete ?athlete ;
                walls:games   ?games;
                walls:noc ?noc .
        ?games dbo:year  ?year .
        ?athlete rdfs:label ?name ;
                foaf:gender gen:F;
                    foaf:age  ?age ;
                dbo:height ?height ;
                dbo:weight ?weight .
                ?noc dbo:ground ?team .
                ?team rdfs:label ?teamname .
                filter contains(?teamname , \""""+country+"""\")
        
        
        }

        GROUP BY ?year
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        year = []
        average_age = []
        average_height = []
        average_weight = []
        for result in results["results"]["bindings"]:
            year.append( result["year"]["value"])
            average_height.append(result["avg_height"]["value"])
            average_age.append(result["avg_age"]["value"])
            average_weight.append(result["avg_weight"]["value"])
            
        return [year,average_age,average_height,average_weight]
    
    #Average Male Statucs Of a Particular Country
    def average_male_stats_country(self,country):
        query= """
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX gen: <http://wallscope.co.uk/resource/olympics/gender/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX na: <http://wallscope.co.uk/resource/olympics/athlete/>
        PREFIX dbp: <http://dbpedia.org/property/>

        SELECT ?year (AVG(?age) as ?avg_age) (AVG(?height) as ?avg_height)  (AVG(?weight) as ?avg_weight)
        WHERE {
        ?instance walls:athlete ?athlete ;
                walls:games   ?games;
                walls:noc ?noc .
        ?games dbo:year  ?year .
        ?athlete rdfs:label ?name ;
                foaf:gender gen:M;
                    foaf:age  ?age ;
                dbo:height ?height ;
                dbo:weight ?weight .
                ?noc dbo:ground ?team .
                ?team rdfs:label ?teamname .
                filter contains(?teamname , \""""+country+"""\")
        
        }

        GROUP BY ?year
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        year = []
        average_age = []
        average_height = []
        average_weight = []
        for result in results["results"]["bindings"]:
            year.append( result["year"]["value"])
            average_height.append(result["avg_height"]["value"])
            average_age.append(result["avg_age"]["value"])
            average_weight.append(result["avg_weight"]["value"])
            
        return [year,average_age,average_height,average_weight]
    
    #Name of all Sports
    def all_sports(self):
        query = """
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX dbp: <http://dbpedia.org/property/>
        PREFIX na: <http://wallscope.co.uk/resource/olympics/athlete/>

        SELECT ?sportname
        WHERE {
        ?instance walls:athlete ?athlete ;
                walls:event   ?event .
         ?event rdfs:subClassOf ?sport .
          ?sport rdfs:label ?sportname        
        
        }
		Group by ?sportname
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        sports_name = []
        for result in results["results"]["bindings"]:
            sports_name.append( result["sportname"]["value"])
            
            
        return sports_name

    #Search for a particular Sports
    def search_sports(self,sportname):
        query = """
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX dbp: <http://dbpedia.org/property/>
        PREFIX na: <http://wallscope.co.uk/resource/olympics/athlete/>

        SELECT ?sportname
        WHERE {
        ?instance walls:athlete ?athlete ;
                walls:event   ?event .
         ?event rdfs:subClassOf ?sport .
          ?sport rdfs:label ?sportname 
          filter contains(?sportname , \""""+sportname+"""\")
        
        }
		Group by ?sportname
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        sports_name = []
        for result in results["results"]["bindings"]:
            sports_name.append( result["sportname"]["value"])
            
            
        return sports_name

    def insert_data(self,df:pd.DataFrame):
        
        sparql = SPARQLWrapper('https://olympicsttl.herokuapp.com/testolympics/update')
        count = 0
        
        for i in range(len(df)):
            
            first_col = df.loc[i]
            data = {i:j for i,j in zip(first_col.index,first_col.values)}
            uri_name = ''.join( i for i in data['Name'] if i.isalnum())
            uri_sex = "".join('male' if i =="M" else 'female' for i in data['Sex'] )
            team_uri =  ''.join( i for i in data['Team'] if i.isalnum())
            game_uri = ''.join( i for i in data['Event'] if i.isalnum())
            sport_uri = ''.join( i for i in data['Sport'] if i.isalnum())
            query = """
                prefix dbo: <http://dbpedia.org/ontology/> 
                prefix walls: <http://wallscope.co.uk/ontology/olympics/> 
                prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
                prefix owl: <http://www.w3.org/2002/07/owl#> 
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
                prefix foaf: <http://xmlns.com/foaf/0.1/> 
                Insert data { """
            
            query = query + f""" 
                    <http://wallscope.co.uk/resource/olympics/athlete/{uri_name}> a foaf:Person;
                    rdfs:label "{data['Name']}" .
                    <http://wallscope.co.uk/resource/olympics/gender/{data['Sex']}> rdfs:label "{uri_sex}" .
                    <http://wallscope.co.uk/resource/olympics/athlete/{uri_name}> foaf:gender <http://wallscope.co.uk/resource/olympics/gender/{data['Sex']}>.
                    <http://wallscope.co.uk/resource/olympics/NOC/{data['NOC']}> dbo:ground <http://wallscope.co.uk/resource/olympics/team/{team_uri}>;
                    rdfs:label "{data['NOC']}" .
                    <http://wallscope.co.uk/resource/olympics/team/{team_uri}> rdfs:label "{data['Team']}" .
                    <http://wallscope.co.uk/resource/olympics/games/{data['Year']}/{data['Season']}> a dbo:Olympics;
                    dbo:year "{data['Year']}"^^<http://www.w3.org/2001/XMLSchema#int> .
                    <http://wallscope.co.uk/resource/olympics/city/{data['City']}> a dbo:city;
                    rdfs:label "{data['City']}" .
                    <http://wallscope.co.uk/resource/olympics/games/{data['Year']}/{data['Season']}> dbo:location <http://wallscope.co.uk/resource/olympics/city/{data['City']}> .
                    <http://wallscope.co.uk/resource/olympics/season/{data['Season']}> a dbo:TimePeriod;
                    rdfs:label "{data['Season']}" .
                    <http://wallscope.co.uk/resource/olympics/games/{data['Year']}/{data['Season']}> walls:season <http://wallscope.co.uk/resource/olympics/season/{data['Season']}> .
                    <http://wallscope.co.uk/resource/olympics/event/{game_uri}> a dbo:SportsEvent;
                    rdfs:label "{data['Event']}" .
                    <http://wallscope.co.uk/resource/olympics/sports/{sport_uri}> rdfs:label "{data['Sport']}" .
                    <http://wallscope.co.uk/resource/olympics/event/{game_uri}> rdfs:subClassOf <http://wallscope.co.uk/resource/olympics/sports/{sport_uri}> .

                    <http://wallscope.co.uk/resource/olympics/instance/{game_uri}/{data['Year']}/{data['Season']}/{uri_name}> walls:athlete <http://wallscope.co.uk/resource/olympics/athlete/{uri_name}>;
                    walls:games <http://wallscope.co.uk/resource/olympics/games/{data['Year']}/{data['Season']}>;
                    walls:event <http://wallscope.co.uk/resource/olympics/event/{game_uri}>;
                    walls:noc <http://wallscope.co.uk/resource/olympics/NOC/{data['NOC']}> .

                    """
            try:
                if not(np.isnan(first_col.Age)):
                    query = query + (f'''<http://wallscope.co.uk/resource/olympics/athlete/{uri_name}> foaf:age "{data["Age"]}"^^<http://www.w3.org/2001/XMLSchema#int> .''')
                if isinstance(first_col['Medal'], str):
                    query = query + (f'''<http://wallscope.co.uk/resource/olympics/medal/{data["Medal"]}> rdfs:label "{data["Medal"]}" .
                            <http://wallscope.co.uk/resource/olympics/instance/{game_uri}/{data['Year']}/{data['Season']}/{uri_name}> walls:medal <http://wallscope.co.uk/resource/olympics/medal/{data['Medal']}> .''')
                if  not(np.isnan(first_col.Height)):
                    query = query + (f'''<http://wallscope.co.uk/resource/olympics/athlete/{uri_name}> dbo:height "{data['Height']}"^^<http://www.w3.org/2001/XMLSchema#int> . ''')
                if  not(np.isnan(first_col.Weight)):
                    query = query + (f'''<http://wallscope.co.uk/resource/olympics/athlete/{uri_name}> dbo:weight "{data['Weight']}"^^<http://www.w3.org/2001/XMLSchema#double> .''')
                query = query + '\n}'
                
                sparql.setQuery(query)
                sparql.setReturnFormat(JSON)
                results = sparql.query().convert()
                
                
            except Exception as e:
                print(e)
    def top10_medals_country(self):
        query = """
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX gen: <http://wallscope.co.uk/resource/olympics/gender/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX na: <http://wallscope.co.uk/resource/olympics/athlete/>
        PREFIX dbp: <http://dbpedia.org/property/>

        SELECT ?teamname (count(?medal) as ?totalmedal)
        WHERE {
        ?instance walls:noc ?noc ;
                walls:medal ?medal .
            
                ?noc dbo:ground ?team .
                ?team rdfs:label ?teamname .
                        
        }

        GROUP BY ?teamname
        Order By Desc(?totalmedal)
        Limit 10
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        country = []
        medals = []
        
        for result in results["results"]["bindings"]:
            country.append( result["teamname"]["value"])
            medals.append(result["totalmedal"]["value"])
        
        return [country , medals]
    def top10_country_femalecount(self):  #top 10 countries with highest female athlete 
        query="""
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX gen: <http://wallscope.co.uk/resource/olympics/gender/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX na: <http://wallscope.co.uk/resource/olympics/athlete/>
        PREFIX dbp: <http://dbpedia.org/property/>

        SELECT ?teamname  (count(?gender) as ?totalfemale)
        WHERE {
        ?instance walls:athlete ?athlete;
                walls:noc ?noc .
                
         ?athlete foaf:gender ?gender.
         ?gender rdfs:label "female" .
                ?noc dbo:ground ?team .
                ?team rdfs:label ?teamname .
                        
        }

        Group by ?teamname
        Order by DESC(?totalfemale)
       
        Limit 10
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        country = []
        female_count = []
        
        for result in results["results"]["bindings"]:
            country.append( result["teamname"]["value"])
            female_count.append(result["totalfemale"]["value"])
        
        return [country , female_count]


    def top10_country_malecount(self):  #top 10 countries with highest female athlete 
        query="""
        PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX gen: <http://wallscope.co.uk/resource/olympics/gender/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX na: <http://wallscope.co.uk/resource/olympics/athlete/>
        PREFIX dbp: <http://dbpedia.org/property/>

        SELECT ?teamname  (count(?gender) as ?totalmale)
        WHERE {
        ?instance walls:athlete ?athlete;
                walls:noc ?noc .
                
         ?athlete foaf:gender ?gender.
         ?gender rdfs:label ?gendertype.
                ?noc dbo:ground ?team .
                ?team rdfs:label ?teamname .
        filter contains(?gendertype ,'male')
                        
        }

        Group by ?teamname
        Order by DESC(?totalmale)
       
        Limit 10
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        country = []
        male_count = []
        
        for result in results["results"]["bindings"]:
            country.append( result["teamname"]["value"])
            male_count.append(result["totalmale"]["value"])
        
        return [country , male_count]

    def run_query(self,query):
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(CSV)
        results = self.sparql.query().convert().decode("utf-8")
        return results
                
        
        
