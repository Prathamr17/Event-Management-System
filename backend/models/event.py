from extensions import db

class Event(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String(120), nullable=False)
    date = db.Column(db.Date, nullable=False)

    created_by = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    created_at = db.Column(db.DateTime, server_default=db.func.now())

    user = db.relationship("User", backref="events")
