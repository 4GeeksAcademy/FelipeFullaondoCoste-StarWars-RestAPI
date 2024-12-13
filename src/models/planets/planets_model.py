from .. import db


class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(900), nullable=False)
    density = db.Column(db.String(60), nullable=False)
    
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.name
    
#metodods de instacia
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "density": self.density
        }