import media
import fresh_tomatoes

"""
declare favorite movies, with 4 args each:
title (movie's title)
storyline (year movie was released)
poster_image_url (url to poster image)
trailer_youtube_url (url to youtube trailer)
"""


speed = media.Movie(
    "Speed",
    "Rescue bus passengers being hostages.",
    "https://upload.wikimedia.org/wikipedia/en/4/45/Speed_movie_poster.jpg",
    "https://www.youtube.com/watch?v=aRmhneo5A48")

sound_of_music = media.Movie(
    "Sound of Music",
    "The Story of Maria and Von Trapp Family.",
    "https://upload.wikimedia.org/wikipedia/en/6/6b/Musical1959-SoundOfMusic-OriginalPoster.png",
    "https://youtu.be/lEcKXr3mJ_o")

brave_heart = media.Movie(
    "Brave Heart",
    "Scottish warrior who led the Scots in the First War of Scottish Independence against King Edward I of England.",
    "https://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg",
    "https://www.youtube.com/watch?v=nMft5QDOHek")

raiders_of_the_lost_ark = media.Movie(
    "Raiders of the Lost Ark",
    "Indiana Jones against a group of Nazis who are searching for the Ark of the Covenan.",
    "https://upload.wikimedia.org/wikipedia/en/4/4c/Raiders_of_the_Lost_Ark.jpg",
    "https://youtu.be/0ZOcoxjeUYo")

bambi = media.Movie(
    "Bambi",
    "Bambi join his new friends exploring the woods.",
    "https://upload.wikimedia.org/wikipedia/en/8/88/Walt_Disney%27s_Bambi_poster.jpg",
    "https://www.youtube.com/watch?v=nLvX-erABqY")

die_hard = media.Movie(
    "Die Hard",
    "The film follows off-duty New York City Police Department officer John McClane.",
    "https://upload.wikimedia.org/wikipedia/en/7/7e/Die_hard.jpg",
    "https://www.youtube.com/watch?v=eLu3z4Ikwes")


mov1=[speed, sound_of_music, brave_heart, raiders_of_the_lost_ark, bambi, die_hard]
fresh_tomatoes.open_movies_page(mov1)


