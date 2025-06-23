from server.app import create_app
from server.extensions import db
from server.models import User, Guest, Episode, Appearance
from datetime import date

app = create_app()

with app.app_context():
    print("Seeding database...")

    db.session.query(Appearance).delete()
    db.session.query(Guest).delete()
    db.session.query(Episode).delete()
    db.session.query(User).delete()

    user = User(username="admin")
    user.set_password("password123")

    g1 = Guest(name="Zendaya", occupation="Actress")
    g2 = Guest(name="Trevor Noah", occupation="Comedian")

    e1 = Episode(date=date(2025, 6, 20), number=1)
    e2 = Episode(date=date(2025, 6, 21), number=2)

    a1 = Appearance(rating=5, guest=g1, episode=e1)
    a2 = Appearance(rating=4, guest=g2, episode=e1)
    a3 = Appearance(rating=5, guest=g2, episode=e2)

    db.session.add_all([user, g1, g2, e1, e2, a1, a2, a3])
    db.session.commit()

    print("Seeding complete.")
