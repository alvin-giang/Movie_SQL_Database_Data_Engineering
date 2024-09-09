CREATE TABLE language (
	Language_Id VARCHAR (30) PRIMARY KEY NOT NULL,
	Language VARCHAR (30) NOT NULL
);

CREATE TABLE genre (
	Genre_Id INTEGER PRIMARY KEY NOT NULL,
	Genres VARCHAR (30) NOT NULL
);

CREATE TABLE movie (
	Movie_Id INTEGER PRIMARY KEY NOT NULL,
	Original_Title VARCHAR (255) NOT NULL,
	Title VARCHAR (255) NOT NULL,
	Language_Id VARCHAR (30) NOT NULL,
	FOREIGN KEY (Language_Id) REFERENCES language(Language_Id),
	Overview VARCHAR (8000) NOT NULL,
	Release_Date DATE NOT NULL,
	Popularity FLOAT NOT NULL,
	Vote_Average FLOAT NOT NULL,
	Vote_Count INTEGER NOT NULL
);

CREATE TABLE movie_genre (
	Movie_Id INTEGER NOT NULL REFERENCES movie(Movie_Id),
	Genre_Id INTEGER NOT NULL REFERENCES genre(Genre_Id),
	PRIMARY KEY (Movie_Id, Genre_Id)
);

SELECT * FROM movie_genre