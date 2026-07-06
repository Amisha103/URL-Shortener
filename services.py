from models import URL
from database import db
from utils import generate_short_code

def create_short_url(original_url):
    while True:
        short_code = generate_short_code()

        existing = URL.query.filter_by(short_code=short_code).first()

        if not existing:
            break

    new_url = URL(
        original_url=original_url,
        short_code=short_code
    )

    db.session.add(new_url)
    db.session.commit()

    return new_url



def get_original_url(short_code):
    url = URL.query.filter_by(short_code=short_code).first()

    if not url:
        return None

    url.click_count += 1
    db.session.commit()

    return url