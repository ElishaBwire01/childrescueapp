from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Child Rescue Mission</title>
            <style>
                body {
                    background-color: #121212;
                    color: white;
                    text-align: center;
                    font-family: Arial, sans-serif;
                    padding-top: 100px;
                }
            </style>
        </head>
        <body>
            <h1>Welcome to Child Rescue Mission</h1>
            <p>This app is hosted on Railway and will stay online 24/7.</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
