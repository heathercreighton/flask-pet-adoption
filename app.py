from flask import Flask
from helper import pets

app = Flask(__name__)

@app.route('/')
def index():
  return """<h1>Adopt a Pet!</h1>
  <p> Browse throught the links below to find you new furry friend:
  <ul>
  <li><a href='/animals/dogs'>Dogs</a></li>
  <li><a href='/animals/cats'>Cats</a></li>
  <li><a href='/animals/rabbits'>Rabbits</li>
  </ul>"""

@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = """<h1>List of pets</h1>"""
  pets_array = pets[pet_type]
  pet_list = "<ul>"
  for i, p in enumerate(pets_array):
    pet_list += f"<li><a href='/animals/{pet_type}/{i}'>{p['name']}</a></li>"
  html += pet_list + "</ul>"
  return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type,pet_id):
  pet_info = pets[pet_type][pet_id]
  pet_name = f"""<h1>{pet_info['name']}</h1>
  <img src={pet_info['url']} />
  <p>{pet_info['description']}</p>
  <ul>
  <li>age: {pet_info['age']}</li>
  <li>breed: {pet_info['breed']}</li>
  """
  return pet_name
    

