from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons

def validate_planet_id(planet_id):
    ### to generalize for planets and moons, could input id# and list and then do for item in list, return item
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"{planet_id} is not a valid type. Please use int."}, 400))
    for planet in planets:
        if planet.id == planet_id:
            return planet
    abort(make_response({"message": f"{planet_id} is not a valid planet. Please provide new ID."}, 404))

planets = [
    Planet(1, "Mercury", "Smallest planet, closest to the sun", 0),
    Planet(2, "Venus", "Hottest planet, second from the sun", 0),
    Planet(3, "Earth", "Habitable planet, third from the sun", 1),
    Planet(4, "Mars", "Red Planet, fourth from the sun", 2),
    Planet(5, "Jupiter", "Largest planet, fifth from the sun", 79),
    Planet(6, "Saturn", "Ringed planet, sixth from the sun", 82),
    Planet(7, "Uranus", "Tilted planet, seventh from the sun", 27),
    Planet(8, "Neptune", "Windy blue planet, eigth from the sun", 14),
    Planet(9, "Pluto", "Dwarf planet, ninth from the sun", 5)
]

planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planet_bp.route("", methods=["GET"])

def handle_planets():
    planet_response = []

    for planet in planets:
        planet_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "moons": planet.moons
        })

    return jsonify(planet_response)

@planet_bp.route("/<planet_id>", methods=["GET"])

def handle_single_planet(planet_id):
    planet = validate_planet_id(planet_id)
    return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "moons": planet.moons
        }

###As a client, I want to send a request...

# 1. ...to get one existing `planet`, so that I can see the `id`, `name`, `description`, and other data of the `planet`.
# 1. ... such that trying to get one non-existing `planet` responds with get a `404` response, so that I know the `planet` resource was not found.
# 1. ... such that trying to get one `planet` with an invalid `planet_id` responds with get a `400` response, so that I know the `planet_id` was invalid.
