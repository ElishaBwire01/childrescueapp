from flask import Flask

app = Flask(__name__)

# Main Homepage Route
@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Child Rescue Mission</title>
        <style>
            body {
                margin: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(to bottom right, #0f2027, #203a43, #2c5364);
                color: white;
            }

            nav {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 1rem 2rem;
                background-color: rgba(0, 0, 0, 0.5);
                position: sticky;
                top: 0;
                z-index: 1000;
            }

            nav h1 {
                color: #00aaff;
                margin: 0;
                font-size: 1.5rem;
            }

            nav ul {
                display: flex;
                list-style: none;
                gap: 1rem;
            }

            nav ul li a {
                color: white;
                text-decoration: none;
                transition: color 0.3s;
            }

            nav ul li a:hover {
                color: #00aaff;
            }

            header {
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 90vh;
                text-align: center;
                padding: 2rem;
            }

            header h2 {
                font-size: 3rem;
                margin-bottom: 1rem;
                color: #00aaff;
            }

            header p {
                font-size: 1.2rem;
                max-width: 600px;
            }

            .btn {
                margin-top: 1.5rem;
                padding: 0.75rem 1.5rem;
                background: #00aaff;
                border: none;
                border-radius: 5px;
                color: white;
                font-size: 1rem;
                cursor: pointer;
                transition: background 0.3s;
            }

            .btn:hover {
                background: #0077cc;
            }

            footer {
                text-align: center;
                padding: 1rem;
                background-color: rgba(0, 0, 0, 0.3);
                position: fixed;
                bottom: 0;
                width: 100%;
                font-size: 0.9rem;
            }

            @media (max-width: 768px) {
                nav ul {
                    flex-direction: column;
                    background: #000000a0;
                    padding: 1rem;
                    position: absolute;
                    right: 0;
                    top: 60px;
                    display: none;
                }

                nav:hover ul {
                    display: flex;
                }
            }
        </style>
    </head>
    <body>
        <nav>
            <h1>CHILD RESCUE MISSION</h1>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/programs">Programs</a></li>
                <li><a href="/donate">Donate</a></li>
                <li><a href="/contact">Contact</a></li>
            </ul>
        </nav>

        <header>
            <h2>Saving Children's Future</h2>
            <p>We are a non-profit organization based in Mombasa, Kenya focused on providing education, food, and shelter to orphans and the needy.</p>
            <a href="/donate"><button class="btn">Support Us</button></a>
        </header>

        <footer>
            &copy; 2025 Child Rescue Mission | All Rights Reserved
        </footer>
    </body>
    </html>
    """

# Other Page Routes

@app.route('/about')
def about():
    return "<h2 style='color:white; text-align:center;'>About Us Page Coming Soon...</h2>"

@app.route('/programs')
def programs():
    return "<h2 style='color:white; text-align:center;'>Programs Page Coming Soon...</h2>"

@app.route('/donate')
def donate():
    return "<h2 style='color:white; text-align:center;'>Donate Page Coming Soon...</h2>"

@app.route('/contact')
def contact():
    return "<h2 style='color:white; text-align:center;'>Contact Page Coming Soon...</h2>"

# Run the Flask App
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
