from flask_testing import TestCase
from flask import current_app, url_for
from server import application


class MainTest(TestCase):

    def create_app(self):
        """"Creation of application"""
        application.config['TESTING'] = True
        application.config['WTF_CSRF_ENABLED'] = False
        return application

    def test_app_exists(self):
        """Test the app exists"""
        self.assertIsNotNone(current_app)

    def test_blueprint_exists(self):
        """Test blueprint exists"""
        self.assertIn('main_pages', self.app.blueprints)
        self.assertIn('main_api', self.app.blueprints)

    def test_index_get(self):
        """Test index view returns 200 status"""
        response = self.client.get(url_for('main_pages.index'))
        self.assert_200(response)

    def test_api_users_get(self):
        """Test API can get a users list (GET request)."""
        response = self.client.get('/api/users', headers={"Content-Type": "application/json"})
        self.assertEqual(list, type(response.json['users']))
        self.assertNotEqual([],response.json['users'])
        self.assertIn('users',response.json)
        self.assertIn('actual_page',response.json)
        self.assertIn('pages',response.json)
        self.assertIn('total',response.json)
        self.assertEqual(200, response.status_code)

    def test_api_users_get_order_by_username(self):
        """Test API can get a users list ordering by username(GET request)."""
        response = self.client.get('/api/users?page=1&page_size=10&order_by=username&order=asc',
                                   headers={"Content-Type": "application/json"})
        self.assertEqual(200, response.status_code)

    def test_api_users_get_order_by_id(self):
        """Test API can get a users list ordering by id (GET request)."""
        response = self.client.get('/api/users?page=1&page_size=10&order_by=id&order=asc',
                                   headers={"Content-Type": "application/json"})
        self.assertEqual(200, response.status_code)