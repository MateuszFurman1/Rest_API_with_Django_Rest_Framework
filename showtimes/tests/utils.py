from random import sample
import pytz
from faker import Faker
from movielist.models import Movie
from movielist.tests.utils import create_fake_movie
from showtimes.models import Cinema, Screening

faker = Faker("pl_PL")
TZ = pytz.timezone('UTC')


def random_movies():
    """Return 3 random Movies from db."""
    movies = list(Movie.objects.all())
    return sample(movies, 3)


def add_screenings(cinema):
    """Add 3 screenings for given cinema."""
    movies = random_movies()
    for movie in movies:
        Screening.objects.create(cinema=cinema, movie=movie, date=faker.date_time(tzinfo=TZ))


def fake_cinema_data():
    """Generate fake data for cinema."""
    return {
        "name": faker.name(),
        "city": faker.city(),
    }


def create_fake_cinema():
    """Create fake cinema with some screenings."""
    cinema = Cinema.objects.create(**fake_cinema_data())
    add_screenings(cinema)