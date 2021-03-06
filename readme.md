**Español**

Este plugin fue desarrollado como parte de una estrategia **Open Source** para medios de todo el mundo basada en el CMS **Wordpress**.  
Haciendo click en este [enlace](https://tiempoar.com.ar/proyecto-colaborativo/) se puede encontrar más información sobre el proyecto, así como las lista de plugins que complementan a este para tener un sitio completamente funcional.

**English**

This plugin was developed as part of an **Open Source** strategy for worldwide media based on the CMS **WordPress**.
By clicking on this [link](https://tiempoar.com.ar/proyecto-colaborativo/) you can find more information about the project, as well as the list of complements that complement it to have a fully functional site.

# CONTENT BALANCER REST API
EN

This API extracts keywords from text. The algorithm uses a neural network specifically designed for natural language processing.
It is based on the TextRank algorithm that extracts words according to their weight in the text.
For this occasion we have limited the algorithm so that only nouns, pronouns and verbs of the text to be consulted are taken into account.

ES

Esta API extrae palabras clave de un texto. El algoritmo utiliza una red neuronal diseñada específicamente para el procesamiento del lenguaje natural. Se basa en el algoritmo TextRank que extrae palabras según su peso en el texto. Para esta ocasión hemos acotado el algoritmo para que solo se tengan en cuenta los sustantivos, pronombres y verbos del texto a consultar.



## Run as a Flask app

    1. Set the flask app
        FLASK_APP=/app/app.py

    2. Run the app
        flask run --host=0.0.0.0
        
### To deploy in production create a Docker image

# API method

### Request

`POST /api/textrank`

    Headers:
    Accept: 'application/json'

    Body example:
    {
        "query_string": "text",
        "keywords_qty": "number of tags to return"
    }

### Response

    Status: 200 OK
    Content-Type: application/json

    Content:
    {
        "keywords": [],
        "text": "text"
    }

### Request example

    {
        "query_string":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        "keywords_qty": "10"
    }

### Response example

    {
        "keywords": [
            "Lorem",
            "Ipsum",
            "typesetting",
            "text",
            "type",
            "dummy",
            "electronic",
            "scrambled",
            "containing",
            "leap"
        ],
        "text": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    }
