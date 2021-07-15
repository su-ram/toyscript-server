from db.init_db import db


class Place(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))
    name = db.Column(db.String(50))
    frequency = db.Column(db.Integer)


class Character(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id", onupdate="cascade"))
    name = db.Column(db.String(50))
    lines = db.Column(db.Integer)


class Movie(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200))
    author = db.Column(db.String(100))
    total_characters = db.Column(db.Integer)
    total_pages = db.Column(db.Integer)
    total_places = db.Column(db.Integer)
    total_scenes = db.Column(db.Integer)


class Scene(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    num = db.Column(db.Integer, unique=False)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))
    place_id = db.Column(db.Integer, db.ForeignKey("place.id"))
    place = db.relationship("Place")
    time_id = db.Column(db.Integer, db.ForeignKey("time.id"))
    time = db.relationship("Time")


class Line(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    character_id = db.Column(
        db.Integer,
        db.ForeignKey("character.id", onupdate="cascade", ondelete="no action"),
    )
    character = db.relationship("Character")
    line = db.Column(db.Text)


class Time(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))
    frequency = db.Column(db.Integer)


class TimeCharacter(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))
    time_id = db.Column(db.Integer, db.ForeignKey("time.id"))
    time = db.relationship("Time")
    character_id = db.Column(db.Integer, db.ForeignKey("character.id"))
    character = db.relationship("Character")
    frequency = db.Column(db.Integer)


class PlaceCharacter(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    place_id = db.Column(db.Integer, db.ForeignKey("place.id"))
    place = db.relationship("Place")
    character_id = db.Column(db.Integer, db.ForeignKey("character.id"))
    character = db.relationship("Character")
    frequency = db.Column(db.Integer)


class Sentiment(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    character_id = db.Column(db.Integer, db.ForeignKey("character.id"))
    character = db.relationship("Character")
    anger = db.Column(db.Integer)
    anticipation = db.Column(db.Integer)
    disgust = db.Column(db.Integer)
    fear = db.Column(db.Integer)
    joy = db.Column(db.Integer)
    sadness = db.Column(db.Integer)
    surprise = db.Column(db.Integer)
    trust = db.Column(db.Integer)

    def __init__(self, sentiments: tuple, character_id: int) -> None:
        self.character_id = character_id
        self.anger = sentiments[0]
        self.anticipation = sentiments[1]
        self.disgust = sentiments[2]
        self.fear = sentiments[3]
        self.joy = sentiments[4]
        self.sadness = sentiments[5]
        self.surprise = sentiments[6]
        self.trust = sentiments[7]

    @staticmethod
    def get_sentiment_name():
        return [
            "anger",
            "anticipation",
            "disgust",
            "fear",
            "joy",
            "sadness",
            "surprise",
            "trust",
        ]

    def get_sentiments(self):
        return [
            self.anger,
            self.anticipation,
            self.disgust,
            self.fear,
            self.joy,
            self.sadness,
            self.surprise,
            self.trust,
        ]


class Relation(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))
    charac_one_id = db.Column(db.Integer, db.ForeignKey("character.id"))
    charac_two_id = db.Column(db.Integer, db.ForeignKey("character.id"))
    character_one = db.relationship("Character", foreign_keys=[charac_one_id])
    character_two = db.relationship("Character", foreign_keys=[charac_two_id])
    value = db.Column(db.Integer)
    test = db.Column(db.BOOLEAN)
    test3 = db.Column(db.BOOLEAN)


class WordCloud(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    character_id = db.Column(db.Integer, db.ForeignKey("character.id"))
    character = db.relationship("Character")
    word = db.Column(db.Text)
    frequency = db.Column(db.Integer)
