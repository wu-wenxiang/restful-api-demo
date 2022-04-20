import os
from pecan.deploy import deploy
import sys
from wsgiref import simple_server

conf = os.path.join(os.path.dirname(__file__), 'config.py')
app = deploy(conf)

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8080

    if len(sys.argv) > 1:
        host = sys.argv[1]

    if len(sys.argv) > 2:
        port = int(sys.argv[2])

    print(f'please try: http://{host}:{port}')
    serve = simple_server.make_server(host, port, app)
    serve.serve_forever()
