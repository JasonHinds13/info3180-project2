from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

class WishListForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description = StringField('Description', validators=[InputRequired()])
    website = StringField('Website', validators=[InputRequired()])
    thumbnail = StringField('Thumbnail', validators=[InputRequired()])
