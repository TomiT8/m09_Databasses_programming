from connect_db import session, db
from models_student import *
from sqlalchemy.exc import IntegrityError

Base.metadata.create_all(db)

try:
    session.add_all(
        [
            Address(street_name="Komenského", number=10, city="Košice", student=1),
            Address(street_name="Rastislavova", number=15, city="Košice", student=6),
            Address(street_name="Obrancov Mieru", number=2, city="Košice", student=3),
            Address(street_name="Stará Spišská cesta", number=33, city="Košice", student=4),
            Address(street_name="Kováčska", number=1, city="Košice", student=5),
        ]
    )

    # session.commit()

except IntegrityError as e:
    session.rollback()
    print(f"ERROR: {e}")


