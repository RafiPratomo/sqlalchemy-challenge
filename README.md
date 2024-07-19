# Climate App

This project is a Flask application that provides a set of API endpoints to access climate data from a SQLite database. The data is sourced from weather stations in Hawaii and includes information on precipitation, temperature observations, and more.

## Requirements

- Python 3.x
- Flask
- SQLAlchemy

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/RafiPratomo/sqlalchemy-challenge.git
    ```

2. Navigate to the project directory:
    ```sh
    cd sqlalchemy-challenge
    ```

3. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the required packages:
    ```sh
    pip install Flask SQLAlchemy
    ```

5. Make sure the SQLite database (`hawaii.sqlite`) is in the project directory.

## Running the Application

1. Run the Flask application:
    ```sh
    python app.py
    ```

2. Open a web browser and go to `http://127.0.0.1:5000/` to access the available routes.

## API Endpoints

- **/**: List all available API routes.

- **/api/v1.0/precipitation**: Return a JSON representation of precipitation data.

- **/api/v1.0/stations**: Return a JSON list of stations from the dataset.

- **/api/v1.0/tobs**: Return a JSON list of temperature observations (tobs) for the previous year.

- **/api/v1.0/<start>** and **/api/v1.0/<start>/<end>**: 
    - Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
    - For a specified start date, calculate TMIN, TAVG, TMAX for all the dates greater than or equal to the start date.
    - For a specified start date and end date, calculate TMIN, TAVG, TMAX for the dates from the start date to the end date, inclusive.

## Notes

- The database schema includes two tables: `measurement` and `station`.
- The application uses SQLAlchemy for ORM (Object Relational Mapping).
