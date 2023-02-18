--ЖАНРЫ
INSERT INTO  genre(Genre_name)
VALUES 
	('Hip Hop'),
	('pop rock'),
	('pop music'),
	('smooth jazz'),
	('rhythm and blues'),
	('alternative rock');

--АРТИСТЫ
INSERT INTO artists (Name_Artist)
VALUES
	('Макс Корж'),
	('Drake'),
	('Rick ross'),
	('Imagine Dragons'),
	('SADE'),
	('Barry White'),
	('Sting'),
	('Linkin Park');

--АЛЬБОМЫ
INSERT INTO albums (album_name,year_of_release)
VALUES
	('Психи попадают в топ', '2021' ),
	('Scorpion', '2018' ),
	('Port of Miami 2 ', '2019' ),
	('Origins', '2018' ),
	('Diamond Life', '1984' ),
	('Staying Power', '1999' ),
	('Brand New Day ', '1999' ),
	(' Meteora', '2003');


-- СБОРНИКИ

INSERT INTO collection (year_of_release, name_collection)
VALUES
	--Корж(17 лет)
	('2021','Топ 100 хип хоп композиций'),
	--Imagine Dragons(Natural)
	('2019','US Hot Rock Songs'),
	('2019','Ultratop Flanders'),
	--Sting(Deset Rose)
	('1999', 'Billboard 200'),
	--Linkin Park Numb
	('2003', 'U.S. Billboard Hot 100'),
	('2003', 'U.S. Mainstream Rock Tracks'),
	('2003', 'Japanese Singles Chart'),
	--Barry White
	('1999', 'US Top R&B/Hip-Hop Albums ');





-- ТРЕКИ

INSERT INTO audio_tracks (track_name, duration_sec, album_id)
VALUES
	--Макс Корж
	('Снадобье',' 202', '1' ),
	('Карманы',' 312', '1' ),
	('17 лет',' 336', '1' ),
	--Imagine dragons
	('Natural','189', '4' ),
	('Machine','181', '4' ),
	--Rick Ross
	('Vegas Residency','319', '3' ),
	('Maybach Music VI','242', '3' ),
	--Drake
	('Survival','136', '2' ),
	('Nonstop	','238', '2' ),
	('Elevate','184', '2' ),
	--SADE
        ('Smooth opetaror', '322','5'),
	--Barry White
	('Don`t Play Games' , '444','6'),
	--Sting
	('Desert Rose','285', '7' ),
	-- Linlin Park 
	('Numb','188', '8' ),
	('Nobody`s Listening' , '179','8' ),
	('Session','143', '8' ),
	('Faint','162', '8' );



--artists_genre
INSERT INTO  genre_artists (genre_id,artist_id)
VALUES
	('1','1'),
	('1','2'),
	('1','3'),
	('2','4'),
	('6','4'),
	('3','7'),
	('4','5'),
	('5','6'),
	('6','8');


--album_artists
INSERT INTO  album_artists (album_id ,artist_id)
VALUES
	('1','1'),
	('2','2'),
	('3','3'),
	('4','4'),
	('5','5'),
	('6','6'),
	('7','7'),
	('8','8');


--collection_tracks_id
INSERT INTO collection_audiotrack  (collection_id ,audiotrack_id )
VALUES
	('1', '3'),
	('2', '4'),
	('2', '5'),
	('3', '4'),
	('4', '13'),
	('5', '14'),
	('6', '17'),
	('7', '17'),
	('8', '12');