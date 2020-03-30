import unittest
import FlaskWebProject2


class TestBasic(unittest.TestCase):

    def setUp(self):
        FlaskWebProject2.app.testing = True
        self.app = FlaskWebProject2.app.test_client()

    def test_homepage(self):
        response = self.app.get('/', follow_redirects = True)
        self.assertEqual(response.status_code, 200)

    def test_rootpage(self):
        response = self.app.get('/home', follow_redirects = True)
        self.assertEqual(response.status_code, 200)

    def test_contactpage(self):
        response = self.app.get('/contact', follow_redirects = True)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
