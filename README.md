# Movie_Database-Data_Engineering

## Project Overview

This project is focused on building and managing a SQL database of the top 500 movies from 2019 to 2024, using a Python-based data engineering workflow. The project includes a user-friendly interface built with Flask, enabling users to interact with the movie database. It also features a data visualization component for displaying key insights about the movie data.

## Project Structure

* **ETL/data_enginerring.ipynb**: Involves the extraction, transformation, and loading (ETL) of movie data into a SQL database. The movie data is sourced from various APIs, cleaned, and stored in a relational database.
* **ETL/data_visuallization.ipynb**: A separate module handles the visualization of the movie data, providing insights such as top-rated movies, distribution of genres, and other key metrics.
* **ETL/app.py**: A simple web application built with Flask allows users to query the database and retrieve information about specific movies.
* **Outputs**: Contains data files and data visualizations
* **SQL**: Contains database files
* **README.md**: Overview of the project
* **LICENSE.txt**: License of the project

## Features

* **Data Extraction**: Fetches movie data from APIs for movies released between 2019 and 2024.
* **Data Cleaning and Transformation**: Cleans and structures the data for insertion into a SQL database.
* **Database Integration**: Stores movie data in a SQL database for efficient querying.
* **Data Visualization**: Provides various visualizations such as movie ratings distribution and top-performing movies.
* **Flask Web Interface**: Users can interact with the database through a simple web interface.

## Technologies Used

* **Python**: Core programming language used throughout the project.
* **Flask**: Web framework for building the user interface.
* **SQL**: Relational database management system for storing and querying movie data.
* **Jupyter Notebooks**: Used for data engineering and data visualization.
* **Pandas**: For data manipulation and cleaning.
* **Matplotlib / Seaborn**: For generating visualizations.
* **APIs**: Movie data is fetched using external APIs.

## Setup Instructions

### Prerequisites

* Python 3.x
* Flask
* SQL (MySQL, PostgreSQL, or SQLite)
* Jupyter Notebook
* Libraries: pandas, matplotlib, seaborn, SQLAlchemy, Flask, requests

### Installation

1. Clone the repository:

```python
git clone https://github.com/alvin-giang/Movie_SQL_Database_Data_Engineering.git
```

2. Install required Python libraries:

```python
pip install -r requirements.txt
```

3. Set up the SQL database:

* Ensure your SQL server is running.
* Create a database for storing movie data.
* Update the database connection string in app.py.

4. Run the Flask app:

```python
python app.py
```

5. Open your browser and go to `http://127.0.0.1:5000` to access the web interface.

## Usage

* **Data Engineering**: The Jupyter notebook (data_engineering.ipynb) handles the ETL process. It can be executed step-by-step to load the data into the SQL database.
* **Data Visualization**: The data_visualization.ipynb notebook provides various plots and charts for visualizing the movie data.
* **Flask App**: The web application provides an interface for querying the movie database. You can search for movies by title, genre, or release date.

## Contributors

* **Thanh Vinh Giang (Alvin)** : Project Lead and Developer
* **Tammy Powell**: Contributor
* **Hao Nguyen (Frank)**: Contributor
* **Uthpalie THilakaratna-Attygalle**: Contributor

## License

This project is licensed under the MIT License.