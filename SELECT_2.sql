--1Количество исполнительней в каждом жанре
SELECT genre_name, COUNT (*) FROM genre
GROUP BY genre_name 
ORDER BY count (*)DESC; 

--2 Треки вошедшие в альбоы 2019 и 2020 годов соответсвенно.
SELECT track_name,year_of_release FROM audio_tracks a
left JOIN albums s ON  a.album_id = s.id
WHERE year_of_release = 2019 OR  year_of_release = 2020;

--3 Средняя продолжительность песен по названиям альбомов
SELECT album_name, avg(duration_sec) FROM  albums a
JOIN audio_tracks s on a.id =s.album_id
GROUP BY album_name;



--4 Исполнители,которые НЕ выпустили альбомы в 2020г
SELECT name_artist FROM artists a
JOIN album_artists b ON b.artist_id= a.id 
JOIN albums c on c.id = b.album_id
WHERE year_of_release != 2020
GROUP BY name_artist;



--5 названия сборников, в которых присутствует конкретный исполнитель
SELECT  name_collection, name_artist FROM collection a 
JOIN collection_audiotrack ca  ON a.id = ca.collection_id
JOIN audio_tracks at2 ON at2.id = ca.audiotrack_id
JOIN albums a2 ON a2.id = at2.album_id 
JOIN album_artists aa ON aa.album_id  = at2.album_id
JOIN artists a3 ON a3.id = aa.artist_id 
WHERE name_artist = 'Linkin Park';



-- 6 название альбомов, в которых присутствуют исполнители более 1 жанра
SELECT album_name  FROM albums a
JOIN album_artists aa ON a.id = aa.album_id 
JOIN artists a2 ON aa.id = a2.id
join genre_artists ga on a2.id = ga.artist_id 
GROUP BY album_name
HAVING count (ga.genre_id)>1;

-- 7 Названия треков,не входящих в сборники 
SELECT  track_name FROM collection a 
JOIN collection_audiotrack ca  ON a.id = ca.collection_id
RIGHT JOIN audio_tracks at2 ON at2.id = ca.audiotrack_id
WHERE name_collection IS NULL ;


-- 8 Имя исполнителя(ей), написавшего самый короткий по продолжительности трек (так же включил продолжительность трека )
SELECT  name_artist , duration_sec FROM artists a 
JOIN album_artists aa ON aa.album_id = a.id 
JOIN albums a2 ON a2.id = aa.id 
JOIN audio_tracks at2 ON at2.album_id = aa.id 
WHERE duration_sec = (SELECT MIN(duration_sec) FROM audio_tracks);



--В 9 пункте если ставить лимит на первую строку  по count ,
-- может получиться ситуация когда песен в альбом одинаковое кол-во(как у меня)


--9  название альбомов, содержащих наименьшее количество треков (с COUNT) по возрастанию
SELECT album_name, count(album_name) AS count_tracks  FROM  audio_tracks at2
LEFT JOIN albums a on a.id = at2.album_id
GROUP BY album_name
ORDER BY count(album_name);

--9 название альбомов, содержащих наименьшее количество треков с лимитом
SELECT album_name,count(album_name) AS count_tracks  FROM  audio_tracks at2
LEFT JOIN albums a on a.id = at2.album_id
GROUP BY album_name
ORDER BY count(album_name)
LIMIT 3;