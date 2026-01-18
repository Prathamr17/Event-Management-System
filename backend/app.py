from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import db, jwt

from routes.auth_routes import auth_bp
from routes.event_routes import event_bp
from routes.participant_routes import participant_bp
from routes.feedback_routes import feedback_bp
from routes.report_routes import report_bp
from routes.payment_routes import payment_bp

def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    
    CORS(
        app,
        resources={r"/api/*": {"origins": "http://localhost:5173"}},
        supports_credentials=True,
        allow_headers=["Content-Type", "Authorization"],
        methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    )
    # cors.init_app(app)

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(event_bp, url_prefix="/api/events")
    app.register_blueprint(participant_bp, url_prefix="/api/participants")
    app.register_blueprint(feedback_bp, url_prefix="/api/feedback")
    app.register_blueprint(report_bp, url_prefix="/api/reports")
    app.register_blueprint(payment_bp, url_prefix="/api/payments")

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    print("Hello, World!")
    app.run(debug=True)
