from flask import Flask, render_template_string
import os

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-123')

@app.route('/')
def home():
    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Showcase</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 700px;
            margin: 0 auto;
            padding: 40px 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .container {
            background: white;
            padding: 50px 40px;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            text-align: center;
            width: 100%;
        }
        h1 {
            color: #333;
            margin-bottom: 25px;
            font-size: 2.2em;
            font-weight: 400;
        }
        p {
            color: #555;
            font-size: 1.1em;
            line-height: 1.6;
            margin-bottom: 20px;
        }
        .demo-box {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 12px;
            border-left: 5px solid #667eea;
            margin-top: 25px;
        }
        .note {
            color: #777;
            font-size: 0.9em;
            margin-top: 15px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Sample Project Demo</h1>
        <p>This page demonstrates the layout and visual style used for client-facing dashboards. 
        It’s a static example meant to show the interface structure and data presentation.</p>

        <div class="demo-box">
            <p><strong>NBA Player Stats</strong></p>
            <p>LeBron James — Projected Points: <strong>28.4</strong></p>
            <p>Jayson Tatum — Projected Points: <strong>26.1</strong></p>
            <p>Stephen Curry — Projected Points: <strong>29.8</strong></p>
        </div>

        <p class="note">This is a demo for display purposes only. Data is fictional.</p>
    </div>
</body>
</html>
    ''')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
