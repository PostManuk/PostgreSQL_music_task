CREATE TABLE IF NOT EXISTS genre (
id Serial PRIMARY KEY,
genre_name VARCHAR (80) NOT NULL
);

CREATE TABLE IF NOT EXISTS artists (
id Serial PRIMARY KEY,
name_artist VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS albums (
id Serial PRIMARY KEY,
album_name VARCHAR(80) NOT NULL,
year_of_release INT CHECK (year_of_release >1933) NOT NULL
);

CREATE TABLE IF NOT EXISTS genre_artists(
id Serial PRIMARY KEY,
genre_id INTEGER NOT NULL REFERENCES genre(id),
artist_id INTEGER NOT NULL REFERENCES artists(id)
);

CREATE TABLE IF NOT EXISTS collection(
id Serial PRIMARY KEY,
year_of_release INTEGER NOT NULL,
Name_collection VARCHAR(80) NOT NULL
);

CREATE TABLE IF NOT EXISTS audio_tracks (
id Serial PRIMARY KEY,
track_name VARCHAR(80) NOT NULL,
duration_sec INTEGER NOT NULL,
album_id INTEGER NOT NULL REFERENCES albums(id)
);


CREATE TABLE IF NOT EXISTS album_artists (
id Serial PRIMARY KEY,
album_id INTEGER NOT NULL REFERENCES albums(id),
artist_id INTEGER NOT NULL REFERENCES artists(id)
);

CREATE TABLE IF NOT EXISTS collection_audiotrack (
id Serial PRIMARY KEY,
collection_id INTEGER NOT NULL REFERENCES collection(id),
audiotrack_id INTEGER NOT NULL REFERENCES audio_tracks (id)
);