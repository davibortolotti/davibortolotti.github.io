# importing files and modules to be used in the code
import media
import fresh_tomatoes
import webbrowser


movies = []     # empty list

# CREATING INSTANCES - (title, synopsis, movie poster url, trailer url)
dreams = media.Movie(
    # title
    "Dreams",
    # synopsis
    """A collection of tales based upon the actual dreams of director
    Akira Kurosawa.""",
    # poster img link
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNDBkODdjMzEtNTY1NC0"+
    "0ZWQ5LTk3NDUtY2IwMTk5MzhmNTUwXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_.jpg",
    # youtube link
    "https://www.youtube.com/watch?v=bPHsu5NaVfM")
movies.append(dreams)   # appends to the list

intothewild = media.Movie(
    # title
    "Into the Wild",
    # synopsis
    """A tale about a boy that decides he wants live a fuller life by going to
    Alaska in order to live in nature""",
    # poster img link
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTAwNDEyODU1MjheQTJ"+
    "eQWpwZ15BbWU2MDc3NDQwNw@@._V1_.jpg",
    # youtube link
    "https://www.youtube.com/watch?v=g7ArZ7VD-QQ")
movies.append(intothewild)   # appends to the list

gits = media.Movie(
    # title
    "Ghost in the Shell",
    # synopsis
    """A cyborg policewoman and her partner hunt a mysterious and powerful
    hacker called the Puppet Master.""",
    # poster img link
    "https://images-na.ssl-images-amazon.com/images/M/MV5BM2FhYzVkMzQtOTVlYS0"+
    "0NTYxLThjNzktMDVhNjU1MDE0ZTc5L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@"+
    "@._V1_SY1000_CR0,0,701,1000_AL_.jpg",
    # youtube link
    "https://www.youtube.com/watch?v=p2MEaROKjaE")
movies.append(gits)   # appends to the list

thelastsamurai = media.Movie(
    # title
    "The Last Samurai",
    # synopsis
    """An american capitain from the civil war is invited to train the
    Japanese army against a rebel uprising, but soon falls for the
    samurai ways of living.""",
    # poster img link
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMzkyNzQ1Mzc0NV5BMl5"+
    "BanBnXkFtZTcwODg3MzUzMw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
    # youtube link
    "https://www.youtube.com/watch?v=T50_qHEOahQ")
movies.append(thelastsamurai)

prestige = media.Movie(
    # title
    "The Prestige",
    # synopsis
    """After a tragic accident two stage magicians engage in a battle to
    create the ultimate illusion whilst sacrificing everything they have
    to outwit the other..""",
    # poster img link
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4NDI0MTIxNF5BMl5"+
    "BanBnXkFtZTYwNTM0MzY2._V1_.jpg",
    # youtube link
    "https://www.youtube.com/watch?v=ijXruSzfGEc")
movies.append(prestige)   # appends to the list

shining = media.Movie(
    # title
    "The Shining",
    # synopsis
    """A family heads to an isolated hotel for the winter where an evil and
    spiritual presence influences the father into violence, while his psychic
    son sees horrific forebodings from the past and of the future.""",
    # poster img link
    "https://images-na.ssl-images-amazon.com/images/M/MV5BZWFlYmY2MGEtZjVkYS0"+
    "0YzU4LTg0YjQtYzY1ZGE3NTA5NGQxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
    # youtube link
    "https://www.youtube.com/watch?v=HEew7zvpAWE")
movies.append(shining)   # appends to the list

spirited = media.Movie(
    # title
    "Spirited Away",
    # synopsis
    """During her family's move to the suburbs, a sullen 10-year-old girl
    wanders into a world ruled by gods, witches, and spirits, and where
    humans are changed into beasts.""",
    # poster img link
    "https://images-na.ssl-images-amazon.com/images/M/MV5BOGJjNzZmMmUtMjljNC0"+
    "0ZjU5LWJiODQtZmEzZTU0MjBlNzgxL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SY"+
    "1000_CR0,0,675,1000_AL_.jpg",
    # youtube link
    "https://www.youtube.com/watch?v=ByXuk9QqQkk")
movies.append(spirited)   # appends to the list

tenthings = media.Movie(
    # title
    "Ten things I hate about you",
    # synopsis
    """A pretty, popular teenager can't go out on a date until her ill-tempered
    sister does""",
    # poster img link
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMmVhZjhlZDYtMDAwZi0"+
    "0MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
    # youtube link
    "https://www.youtube.com/watch?v=uE7qjQlfoRs")
movies.append(tenthings)   # appends to the list

wakinglife = media.Movie(
    # title
    "Waking Life",
    # synopsis
    """A man shuffles through a dream meeting various people and discussing
    the meanings and purposes of the universe.""",
    # poster img link
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMWM0ZjY5ZjctODNkZi0"+
    "0Nzk0LWE1ODUtNGM4ZDUyMzUwMGYwXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
    # youtube link
    "https://www.youtube.com/watch?v=SbPgprcMtjo")
movies.append(wakinglife)   # appends to the list

# running the function that creates the .html
fresh_tomatoes.open_movies_page(movies)
