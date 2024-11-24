from flask_cors import CORS
from app import create_app, db
from app.sample_data import init_db

app = create_app()
CORS(app)

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        # Creating tables
        db.create_all()  
        # Initializing DB with sample data
        init_db()  
    app.run(debug=True, host='0.0.0.0')