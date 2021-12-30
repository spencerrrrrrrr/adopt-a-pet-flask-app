from flask import Flask
from helper import pets

app = Flask(__name__)

@app.route('/')
def index():
  return '''
  <h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friend:</p>
  <ul>
  <li><a href="/animals/dogs">Dogs</a></li>
  <li><a href="/animals/cats">Cats</li>
  <li><a href="/animals/rabbits">Rabbits</li>
  </ul>
  '''

@app.route('/animals/<pet_type>')
def animals(pet_type):
  html =  f'<h1>List of {pet_type}</h1>'
  html+='<ul>'
  for pet in pets[pet_type]:
    html+=f'<li>{pet["name"]}</li>'
  html+='</ul>'
  return html