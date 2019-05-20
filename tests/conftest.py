import os
import tempfile
from datetime import datetime

import pytest
from flaskr import create_app, db
from flaskr.models.user import User
from flaskr.models.blog import Blog

@pytest.fixture
def app():
    db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:////' + db_path[1],
    })

    with app.app_context():
        db.init_app(app)
        db.create_all()
        populate_db()
    
    yield app

    os.unlink(db_path[1])

def populate_db():
    user_one = User(
        username = 'test',
        password = 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'
    )
    user_two = User(
        username = 'other',
        password = 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79'
    )
    blog_one = Blog(
        title = 'test title',
        body = 'test\nbody',
        author_id = 1,
        created = datetime.strptime(
            '2018-01-01 00:00:00',
            '%Y-%m-%d %H:%M:%S'
        )
    )
    db.session.add(user_one)
    db.session.add(user_two)
    db.session.add(blog_one)
    db.session.commit()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post(
            '/auth/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)
