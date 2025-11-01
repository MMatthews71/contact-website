from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-123')

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask App on Render</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f5f5f5;
            }
            .container {
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            button {
                background-color: #007bff;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                cursor: pointer;
                margin: 5px;
            }
            input {
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
                margin-right: 10px;
            }
            .task {
                padding: 10px;
                border-bottom: 1px solid #eee;
            }
            pre {
                background: #f8f9fa;
                padding: 10px;
                border-radius: 5px;
                overflow-x: auto;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Flask App Hosted on Render</h1>
            <p>This Flask application is successfully deployed on Render!</p>
            
            <div>
                <h3>Test API Endpoints:</h3>
                <button onclick="testHealth()">Test Health Check</button>
                <div>
                    <input type="text" id="nameInput" placeholder="Enter your name">
                    <button onclick="greet()">Greet Me</button>
                </div>
                <div id="apiResponse"></div>
            </div>

            <div>
                <h3>Task Manager (Demo)</h3>
                <input type="text" id="taskInput" placeholder="Enter task">
                <button onclick="addTask()">Add Task</button>
                <button onclick="loadTasks()">Load Tasks</button>
                <div id="tasksList"></div>
            </div>
        </div>

        <script>
            async function testHealth() {
                try {
                    const response = await fetch('/api/health');
                    const data = await response.json();
                    showResponse('Health Check: ' + JSON.stringify(data, null, 2));
                } catch (error) {
                    showResponse('Error: ' + error);
                }
            }

            async function greet() {
                const name = document.getElementById('nameInput').value || 'World';
                try {
                    const response = await fetch('/api/greet', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ name: name })
                    });
                    const data = await response.json();
                    showResponse('Greeting: ' + data.message);
                } catch (error) {
                    showResponse('Error: ' + error);
                }
            }

            async function addTask() {
                const title = document.getElementById('taskInput').value;
                if (!title) return;

                try {
                    const response = await fetch('/api/tasks', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ title: title })
                    });
                    const data = await response.json();
                    showResponse('Task added: ' + JSON.stringify(data, null, 2));
                    document.getElementById('taskInput').value = '';
                    loadTasks();
                } catch (error) {
                    showResponse('Error: ' + error);
                }
            }

            async function loadTasks() {
                try {
                    const response = await fetch('/api/tasks');
                    const data = await response.json();
                    const tasksList = document.getElementById('tasksList');
                    tasksList.innerHTML = '<h4>Tasks:</h4>' + 
                        (data.tasks.length ? 
                            data.tasks.map(task => 
                                `<div class="task">${task.id}. ${task.title} (${task.completed ? 'Completed' : 'Pending'})</div>`
                            ).join('') :
                            '<p>No tasks yet. Add one above!</p>');
                } catch (error) {
                    showResponse('Error: ' + error);
                }
            }

            function showResponse(message) {
                document.getElementById('apiResponse').innerHTML = 
                    '<pre>' + message + '</pre>';
            }
        </script>
    </body>
    </html>
    '''

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