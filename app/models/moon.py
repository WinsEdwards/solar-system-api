from app import db
from app.models.planet import Planet

class Moon(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    radius = db.Column(db.BigInteger)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=False)
    planet = db.relationship("Planet", back_populates="moons")