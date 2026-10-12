import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


#Этап 1
def average_rating(movies):
    if not movies:
        raise ValueError("Нельзя вычислить средний рейтинг пустого каталога")
    total_rating = 0
    for movie in movies:
        total_rating += movie["rating"]
    return round(total_rating / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    if not movies:
        raise ValueError("Нельзя вычислить возраст фильмов пустого каталога")
    ages = [current_year - movie["year"] for movie in movies]
    return max(ages), min(ages), math.ceil(sum(ages) / len(ages))


def duration_in_hours(minutes):
    return f"{minutes // 60}ч {minutes % 60}м"


#Этап 2
def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"


#Этап 3
def print_non_comedy(movies):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def print_first_masterpiece(movies):
    index = 0
    while index < len(movies):
        if movies[index]["rating"] > 9.0:
            print(movies[index]["title"])
            break
        index += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


#Этап 4
def normalize_title(title):
    words = []
    for word in title.lower().split():
        words.append(word[0].upper() + word[1:])
    return " ".join(words)


def make_slug(title):
    return normalize_title(title).lower().replace(" ", "-")


def format_report_line(movie):
    title = normalize_title(movie["title"])
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    return (
        f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, '
        f"{duration}, жанры: {genres}"
    )


#Этап 5
def titles_sorted_by_rating(movies):
    ordered_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in ordered_movies]


def top_n_by_rating(movies, n=3):
    if n < 0:
        raise ValueError("Количество фильмов в топе не может быть отрицательным")
    ordered_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in ordered_movies[:n]]


#Этап 6
def count_by_genre(movies):
    counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts


def actor_filmography(movies):
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []
            filmography[actor].append(movie["title"])
    return filmography


def ratings_above_average(movies):
    if not movies:
        return {}
    mean_rating = average_rating(movies)
    return {
        movie["title"]: movie["rating"]
        for movie in movies
        if movie["rating"] > mean_rating
    }


#Этап 7
def all_genres(movies):
    genres = set()
    for movie in movies:
        genres.update(movie["genres"])
    return genres


def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    return all_genres(movies_a) - all_genres(movies_b)


#Этап 8
def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def total_duration_above_seven(movies):
    return sum(movie["duration_min"] for movie in movies if movie["rating"] > 7)


if __name__ == "__main__":
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Возраст фильмов (старый, новый, средний): {catalog_age_stats(movies)}")
    duration = duration_in_hours(movies[0]["duration_min"])
    print(f"Длительность первого фильма: {duration}")
    print(f"Категория первого фильма: {rating_tier(movies[0]['rating'])}")
    print(f"Период первого фильма: {decade_label(movies[0]['year'])}")
    print("\nФильмы без жанра comedy:")
    print_non_comedy(movies)
    print("\nПервый фильм с рейтингом выше 9.0:")
    print_first_masterpiece(movies)
    print(f"Фильмов длиннее 120 минут: {count_long_movies(movies)}")
    print("\nНормализованное название:", normalize_title(movies[2]["title"]))
    print("Слаг:", make_slug(movies[2]["title"]))
    print(format_report_line(movies[7]))
    print("\nНазвания по рейтингу:", titles_sorted_by_rating(movies))
    print("Топ-3:", top_n_by_rating(movies))
    print("\nФильмов по жанрам:", sorted(count_by_genre(movies).items()))
    print("Фильмография O. Isaac:", actor_filmography(movies)["O. Isaac"])
    print("Рейтинги выше среднего:", ratings_above_average(movies))
    print("\nВсе жанры:", sorted(all_genres(movies)))
    print("Общие актёры:", sorted(common_actors(movies[0], movies[3])))
    print("Разность жанров:", sorted(genres_only_in_one(movies[5:6], movies[:5])))
    print("\nФильмы с рейтингом не ниже 8.0:")
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))
    print("Сумма минут при рейтинге выше 7:", total_duration_above_seven(movies))
