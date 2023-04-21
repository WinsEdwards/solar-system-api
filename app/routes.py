from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons

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

