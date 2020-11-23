import flask, json
from flask import request, jsonify


app = flask.Flask(__name__)
app.config["DEBUG"] = True

empty_book ={
    "id": 0,
    "title": "null",
    "author": "null",
    "first_sentence": "null",
    "year_published": 0,
    }

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

# A route to return all of the available entries in our catalog.
@app.route('/books/', methods=['GET', 'POST'])
def api_all():
    if request.method == 'GET':
        with open("./api/books.json", "r") as books:
            novels = books.read()
            return novels
    else:
        print(request.values.get('id'))
        new_book ={
            "id": int(request.values.get('id')),
            "title": request.values.get('title'),
            "author": request.values.get('author'),
            "first_sentence": request.values.get('fs'),
            "year_published": int(request.values.get('year')),
        }
        with open("./api/books.json") as json_file:
            data = json.load(json_file)
        
            temp = data['books']

            temp.append(new_book)

        with open("./api/books.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

        print(new_book)
        return new_book

app.run(host='0.0.0.0')