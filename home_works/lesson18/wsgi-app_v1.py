from wsgiref.simple_server import make_server


def simple_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    start_response(status, headers)
    return [b'Hello world']


with make_server('', 8000, simple_app) as httpd:
    print('Starting the WSGI server...')
    httpd.serve_forever()