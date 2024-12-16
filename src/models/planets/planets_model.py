from .. import db

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(900), nullable=False)
    population = db.Column(db.String(60), nullable=False)
    climate = db.Column(db.String(60), nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    # favorites = db.relationship('Favorites', back_populates='Planets')

    def __repr__(self):
        return f'<Planets {self.name}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "population": self.population,
            "climate" : self.climate
        }