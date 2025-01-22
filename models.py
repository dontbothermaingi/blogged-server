from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Story(db.Model):
    __tablename__ = 'stories'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String)
    subtitle = db.Column(db.String)
    contentparagraph1 = db.Column(db.String)
    contentparagraph2 = db.Column(db.String)
    contentparagraph3 = db.Column(db.String)
    contentparagraph4 = db.Column(db.String)
    contentparagraph5 = db.Column(db.String)
    contentparagraph6 = db.Column(db.String)
    contentparagraph7 = db.Column(db.String)
    contentparagraph8 = db.Column(db.String)
    contentparagraph9 = db.Column(db.String)
    contentparagraph10 = db.Column(db.String)
    author = db.Column(db.String)
    date = db.Column(db.String)
    category = db.Column(db.String)
    image = db.Column(db.String)

    def to_dict(self):
        return{
            "id": self.id,
            "title": self.title,
            "subtitle": self.subtitle,
            "contentparagraph1": self.contentparagraph1,
            "contentparagraph2": self.contentparagraph2,
            "contentparagraph3": self.contentparagraph3,
            "contentparagraph4": self.contentparagraph4,
            "contentparagraph5": self.contentparagraph5,
            "contentparagraph6": self.contentparagraph6,
            "contentparagraph7": self.contentparagraph7,
            "contentparagraph8": self.contentparagraph8,
            "contentparagraph9": self.contentparagraph9,
            "contentparagraph10": self.contentparagraph10,
            "author": self.author,
            "date": self.date,
            "category": self.category,
            "images": f"/images/{self.image}"
        }
    
    def __repr__(self):
        return (f"<Story id={self.id}, author={self.author}, subtitle={self.subtitle}, title={self.title}, date={self.date}"
                f"category={self.category}>")
