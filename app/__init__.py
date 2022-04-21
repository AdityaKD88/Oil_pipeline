import logging
from flask import Flask, render_template

try:
    from sklearn.externals import joblib
except:
    import joblib

# create logger for app
logger = logging.getLogger('app')
logger.setLevel(logging.INFO)

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT)

app = Flask(__name__)
app.config.from_object("app.config")





# Handle Bad Requests
@app.errorhandler(404)
def page_not_found(e):
    """Page Not Found"""
    return render_template('404.html'), 404