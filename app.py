from flask import Flask, request
from flask_cors import CORS # Importing CORS TO BE USED LATER
from extensions import db, migrate
from models import Episode, Guest, Appearance

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

db.init_app(app)
migrate.init_app(app, db)
CORS(app)

@app.route('/')
def index():
    return {'message': 'Late Show API'}

@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return {'episodes': [episode.to_dict() for episode in episodes]}

@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return {'error': 'Episode not found'}, 404
    return episode.to_dict()

@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return {'guests': [guest.to_dict() for guest in guests]}

@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    try:
        appearance = Appearance(
            rating=data['rating'],
            episode_id=data['episode_id'],
            guest_id=data['guest_id']
        )
        appearance.validate_rating()
        db.session.add(appearance)
        db.session.commit()
        return appearance.to_dict(), 201
    except ValueError as e:
        return {'errors': [str(e)]}, 422
    except Exception as e:
        return {'errors': ['Invalid data']}, 422

if __name__ == '__main__':
    app.run(port=5555, debug=True)
