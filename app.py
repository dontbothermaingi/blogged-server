from models import db, Story
from flask import Flask,request, jsonify, make_response, send_from_directory
from flask_cors import CORS
import os
from flask_restful import Resource,Api
from werkzeug.utils import secure_filename
from flask_migrate import Migrate
from flask_restful import Resource, Api
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'sqlite:///blogg.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
api = Api(app)

db.init_app(app)

migrate =  Migrate(app, db)


# Configure secret keys
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'default_secret_key')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'default_jwt_secret_key')

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # max 16 mb
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Images')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_filename(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

class StoryResource(Resource):
    def get (self):

        stories = Story.query.all()

        return [story.to_dict() for story in stories]
    
    def post (self):
        
        data = request.form
        file = request.files.get('image')

        if not file or not allowed_filename(file.filename):
            return jsonify({'error': 'Product image is required and must be a valid file type'}), 400
        
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        if not data:
            return jsonify({'error': 'No data available for posting'})
        
        required_fields = ['title', 'subtitle', 'author', 'category', 'date']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
            
            title = data.get('title')
            subtitle = data.get('subtitle')
            contentparagraph1 = data.get('contentparagraph1')
            contentparagraph2 = data.get('contentparagraph2')
            contentparagraph3 = data.get('contentparagraph3')
            contentparagraph4 = data.get('contentparagraph4')
            contentparagraph5 = data.get('contentparagraph5')
            contentparagraph6 = data.get('contentparagraph6')
            contentparagraph7 = data.get('contentparagraph7')
            contentparagraph8 = data.get('contentparagraph8')
            contentparagraph9 = data.get('contentparagraph9')
            contentparagraph10 = data.get('contentparagraph10')
            author = data.get('author')

            # Convert date string to Python date object
            date_str = data.get('date')
            date = datetime.strptime(date_str, '%Y-%m-%d').date()

            date = data.get('date')
            category = data.get('category')

            new_story = Story (
                title=title,
                subtitle=subtitle,
                contentparagraph1=contentparagraph1,
                contentparagraph2=contentparagraph2,
                contentparagraph3=contentparagraph3,
                contentparagraph4=contentparagraph4,
                contentparagraph5=contentparagraph5,
                contentparagraph6=contentparagraph6,
                contentparagraph7=contentparagraph7,
                contentparagraph8=contentparagraph8,
                contentparagraph9=contentparagraph9,
                contentparagraph10=contentparagraph10,
                author=author,
                date=date,
                category=category
            )

            try:
                db.session.add(new_story)
                db.session.commit()
                return jsonify(new_story.to_dict()), 200
            except Exception as e:
                db.session.rollback()
                return jsonify({'error': f'Failed to create product: {str(e)}'}), 500
            
api.add_resource(StoryResource, '/stories', endpoint='story')

@app.route('/images/<filename>')
def upload_images(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename), 200

@app.route('/story/<int:id>', methods=['GET'])
def get_story_by_id(id):
    story = Story.query.filter_by(id=id).first()

    if not story:
        return jsonify({'error': 'Story does not exist'}), 404

    if request.method == 'GET':
        return jsonify(story.to_dict()), 200


if __name__ == '__main__':
    app.run(port=1904, debug=True)
