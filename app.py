from flask import Flask
from flask_cors import CORS
from rearange import re_arranger


def create_app():
   
    app = Flask(__name__)

    CORS(app, resources={
        r"re_arrange/*": {
            "origins": "http://127.0.0.1:5500",
            "methods": ["GET", "POST"],
            "allow_headers": ["Content-Type"]
        }
    })
    
    app.register_blueprint(re_arranger)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
