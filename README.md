<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Patagonian Challenge</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Patagonian Challenge.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Testing API](#testing)
- [Built Using](#built_using)
- [Author](#author)


## 🧐 About <a name = "about"></a>

Challenge Patagonian:
1. Script that loads into database all the songs from a list of Artist's IDs.
2. Api REST that implements all the endpoints described on the api_pagination.raml
3. Documentation of Api in api_pagintation.html
4. The database is mysql and it's running over AWS.

Here is the access
```
databaseName: patagonian
user: patagonian
password:  PataSongs123_
host: patagonian1.c3hldx0oqqnn.us-east-1.rds.amazonaws.com
port: 3306
```


### Prerequisites <a name = "prerequisites"></a>

To run the project you need some prerequisites:

1. You have installed python 3.6 
2. run pip install -r requirements.txt to install all dependencies
3. Go to https://developer.spotify.com/dashboard/applications and create an app. Keep your Client ID and Client Secret
4. Set the environment variables: 

FOR LINUX:
```
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
```
FOR WINDOWS
```
set SPOTIPY_CLIENT_ID='your-spotify-client-id'
set SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
```

## 🎈 Usage <a name="usage"></a>

With environments variables of spotify, we use the public api of spotify.com

Load Songs: 
```
load_spotify.cmd -i <artis_id_1>,<artis_id_2>,<artis_id_3>...
```

The application will load the songs

For example, if you would like to load Sebastian Yatra and Weezer songs:
```
load_spotify.cmd -i 07YUOmWljBTXwIseAUd9TW,2MLHyLy5z5l5YRp7momlgw
```
Get Help:
```
load_spotify.cmd --help
```


---
Run API Rest.

go to patagonian directory (there is manage.py file)

run: python manage.py runserver

Server runs at http://localhost:8000

## 🚀 Testing the API <a name = "testing"></a>

To test Rest API, you can use the Rest Client you want.

For example you can use postman.

Open Postman and import Challenge Tecnico API.postman_collection.json

You can test REST Api now.

Another ways are:
1) Test app is following api_pagination.raml specs
2) Run simple reponse test without check content:

    ```
    python manage.py test
    ```
3) You could go to http://127.0.0.1:8000/ and navigate exposed api.
    (remember that artistName param is required.)

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Language
- [Django](https://www.djangoproject.com/) - Web Framework
- [Django Rest Framework](https://www.django-rest-framework.org/) - Rest Framework
- [Postman](https://www.postman.com/) - Rest Client
- [Mysql](https://www.postman.com/) - Databse
- [AWS RDS](https://aws.amazon.com/es/rds/) - Amazon Relational Database Service

of course, Google and some others...

## ✍️ Authors <a name = "author"></a>

- [@diegorichi](http://www.diegorichi.com.ar/)

