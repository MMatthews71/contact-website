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
    <title>External Communication</title>
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
            text-align: left;
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
        .contact-box {
            background: #f8f9fa;
            padding: 25px;
            border-radius: 12px;
            border-left: 5px solid #667eea;
            margin: 25px 0;
        }
        .contact-info {
            background: #e8f4ff;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
        }
        .note {
            color: #777;
            font-size: 0.9em;
            margin-top: 25px;
            padding-top: 15px;
            border-top: 1px solid #eee;
        }
        .warning {
            color: #d35400;
            background-color: #fff3cd;
            padding: 15px;
            border-radius: 8px;
            border-left: 5px solid #ffc107;
            margin: 15px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>External Communication Portal</h1>
        
        <p>Hi, I use this website to communicate to my clients on Fiverr about going off platform so that we don't get into any trouble with Fiverr's guidelines. We technically aren't allowed to go off platform, but they can't scan the contents of this website so I can give you my contacts on here.</p>
        
        <div class="warning">
            <p><strong>Important:</strong> This demonstrates how external communication can bypass platform monitoring. Fiverr's guidelines prohibit taking conversations off-platform, but external websites like this one are not scanned by their systems.</p>
        </div>
        
        <div class="contact-box">
            <p><strong>Contact me directly through these channels:</strong></p>
            
            <div class="contact-info">
                <p><strong>WhatsApp:</strong> +61 415618338</p>
                <p><strong>Email:</strong> matthewsmax44@gmail.com</p>
            </div>
            
            <p>Message me on WhatsApp or through email and we can continue talking about the project without having to be careful about what we say. We can discuss pricing, timelines, and any other details that might violate Fiverr's terms if discussed on their platform.</p>
        </div>
        
        <p>This method allows us to have completely private conversations that Fiverr cannot monitor or flag. We can share files, discuss payment methods, and coordinate work without any platform restrictions.</p>
        
        <p class="note">This website is hosted externally and is not connected to any freelancing platform's monitoring systems. All communications here are private and secure from platform scanning.</p>
    </div>
</body>
</html>
    ''')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)