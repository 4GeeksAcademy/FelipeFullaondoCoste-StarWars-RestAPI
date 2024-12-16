from .. import db

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id =
    people_id =
    planets_id =

    def __repr__(self):
        return f'<Favorites {self.id}>'
    
    def serialize(self):
        return {
            "id": self.id
        }