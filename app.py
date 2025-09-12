import socket
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check_ip', methods=['GET'])
def check_ip():
    urls_param = request.args.get('urls')
    if not urls_param:
        return jsonify({"error": "URL parameter is missing"}), 400

    # カンマで区切られたURL文字列をリストに変換
    urls = [url.strip() for url in urls_param.split(',')]
    results = {}

    for url in urls:
        try:
            ip_address = socket.gethostbyname(url)
            results[url] = ip_address
        except socket.gaierror:
            results[url] = "Could not resolve the IP address"
            
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)