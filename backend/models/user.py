from extensions import db
import bcrypt

class User(db.Model):
    __tablename__ = "users"   # ← REQUIRED, DO NOT SKIP

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(
            password.encode(), bcrypt.gensalt()
        ).decode()

    def check_password(self, password):
        return bcrypt.checkpw(
            password.encode(), self.password_hash.encode()
        )
