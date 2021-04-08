from flask import Flask
from data import pets

app = Flask(__name__)


@app.route('/')
def index():
    return """
  <h1>Adpot a Pet!</h1>
  <p>Browse through the links below to find your new furry friend:</p>
  <ul>
    <li><a href='/animals/dogs'>Dogs</a></li>
    <li><a href='/animals/cats'>Cats</a></li>
    <li><a href='/animals/rabbits'>Rabbits</a></li>
  </ul>
  """


@app.route('/animals/<pet_type>')
def animals(pet_type):
    html = f"""
    <h1>List of {pet_type}</h1>
  """
    pet_list = "<ul>"
    for idx, item in enumerate(pets[pet_type]):
        pet_list += f"<li><a href='{pet_type}/{idx}'>{item['name']}</a></li>"
    pet_list += "</ul>"
    html += pet_list
    return html


@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    pet_obj = pets[pet_type][pet_id]
    html = f"""<h1 style='margin: auto;'>{pet_obj['name']}</h1>
    <img src='{pet_obj["url"]}' alt="pet_img" />
    <p>{pet_obj['description']}</p>
    <ul>
      <li>{pet_obj['breed']}</li>
      <li>{pet_obj['age']} Years old</li>
    </ul>
  """
    return html
