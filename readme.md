# CONTENT BALANCER REST API

This API extracts keywords from text. The algorithm uses a neural network specifically designed for natural language processing.
It is based on the TextRank algorithm that extracts words according to their weight in the text.
For this occasion we have limited the algorithm so that only nouns, pronouns and verbs of the text to be consulted are taken into account.

## Install

    1. Set the flask app
        FLASK_APP=/app/app.py

    2. Run the app
        flask run --host=0.0.0.0

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
