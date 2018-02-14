from app import app
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)


#  model for articles table

class articles(UserMixin , db.Model) :

    __tablename__  =  'articles'
    id = db.Column(db.Integer)
    user_profiles_id = db.Column(db.Integer , db.ForeignKey('user_profiles.id') , nullable = False)
    article_title = db.Column(db.String , nullable = False)
    article_slug = db.Column(db.String , nullable = False)
    article_feature_image = db.Column(db.String , nullable = False)
    article_body = db.Column(db.String , nullable = False)
    created_at = db.Column(db.DateTime , nullable = False , primary_key = True)
    updated_at = db.Column(db.DateTime , nullable = False , primary_key = True)


# model for  table user_profiles

class user_profiles(db.Model , UserMixin):

    __tablename__ = 'user_profiles'
    id = db.Column(db.Integer)
    user_id = db.Column(db.Integer ,db.ForeignKey('users.id') , nullable = False)
    fullname = db.Column(db.String , primary_key = True , nullable =False)
    user_title = db.Column(db.Integer , primary_key = True , nullable = False)
    created_at = db.Column(db.DateTime ,  primary_key = True , nullable = False )
    updated_at = db.Column(db.DateTime , primary_key = True , nullable = False)


# model for users  table

class users(db.Model , UserMixin):

    __tablename__ = 'users'
    id = db. Column(db.Integer , nullable = False)
    email =  db.Column(db.String , primary_key = True , nullable = True )
    user_name = db.Column(db.String , primary_key = True , nullable = True)
    password = db.Column(db.String , primary_key = True , nullable = True)
    created_at = db.Column(db.String , primary_key = True , nullable = False)
    updated_at = db.Column(db.String , primary_key = True , nullable = False)


# model for  table categories

class categories(db.Model ,UserMixin ):

    __tablename__ = 'categories'
    id = db.Column(db.Integer , nullable = False)
    category_name = db.Column(db.Integer , nullable = True , primary_key = True)
    category_slug = db.Column(db.String , nullable = False , primary_key = True)
    created_at = db.Column(db.DateTime , nullable = False , primary_key = True)
    updated_at = db.Column(db.DateTime , nullable =False , primary_key = True)


# model for table category_to_articles

class category_to_articles(db.Model , UserMixin):

    __tablename__ = 'category_to_articles'
    id =  db.Column(db.Integer , nullable = False)
    category_name = db.Column(db.Integer , db.ForeignKey('categories.category_name'), nullable = True )
    article_id = db.Column(db.Integer , db.ForeignKey('articles.id') , nullable = True )
    created_at = db.Column(db.DateTime , nullable = False , primary_key = True)
    updated_at = db.Column(db.DateTime , nullable = False , primary_key = True )
