from flask import Flask, render_template
from flask_cors import CORS
from rearange import re_arranger


def create_app():
   
    app = Flask(
        __name__, 
        static_folder='static', 
        template_folder='templates'
    )

    CORS(app)

    @app.route('/validate')
    def serve_frontend():
        return render_template('index.html')
    
    app.register_blueprint(re_arranger)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
