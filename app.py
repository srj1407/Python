from flask import Flask, render_template

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route and the function to handle it
@app.route('/list')
def hello_list():
    list_items = ['Item 1', 'Item 2', 'Item 3', 'Item 4']
    return render_template('greeting.html', list_items=list_items)

# This part is needed to run the app directly
if __name__ == '__main__':
    app.run(debug=True)