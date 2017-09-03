from django.test import Client, TestCase

class EndpointTestCase(TestCase):
    # Test POST request
    def test_post(self):
        c = Client()
        response = c.post('/')
        expected_response = b'<p>Post Request</p>'
        self.assertEqual(response.content, expected_response)

    # Test GET requests for: JSON accepted
    def test_get_json(self):
        c = Client()
        response = c.get('/',HTTP_ACCEPT='application/json')
        expected_response = b'{"message": "Good morning"}'
        self.assertEqual(response.content, expected_response)

    # Test GET requests for: JSON not accepted 
    def test_get_no_json(self):
        c = Client()
        response = c.get('/',HTTP_ACCEPT='application/javascript')
        expected_response = b'<p>Hello, World</p>'
        self.assertEqual(response.content, expected_response)

    def test_put(self):
        c = Client()
        response = c.put('/',HTTP_ACCEPT='application/javascript')
        expected_response = b'<p>This Request method is not handled.</p>'
        self.assertEqual(response.content, expected_response)
