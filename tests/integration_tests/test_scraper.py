from pathlib import Path

from bs4 import BeautifulSoup
from scraper.scraper import scrap_course

BASE_DIR = Path(__file__).resolve(strict=True).parent


def test_scrap_course_happy_path():
    with open(Path(BASE_DIR, "../css.html")) as file:
        soup = BeautifulSoup(file, 'html.parser')
        courses = soup.find_all("table")
        for course in courses:
            scrap_course(course, "a[name^=\"css\"]", "AUT", "2019", None)
            break
