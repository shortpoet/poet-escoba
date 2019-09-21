from flask import Flask, render_template, redirect, Markup, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import *
from sqlalchemy import orm
from sqlalchemy.engine import reflection
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

connection_string = "root:password@localhost/test"
engine = create_engine(f'mysql://{connection_string}')

app = Flask(__name__)

from bson import json_util
import json
import re
from datetime import datetime as dt

# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:password@localhost:3306/test"
# db = SQLAlchemy(app)

# Base = automap_base()
# reflect the tables
# Base.prepare(engine, reflect=True)

# Create our session (link) from Python to the DB
session = Session(engine)
metadata = MetaData()
metadata.reflect(engine)

# Base = automap_base(metadata=metadata)
# Base.prepare()

Base = declarative_base()
Base.metadata = metadata

db = create_engine('mysql://root:password@localhost:3306/test',echo=False)
metadata.reflect(bind=db)

deck_table = metadata.tables['Deck']
cards_table = metadata.tables['Cards']

sm = orm.sessionmaker(bind=db, autoflush=True, autocommit=True, expire_on_commit=True)
session = orm.scoped_session(sm)

q = session.query(deck_table,cards_table).join(cards_table)
for r in q.limit(10):
    print(r)\

q = session.query(deck_table,cards_table).join(deck_table)
for r in q.limit(10):
    print(r)

class Card(Base):
    __tablename__ = "Card"
    deck = relationship("Deck", backref = "DeckId")


class Deck(Base):
    __tablename__ = "Deck"

insp = reflection.Inspector.from_engine(db)
print(insp.get_table_names())
print(insp.get_foreign_keys(Cards.__tablename__))
print(insp.get_foreign_keys(Deck.__tablename__))


# Deck = Base.classes.Deck
# print(Base.classes)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String, unique=True, nullable=False)
#     email = db.Column(db.String, unique=True, nullable=False)

@app.route("/tablenames")
def tablenames():

    table_names = engine.table_names()

    # db.session.add(User(name="Flask", email="example@example.com"))
    # db.session.commit()

    # users = User.query.all()

    return jsonify(table_names)

@app.route("/deck")
def deck():

    deck = session.query(Deck).all()
    # columns = session.query(Deck.__table__.columns).all()
    # col_arr = [col for col in columns]
    columns = Deck.__table__.columns.keys()
    cards = []
    for card in deck:
        passenger_dict = {}
        # passenger_dict["name"] = passenger.name
        # passenger_dict["age"] = passenger.age
        # passenger_dict["sex"] = passenger.sex
        cards.append(card)
        print(card)

    return jsonify(columns)
    # return jsonify(all_passengers)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='5000', debug=True)