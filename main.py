from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/result', methods = ["GET", "POST"])
def handleResults():
    if request.method == "GET":
        return render_template('error.html')
    else:
        result = model.get_topics(request.form["search"])
        # print(result)
        if not result:
            return render_template('error.html')
        return render_template('result.html', topics=result)

@app.route('/categories', methods=['GET'])
def categories():
    return render_template('categories.html', titles=model.itemList)
    
@app.route('/resources', methods=['GET'])
def resources():
    return render_template('resources.html')

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
