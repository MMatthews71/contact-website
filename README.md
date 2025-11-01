# Flask App for Render

A simple Flask application ready to deploy on Render.

## Features
- RESTful API endpoints
- Simple task manager demo
- Health check endpoint
- Responsive web interface

## Deployment on Render

1. Fork/push this code to a GitHub repository
2. Connect your GitHub account to Render
3. Create a new Web Service
4. Select your repository
5. Use these settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py