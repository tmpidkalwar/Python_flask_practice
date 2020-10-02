from flask import Flask, render_template, request

# name of the module that is currently running in the flask
app = Flask(__name__)

# When visit this webpage, to return given information, use route
# parameter '/' signifies the home page to be returned. 
# Below definition describes the home page.
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/your-url', methods=['GET','POST'])
def your_url():
    if request.method == 'POST':
        return render_template('your_url.html', code=request.form['code'])
    else:
        return 'This is not Valid'