from flask import Flask, render_template, request, redirect, url_for

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route and the function to handle it
@app.route('/list')
def hello_list():
    list_items = ['Item 1', 'Item 2', 'Item 3', 'Item 4']
    return render_template('greeting.html', list_items=list_items)

@app.route('/home')
def home():
    return "<h1>Home</h1>"

@app.route('/json')
def json():
    return {"key": "value", "my_list": [1, 2, 3, 4]}

@app.route('/getRequest', methods=['GET'])
def get_request():
    return "<p>GET Request Received</p>"

@app.route('/dynamic', defaults={'user_input': 'default_value'})
@app.route('/dynamic/<user_input>')
def dynamic_input(user_input):
    return f"<p>GET Request Received with user input: {user_input}</p>"

@app.route('/query')
def query():
    param1=request.args.get('param1')
    return f"<p>GET Request Received with user input: {param1}</p>"

@app.route('/form', methods = ['GET', 'POST'])
def form():
    if request.method == 'POST':
        name=request.form.get('name')
        return f"<p>POST Request Received with user input: {name}</p>"
    return "<form method='POST'> Name: <input type='text' name='name'><input type='submit'></form>"

@app.route('/acceptjson', methods = ['GET', 'POST'])
def acceptjson():
    data=request.get_json()
    fname=data.get('fname')
    lname=data.get('lname')
    return {"fname": fname, "lname": lname}

@app.route('/formRedirect', methods = ['GET', 'POST'])
def formRedirect():
    if request.method == 'POST':
        name=request.form.get('name')
        print(name)
        return redirect(url_for('home'))
    return "<form method='POST'> Name: <input type='text' name='name'><input type='submit'></form>"

# This part is needed to run the app directly
if __name__ == '__main__':
    app.run(debug=True)