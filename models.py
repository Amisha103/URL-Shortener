from database import db
from datetime import datetime

class URL(db.Model):
    __tablename__ = "urls"

    id = db.Column(db.Integer, primary_key=True)

    original_url = db.Column(
        db.Text,
        nullable=False
    )

    short_code = db.Column(
        db.String(10),
        unique=True,
        nullable=False,
        index=True
    )

    click_count = db.Column(
        db.Integer,
        default=0
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    '''
    | Column         | Purpose                                     |
| -------------- | ------------------------------------------- |
| `id`           | Primary key                                 |
| `original_url` | The long URL entered by the user            |
| `short_code`   | The generated code (e.g. `aB12Xy`)          |
| `click_count`  | Track how many times the short URL was used |
| `created_at`   | Record when the URL was created             |
    
    '''