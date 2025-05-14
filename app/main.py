from flask import Flask
from prometheus_client import start_http_server, Summary

app = Flask(__name__)

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@REQUEST_TIME.time()
@app.route('/')
def index():
    return 'Hello, from DevOps Boy!'

if __name__ == '__main__':
    start_http_server(5000)  # Expose metrics on port 5000
    app.run(host='0.0.0.0', port=5000)
