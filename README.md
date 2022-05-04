# Data Visualisation of 120 Years of  Olympics Record
A Django and symentics web based open source webapp to visualise Data of Olympics .

## Screenshots 

![App Screenshot](https://i.ibb.co/TWrRQTC/1.png)
![App Screenshot](https://i.ibb.co/4WTTHD6/2.png)
![App Screenshot](https://i.ibb.co/ZVZ3SQC/3.png)
![App Screenshot](https://i.ibb.co/jVPYY9K/4.png)
![App Screenshot](https://i.ibb.co/KwxxXkz/5.png)
![App Screenshot](https://i.ibb.co/SKcY3vz/6.png)
![App Screenshot](https://i.ibb.co/rpKLrR4/7.png)
![App Screenshot](https://i.ibb.co/tJWgWzF/8.png)
![App Screenshot](https://i.ibb.co/fQDVfrr/9.png)
![App Screenshot](https://i.ibb.co/VVwWY4R/10.png)


## Python Libraries

 - [DJANGO](https://www.djangoproject.com/)
 - [tailwindcss](https://tailwindcss.com/)
 - [SPARQLWrapper](https://libraries.io/pypi/SPARQLWrapper)
 


## Semantic Web

 - [Introduction](https://medium.com/wallscope/tackling-big-data-challenges-with-linked-data-278b0761a6de)
 - [Creating Linked Data ](https://medium.com/wallscope/creating-linked-data-31c7dd479a9e/)
 - [SPARQL Queries ](https://www.youtube.com/playlist?list=PLea0WJq13cnA6k4B6Tr1ljj2nleUl9dZt)
 

## Data Source 
- [Olympics Turtle File](https://github.com/wallscope/olympics-rdf)

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file
- SECRET_KEY= Secret key of your django project
- DEBUG = "False"
- ALLOWED_HOSTS = ""



## Running blazegraph Server 
- ### Note - Before running blazeraph you system must have java installed in it .

- [Download blazegraph](https://github.com/blazegraph/database/releases/tag/BLAZEGRAPH_2_1_6_RC)

- Go to the directory where blazegraph jar file is stored
```bash
  java -server -Xmx4g -jar blazegraph.jar
```
- Blazegraph will now be running on port 9999 . Run the port in your browser and load the olympic turtle rdf file .
    
## Run Locally

Clone the project

```bash
  git clone https://github.com/ankushbisht01/120-years-olympics
```

Go to the project directory

```bash
  cd 120-years-olympics
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py runserver
```


## Lessons Learned

By making the following Project I explored the new way of storing and quering data and learned the importance of semantic web over traditional data storage techniques . 
Know more About Symentic Web and Linked Data - https://www.youtube.com/playlist?list=PLea0WJq13cnDDe8V7eVLReIaOnFztOEAq
