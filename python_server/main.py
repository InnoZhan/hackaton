# python_server/main.py
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from redis import Redis
import os
import cnn

app = Flask(__name__)
UPLOAD_FOLDER = '/home/kamil/Desktop/HACKATON/python_server/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
redis = Redis(host='redis', port=6379)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            cnn.test()
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template("index.html")

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = "80", debug=True)
