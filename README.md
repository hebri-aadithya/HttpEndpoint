Simple Django HTTP Endpoint that handles POST and GET Requests

Software requirements: Python (I used Python 3), Django, cURL

Setup and Running Instructions:
1. Clone the repo from https://github.com/hebri-aadithya/HttpEndpoint.git
2. Run 'cd SimpleHTTPEndpoint/' in the directory where you cloned the repo.
3. To run the application: python manage.py runserver
4. To run the test cases: python manage.py test tests/

Notes:
1. Test cases are present in SimpleHTTPEndpoint/tests in the test_endpoint.py file.
2. The application handles GET and POST requests and presents a message saying 'not handled' for other HTTP methods.
3. For a GET request, if 'application.json' is present in the ACCEPT header, JSON data is sent back. Else, HTML data is sent.
