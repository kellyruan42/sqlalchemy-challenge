#####################################################
# Import all needed
#####################################################
import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import flask
from flask import Flask , jsonify

#####################################################
# Create connection
#####################################################
# Create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

####################################################
# Flask Setup
####################################################
app = Flask(__name__)

####################################################
# Flask Routes
####################################################
@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    precipitation_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-08-23').order_by(Measurement.date).all()
    results = {date : x for date , x in precipitation_data}
    return jsonify(results)


@app.route("/api/v1.0/stations")
def station():
    station_data = session.query(Station.station).all()
    station_list = list(np.ravel(station_data))
    return jsonify (station_list)


@app.route("/api/v1.0/tobs")
def tobs():
    tobs_data = session.query(Measurement.tobs).\
            filter(Measurement.station == 'USC00519281' ).\
            filter(Measurement.date >= '2017,8,23').all()
    tobs_list = list(np.ravel(tobs_data))
    return jsonify (tobs_list)


@app.route ("/api/v1.0/<start>")
def start_date(start):
    start_date_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    results = list(np.ravel(start_date_data))
    min = results[0]
    avgerage = results[1]
    max_num = results[2]
    return jsonify({"Minimum Temperature": min, "Average Temperature": avgerage, "Maximum Temperature": max_num})


@app.route ("/api/v1.0/<start>/<end>")
def startend_date(start, end):
    start_end_date_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    new_result = list(np.ravel(start_end_date_data))
    min = new_result[0]
    avgerage = new_result[1]
    max_num = new_result[2]
    return jsonify({"Minimum Temperature": min, "Average Temperature": avgerage, "Maximum Temperature": max_num})
            

if __name__ == "__main__":
   app.run(debug=True)




