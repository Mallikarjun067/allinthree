
    
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    user_name = request.form.get('username')
    return f"""
    <html>
        <body style="background:#1a1a2e; color:white; font-family:sans-serif; text-align:center; padding-top:50px;">
            <h1>Hello, {user_name}!</h1>
            <p>This response was generated dynamically by the Python container.</p>
            <a href="/" style="color:#e94560;">Go Back</a>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
