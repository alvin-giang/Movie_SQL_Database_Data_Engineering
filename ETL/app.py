from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import datetime as dt

# Database Setup
engine = create_engine("sqlite:///movies.sqlite")
Base = automap_base()
Base.prepare(autoload_with=engine)

# Save references to each table
Language = Base.classes.language
Movie = Base.classes.movie
Genre = Base.classes.genre
# Movie_genre = Base.classes.movie_genre


# Flask Setup
app = Flask(__name__)



@app.route("/")
def welcome():
    """List all available api routes."""
    session = Session(engine)
    session.close()

    return (
        f"""
        <html>
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title> Top 500 Movie API Explorer</title>
                <style> 
                    body {{
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        background-color: #f4f4f4;
                    }}

                    header {{
                        background-color: #333;
                        color: white;
                        padding: 10px 0;
                        text-align: center;
                    }}

                    header h1 {{
                        margin: 0;
                    }}

                    main {{
                        padding: 20px;
                    }}

                    li {{
                        margin-bottom: 20px;
                    }}
                    section {{
                        margin-bottom: 40px;
                    }}

                    h2 {{
                        color: #333;
                    }}
                    img {{
                        max-width: 30%;
                        border-radius: 8px;
                    }}

                    footer {{
                        background-color: #333;
                        color: white;
                        text-align: center;
                        padding: 10px 0;
                    }}
                </style>
            </head>
            <body>
                <header>
                    <h1>Top 500 Movie API Explorer</h1>
                    <p>Group 4 - Project 3 - UWA Bootcamp - EdX</p>
                </header>
            <main>
                <section id="home">
                    <h2>Welcome to Top 500 Movie API Explorer</h2>
                    <p>Discover top 500 movies from the last 5 years using our API integration!</p>
                    <p>Our selection includes movies ranked by vote average, ensuring only the best movies with more than 1000 votes make it to our list.</p>
                </section>
                <section id="route">
                    <h2>Explore our awesome routes</h2>
                    <div id="movies-container">
                        <ul>
                            <li class="class1"><a href="/api/v1.0/movies">/api/v1.0/movies</a> - Top 500 movies</li>
                            <li class="class1"><a href="/api/v1.0/overview/movie-name/">/api/v1.0/overview/movie-name/</a> - Movie's overview - Enter the name of the movie</li>
                            <li class="class1"><a href="/api/v1.0/top-10-movies/year/">/api/v1.0/top-10-movies/year/</a> - Top 10 movies of each year - Enter the year</li>
                            <li class="class1"><a href="/api/v1.0/ABC">/api/v1.0/ABC</a> - ABC</li>
                            <li class="class1"><a href="/api/v1.0/ABC">/api/v1.0/ABC</a> - ABC</li>
                        </ul>
                    </div>
                </section>
                <hr>
                <div class="container">
                    <div class="image">
                        <img src="https://www.vanas.ca/images/blog/vfx-visual-effects-vanas.jpg"/>
                    </div>
                </div>
                <hr>
            </main>
            <footer>
                <p>&copy; Top 500 Movie API Explorer - UWA Bootcamp - Group 4. All rights reserved.</p>
            </footer>
        </html>
        """
    )

@app.route("/api/v1.0/movies")
def movies():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all movies
    results = session.query(Movie.movie_id, Movie.title, Movie.release_date, Movie.popularity, Movie.vote_average, Movie.vote_count).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_movies
    all_movies = []
    for movie_id, title, release_date, popularity, vote_average, vote_count in results:
        movie_dict = {}
        movie_dict["Movie_Id"] = movie_id
        movie_dict["Title"] = title
        movie_dict["Release_Date"] = release_date
        movie_dict["popularity"] = popularity
        movie_dict["Vote_Average"] = vote_average
        movie_dict["Vote_Count"] = vote_count
        all_movies.append(movie_dict)

    return jsonify(all_movies)

@app.route("/api/v1.0/overview/movie-name/<movie_name>")
def movie_overview(movie_name):
     # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all movies

    canonicalised = movie_name.replace(" ", "").lower()

    results = session.query(Movie.movie_id, Movie.title, Movie.overview).all()

    session.close()
    for movie_id, title, overview in results:
        search_term = title.replace(" ", "").lower()
        if search_term == canonicalised:
            movie = {"Movie_id": movie_id,
                     "Movie_title": title,
                     "Movie_overview": overview}
            return jsonify(movie)
    
    else:
        return jsonify({"error": f"Movie name: {movie_name} not found."}), 404

@app.route("/api/v1.0/top-10-movies/year/<year>")
def top_10_movie(year):
     # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all movies
    start_date = f"{year}-01-01"
    end_date = f"{year}-31-12"

    results = session.query(Movie.movie_id, Movie.title, Movie.vote_average, Movie.release_date).filter(Movie.release_date >= start_date).filter(Movie.release_date <= end_date).order_by(Movie.vote_average.desc()).limit(10).all()

    session.close()
    top_10_movie = []
    for movie_id, title, vote_average, release_date in results:
        movie_dict = {}
        movie_dict["Movie_Id"] = movie_id
        movie_dict["Title"] = title
        movie_dict["Release_Date"] = release_date
        movie_dict["Vote_Average"] = vote_average
        top_10_movie.append(movie_dict)

    return jsonify(top_10_movie)

if __name__ == "__main__":
    app.run(debug=True)