from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-123')

@app.route('/')
def home():
    return render_template('index.html', title='Home')

@app.route('/api/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'service': 'Flask App',
        'version': '1.0.0'
    })

@app.route('/api/greet', methods=['POST'])
def greet():
    data = request.get_json()
    name = data.get('name', 'World')
    return jsonify({'message': f'Hello, {name}!'})

# Simple in-memory "database" for demo
tasks = []

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = {
        'id': len(tasks) + 1,
        'title': data.get('title'),
        'completed': False
    }
    tasks.append(task)
    return jsonify(task), 201

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)