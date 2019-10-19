from unittest import TestCase, main
import json
from server.app import app


class IntegrationTestExample(TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.url = '/api/example/color'
        self.headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def test_post_ok(self):
        payload = {'color': 'red',
                   'size': 123,
                   'is_active': True,
                   'year': 2020
                   }
        query_string = {'identifier': '123'}
        expected_body = {'identifier': '123', 'value': 'red'}
        response = self.app.post(path=self.url, data=json.dumps(payload),
                                 headers=self.headers, query_string=query_string)
        self.assertEqual(expected_body, response.json)

    def test_post_fail(self):
        payload = {'color': 'red',
                   'size': 123,
                   'is_active': True,
                   'year': 0
                   }
        response = self.app.post(path=self.url, data=json.dumps(payload), headers=self.headers)
        self.assertEqual(400, response.status_code)


if __name__ == '__main__':
    main()
