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
    <title>Sample Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
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
            margin-bottom: 30px;
            font-size: 2.5em;
            font-weight: 300;
        }
        .contact-methods {
            margin: 40px 0;
        }
        .contact-item {
            background: #f8f9fa;
            padding: 25px;
            margin: 20px 0;
            border-radius: 15px;
            border-left: 5px solid #667eea;
            transition: transform 0.3s ease;
        }
        .contact-item:hover {
            transform: translateX(10px);
            background: #f1f3f4;
        }
        .contact-label {
            font-weight: bold;
            color: #555;
            font-size: 1.1em;
            display: block;
            margin-bottom: 8px;
        }
        .contact-value {
            color: #333;
            font-size: 1.4em;
            font-weight: 600;
        }
        .message {
            color: #666;
            font-size: 1.2em;
            line-height: 1.6;
            margin-bottom: 40px;
            padding: 0 20px;
        }
        .whatsapp {
            color: #25D366;
        }
        .email {
            color: #EA4335;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Let's Work Together</h1>
        
        <div class="message">
            Hi, this isn't a sample website, it's just my contact. Fiverr doesn't allow me to add my contact methods to my profile, so 
            I get around it by sending this link. Please contact me in one of these methods and we can begin work. 
            This is all safe, it just allows easier communication so we can be more efficient.
        </div>

        <div class="contact-methods">
            <div class="contact-item">
                <span class="contact-label whatsapp">WhatsApp</span>
                <div class="contact-value">+61 415 618 338</div>
            </div>
            
            <div class="contact-item">
                <span class="contact-label email">Email</span>
                <div class="contact-value">matthewsmax44@gmail.com</div>
            </div>
        </div>
    </div>
</body>
</html>
    ''')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)