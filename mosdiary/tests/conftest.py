from mosdiary.models import User
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db = tempfile.NamedTemporaryFile()
        self.app = User.app.test_client()
        User.DATABASE = self.db.name
        User.init_db()

if __name__ == '__main__':
    unittest.main()

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db = tempfile.NamedTemporaryFile()
        self.app = User.app.test_client()
        User.DATABASE = self.db.name
        User.init_db()

    def test_empty_db(self):
        rv = self.app.get('/')
        assert 'No entries here so far' in rv.data

def login(self, username, password):
    return self.app.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)

def logout(self):
    return self.app.get('/logout', follow_redirects=True)

def test_messages(self):
    self.login(User.USERNAME, User.PASSWORD)
    rv = self.app.post('/add', data=dict(
        title='<Hello>',
        text='<strong>HTML</strong> allowed here'
    ), follow_redirects=True)
    assert 'No entries here so far' not in rv.data
    self.login(User.USERNAME, User.PASSWORD)
    assert '&lt;Hello&gt' in rv.data
    assert '<strong>HTML</strong> allowed here' in rv.data