from flask import Flask, request, jsonify, render_template, redirect, send_file

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('enterpanel.html')

@app.route('/api', defaults={'path': ''}, methods=['POST','GET','PUT', 'OPTIONS', 'PATCH', 'CONNECT', 'TRACE', 'HEAD'])
@app.route('/api/<path:path>')
def catch_all(path):
    data = {
        'method': request.method,
        'url': request.url,
        'headers': dict(request.headers),
        'body': request.get_data(as_text=True)
    }
    with open('http_log.txt', 'a') as f:
        f.write(f'{data}\n')
    return jsonify(data)

@app.route('/panel')
def show_http_requests():
    with open('http_log.txt', 'r') as f:
        http_log = f.read()
    http_requests = http_log.split('\n')
    print(http_requests)
    return render_template('panel.html', http_requests=http_requests)

@app.route('/requestapi')
def request_api():
    return render_template('requestapi.html')

if __name__ == '__main__':
    app.run(port=80)