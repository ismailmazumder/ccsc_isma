from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import webbrowser

PORT = 8000
ROOT = Path(__file__).resolve().parent

if __name__ == '__main__':
    handler = SimpleHTTPRequestHandler
    server = ThreadingHTTPServer(('127.0.0.1', PORT), handler)
    url = f'http://127.0.0.1:{PORT}/main.html'
    print(f'Serving {ROOT} at {url}')
    webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nServer stopped.')
