from flask import render_template
from flask import current_app as app

@app.route('/')
def home():
    """Homepage route."""
    return render_template('index.html')

@app.route('/spring')
def spring():
    """Spring season route."""
    return render_template('season.html', season='Spring')

@app.route('/summer')
def summer():
    """Summer season route."""
    return render_template('season.html', season='Summer')

@app.route('/autumn')
def autumn():
    """Autumn season route."""
    return render_template('season.html', season='Autumn')

@app.route('/winter')
def winter():
    """Winter season route."""
    return render_template('season.html', season='Winter')
