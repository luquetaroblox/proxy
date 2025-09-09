import os
import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    target_url = f"http://213.142.135.46:9999/{path}"
    response = requests.request(
        method=request.method,
        url=target_url,
        data=request.get_data(),
        headers=request.headers
    )
    return response.text, response.status_code, {"Content-Type": response.headers.get("Content-Type")}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
