from flaskr import app

@app.route('/')
def home_page():
    return '<p>Hello, World!</p>'