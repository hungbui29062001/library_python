from library.extension import db
# from datetime import datetime

class TokenBlockList(db.Model):
    __tablename__ = 'tokenblocklist'

    id = db.Column(db.Integer, primary_key = True)
    jti = db.Column(db.String(), nullable = True)
    # created_at = db.Column(db.DateTime(), default = datetime.now(datetime.UTC))