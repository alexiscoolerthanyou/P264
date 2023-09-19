# Import Libraries below
import os
import cv2
from flask import  Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

# Define flask 
app = Flask(__name__)
@app.route('/')
def main():
    return render_template("index.html")
@app.route('/', methods=['POST'])
def upload_video():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join('static/', filename))
    return render_template('upload.html', filename=filename)

@app.route('/display/')
def display_video(filename):
    return redirect(url_for('static', filename = filename))

if __name__ == "__main__":
    app.run(debug=True)
