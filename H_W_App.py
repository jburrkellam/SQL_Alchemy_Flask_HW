
import numpy as np

import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect


from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///hawaii.sqlite?check_same_thread=False")

Base = automap_base()
Base.prepare(engine, reflect=True)

session = Session(engine)

Measurement = Base.classes.measurement
Station = Base.classes.station



#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"Welcome to the Surf's Up API!:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/station"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>" 
    )


@app.route("/api/v1.0/precipitation")  
def precipitation():

    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-08-23').all()
    prcp_data = list(np.ravel(results))

#    all_measurement = []
#     for measurement in results:
#         measurement_dict = {}
        #   measurement_dict["date"] = measurement.date
        #   measurement_dict["prcp"] = measurement.prcp
        #   all_measurement.append(measurement_dict)

    return jsonify(prcp_data)


@app.route("/api/v1.0/station")
def station():

    results = session.query(Station.station).all()
    station_data = list(np.ravel(results))
    return jsonify(station_data)

@app.route("/api/v1.0/tobs")
def observations():

    results = session.query(Measurement.tobs).all()
    temp_data = list(np.ravel(results))
    return jsonify(temp_data)





    
if __name__ == "__main__":
    app.run(debug=True)