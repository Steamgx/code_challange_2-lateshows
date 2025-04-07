from app import app
from extensions import db
from models import Episode, Guest, Appearance

def seed_database():
    with app.app_context():
        print("Deleting all records...")
        Episode.query.delete()
        Guest.query.delete()
        Appearance.query.delete()

        print("Creating episodes...")
        e1 = Episode(date="1/11/99", number=1)
        e2 = Episode(date="2/22/00", number=2)
        e3 = Episode(date="3/33/01", number=3)

        print("Creating guests...")
        g1 = Guest(name="Michael J. Fox", occupation="Actor")
        g2 = Guest(name="Tom Hanks", occupation="Actor")
        g3 = Guest(name="Oprah Winfrey", occupation="TV Host")

        print("Creating appearances...")
        a1 = Appearance(rating=5, episode=e1, guest=g1)
        a2 = Appearance(rating=4, episode=e1, guest=g2)
        a3 = Appearance(rating=3, episode=e2, guest=g3)
        a4 = Appearance(rating=5, episode=e3, guest=g1)

        print("Adding to session...")
        db.session.add_all([e1, e2, e3, g1, g2, g3, a1, a2, a3, a4])

        print("Committing...")
        db.session.commit()
        print("Seeding complete!")

if __name__ == '__main__':
    seed_database()
