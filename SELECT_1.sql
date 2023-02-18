--1 Альбомы и год выпуска албовом 2018г.
SELECT album_name,year_of_release FROM albums
WHERE year_of_release = 2018;

--2 Самый продолжительный трек(в секундах), его название
SELECT track_name, duration_sec FROM audio_tracks 
WHERE duration_sec = (SELECT MAX(duration_sec) FROM audio_tracks);


--3 Трек с продолжительностью более 3.5 мин 
SELECT track_name  FROM audio_tracks
WHERE duration_sec > 210; 

--4 названия сборников, вышедших в период с 2018 по 2020 год включительно
SELECT name_collection , year_of_release FROM collection
WHERE year_of_release  BETWEEN 2018 AND 2020; 

--5 Исполнители, чье имя состоит из 1 слова
SELECT name_artist FROM artists
WHERE name_artist NOT LIKE '%% %%'; 

--6 название треков, которые содержат слово "мой"/"my" , 
--слово Vegas с возможным использованием в начале и конце слова Vegas символов.
SELECT track_name FROM audio_tracks
WHERE  track_name LIKE 'my';

SELECT track_name FROM audio_tracks
WHERE  track_name LIKE 'мой';

SELECT track_name FROM audio_tracks
WHERE  track_name LIKE '%Vegas%';