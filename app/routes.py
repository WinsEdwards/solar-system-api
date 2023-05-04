from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet
# from app.models.moon import Moon

# class Planet:
#     def __init__(self, id, name, description, moons):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.moons = moons

def validate_planet_id(planet_id):
    ### to generalize for planets and moons, could input id# and list and then do for item in list, return item
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"{planet_id} is not a valid type. Please use int."}, 400))
    
    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message": f"{planet_id} is not a valid planet. Please provide new ID."}, 404))
    
    return planet

# planets = [
#     Planet(1, "Mercury", "Smallest planet, closest to the sun", 0),
#     Planet(2, "Venus", "Hottest planet, second from the sun", 0),
#     Planet(3, "Earth", "Habitable planet, third from the sun", 1),
#     Planet(4, "Mars", "Red Planet, fourth from the sun", 2),
#     Planet(5, "Jupiter", "Largest planet, fifth from the sun", 79),
#     Planet(6, "Saturn", "Ringed planet, sixth from the sun", 82),
#     Planet(7, "Uranus", "Tilted planet, seventh from the sun", 27),
#     Planet(8, "Neptune", "Windy blue planet, eigth from the sun", 14),
#     Planet(9, "Pluto", "Dwarf planet, ninth from the sun", 5)
# ]

planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

# @planet_bp.route("", methods=["GET"])

# def handle_planets():
#     planet_response = []

#     for planet in planets:
#         planet_response.append({
#             "id": planet.id,
#             "name": planet.name,
#             "description": planet.description,
#             "moons": planet.moons
#         })

#     return jsonify(planet_response)

# @planet_bp.route("/<planet_id>", methods=["GET"])

# def handle_single_planet(planet_id):
#     planet = validate_planet_id(planet_id)
#     return {
#             "id": planet.id,
#             "name": planet.name,
#             "description": planet.description,
#             "moons": planet.moons
#         }

@planet_bp.route("", methods=['POST'])

def add_planets():
    request_body = request.get_json()

    print(request_body)
    # determine request_body type, then proceed based on that
    planet_list = []

    if isinstance(request_body, list):
        
        for single_planet in request_body:
            new_planet = Planet(
            name = single_planet["name"],
            description = single_planet["description"],
            moons = single_planet["moons"]
            )

            planet_list.append(new_planet)

    else:
        new_planet = Planet(
            name = request_body["name"],
            description = request_body["description"],
            moons = request_body["moons"]
        )

        planet_list.append(new_planet)
    
    db.session.add_all(planet_list)
    db.session.commit()

    return f"Planet(s) successfully created!", 201

#define a route for getting all planets
@planet_bp.route("", methods=["GET"])

def read_all_planets():
    planets_reponse = []
    planets = Planet.query.all()

    for planet in planets:
        planets_reponse.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "moons":planet.moons
        })

    return jsonify(planets_reponse)

#define a route for getting all planets
@planet_bp.route("/<planet_id>", methods=["GET"])

def read_one_planet(planet_id):
    planet = validate_planet_id(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "moons":planet.moons
        }, 200

@planet_bp.route("/<planet_id>", methods=["PUT"])

def update_planet(planet_id):
    planet = validate_planet_id(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.moons = request_body["moons"]

    db.session.commit()

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "moons":planet.moons
        }, 200

@planet_bp.route("/<planet_id>", methods=["DELETE"])

def delete_planet(planet_id):
    planet = validate_planet_id(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet_id} has been successfully deleted", 200)

### creating new blueprint for moon model

# moon_bp = Blueprint("moons", __name__, url_prefix="/moons")

#  @moon_bp.route("", methods=['POST'])

# @planet_bp.route("/<planet_id>/moons", methods=["POST"])


# def add_moon(planet_id):
#     request_body = request.get_json()
#     planet = validate_planet_id(planet_id)

#     new_moon = Moon(
#         name = request_body["name"],
#         radius = request_body["radius"],
#         planet = planet
#     )

#     db.session.add(new_moon)
#     db.session.commit()

#     return make_response(f"Moon {new_moon.name} successfully created!", 201)
