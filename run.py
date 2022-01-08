from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(list(request.form.keys()))[0]
        if list(request.form.keys())[0] == 'button':
            print(request.form['button'])

        if list(request.form.keys())[0] == 'button2':
            print(request.form['button2'])

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)