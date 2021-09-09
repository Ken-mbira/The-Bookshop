from flask import render_template
from app import app

@app.route('/')
def index():
    """
    View of the root page that is the index.html
    """
    title = "THE BOOKSHOP"
    return render_template('index.html',title = title)