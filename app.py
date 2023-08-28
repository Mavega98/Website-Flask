from flask import Flask, render_template
import invoice_table_data

# Create a Flask web application
app = Flask(__name__)

# Define a route for the homepage
@app.route("/")
def index():
    """
    This function handles the request to the homepage.
    It renders the 'index.html' template.
    """
    return render_template("index.html")

# Define a route for running a function and displaying its result
@app.route('/run_function')
def run_function():
    """
    This function handles the request to run a specific function ('print_invoice')
    and displays the result on the 'invoice_data.html' template.
    """
    try:
        result = invoice_table_data.invoice_start_message()  # Run the 'print_invoice' function
    except Exception as e:
        result = str(e)  # If an exception occurs, capture the error message

    return render_template("invoice_data.html", result=result)

# Run the Flask app if this script is executed directly
if __name__ == "__main__":
    """
    If this script is executed directly (not imported as a module
    start the Flask app using the 'app.run()' method.
    """
    app.run()
