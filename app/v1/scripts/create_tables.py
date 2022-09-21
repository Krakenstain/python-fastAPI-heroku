import app.v1.utils.db as db


def create_tables():
    """
    Create tables in the database
    """
    with db.Session():
        db.Base.metadata.create_all(db.engine)
        print("Tables created")


create_tables()