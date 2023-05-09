from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    moon_id = db.Column(db.Integer, db.ForeignKey('moon.id'))
    moons = db.relationship("Moon", back_populates="planets")


    @classmethod
    def from_dict(cls, planet_data):
        new_planet = Planet(
            name = planet_data["name"],
            description = planet_data["description"],
            moons = planet_data["moons"]
        )

        return new_planet

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "moons": self.moons
        }