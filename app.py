# Import the dependencies.
from flask import Flask, jsonify, request
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
import datetime as dt


#################################################
# Database Setup
#################################################

# Create engine using the `hawaii.sqlite` database file
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# Declare a Base using `automap_base()`
Base = automap_base()
# Use the Base class to reflect the database tables
Base.prepare(engine, reflect=True)

# Assign the measurement class to a variable called `Measurement` and
# the station class to a variable called `Station`
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route('/')
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"  # Escape < and > to display correctly
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;" 
    )

@app.route('/api/v1.0/precipitation')
def precipitation():
    """Return a JSON representation of precipitation data."""
    results = session.query(Measurement.date, Measurement.prcp).all()
    precip_data = {date: prcp for date, prcp in results}
    return jsonify(precip_data)

@app.route('/api/v1.0/stations')
def stations():
    """Return a JSON list of stations from the dataset."""
    results = session.query(Station.station).all()
    stations_list = [result[0] for result in results]
    return jsonify(stations_list)

@app.route('/api/v1.0/tobs')
def tobs():
    """Return a JSON list of Temperature Observations (tobs) for the previous year."""
    most_active_station = session.query(Measurement.station, func.count(Measurement.station)).\
                          group_by(Measurement.station).\
                          order_by(func.count(Measurement.station).desc()).first()[0]
    
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    results = session.query(Measurement.date, Measurement.tobs).\
              filter(Measurement.station == most_active_station).\
              filter(Measurement.date >= one_year_ago).all()
    
    tobs_data = {date: tobs for date, tobs in results}
    return jsonify(tobs_data)

@app.route('/api/v1.0/<start>')
@app.route('/api/v1.0/<start>/<end>')
def temperature_range(start, end=None):
    """Return a JSON list of the minimum, average, and maximum temperature for a specified date range."""
    if not end:
        end = session.query(func.max(Measurement.date)).first()[0]
    
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
              filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    
    temp_stats = {
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2]
    }
    
    return jsonify(temp_stats)

if __name__ == '__main__':
    app.run(debug=True)