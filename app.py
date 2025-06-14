from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head><title>Child Rescue Mission</title></head>
        <body style="background:#121212; color:white; text-align:center; font-family:sans-serif;">
            <h1>Welcome to Child Rescue Mission</h1>
            <p>This app is hosted on Railway and will stay online even when your phone is off.</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
