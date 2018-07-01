# import necessary libraries
import json
from flask import (
    Flask,
    render_template,
    jsonify,
    request)

from flask_sqlalchemy import SQLAlchemy

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

# The database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///DataSets/belly_button_diversity.sqlite"

db = SQLAlchemy(app)

class Button(db.Model):
    __tablename__ = 'button'
    SAMPLEID = db.Column(db.Integer, primary_key = True)
    EVENT = db.Column(db.String)
    ETHNICITY = db.Column(db.String)
    GENDER = db.Column(db.String)
    AGE = db.Column(db.Integer)
    WFREQ = db.Column(db.Integer)
    BBTYPE = db.Column(db.String)
    LOCATION = db.Column(db.String)
    COUNTRY012 = db.Column(db.String)
    ZIP012 = db.Column(db.Integer)
    COUNTRY1319 = db.Column(db.String)
    ZIP1319 = db.Column(db.Integer)
    DOG = db.Column(db.String)
    CAT = db.Column(db.String)
    IMPSURFACE013 = db.Column(db.Integer)
    NPP013 = db.Column(db.Float)
    MMAXTEMP013 = db.Column(db.Float)
    PFC013 = db.Column(db.Float)
    IMPSURFACE1319 = db.Column(db.Integer)
    NPP1319 = db.Column(db.Float)
    MMAXTEMP1319 = db.Column(db.Float)
    PFC1319 = db.Column(db.Float)

@app.route("/")
    """Return the dashboard homepage."""
    def home():
        return render_template("index.html")

@app.route('/names')
    """List of sample names."""
    def sample_names():
        query_statement = db.session.query(Button.SAMPLEID).all()
        df = pd.DataFrame(query_statement, columns = ['name', 'id'])
        return jsonify(df)

@app.route('/otu')
    """List of OTU descriptions."""
    def descriptions():
        query_statement = db.session.query(Button.)