from connect_db import session, db
from models_student import *
from sqlalchemy.exc import IntegrityError

Base.metadata.create_all(db)

try:
    session.add_all(
        [
            Locker(number=1, student=1),
            Locker(number=6, student=6),
            Locker(number=3, student=3),
            Locker(number=4, student=4),
            Locker(number=5, student=5)
        ]
    )

    session.commit()

except IntegrityError as e:
    session.rollback()
    print(f"ERROR: {e}")

