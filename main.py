
## main.py
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)

# Define the main route
@app.route('/')
def index():
    return render_template('index.html')

# Define the route to handle spreadsheet upload
@app.route('/upload', methods=['POST'])
def upload():
    # Extract event data from the uploaded spreadsheet
    event_data = extract_event_data(request.files['spreadsheet'])
    return redirect(url_for('create_events', event_data=event_data))

# Define the route to create events in Google Calendar
@app.route('/create_events', methods=['POST'])
def create_events():
    # Get the event data from the request
    event_data = request.form['event_data']
    # Create events in Google Calendar using the event data
    create_events_in_calendar(event_data)
    return redirect(url_for('index'))

# Define the route to render the configuration page
@app.route('/configure')
def configure():
    return render_template('configure.html')

# Define the route to save the user-specified configuration values
@app.route('/save_configuration', methods=['POST'])
def save_configuration():
    # Get the configuration values from the request
    configuration_values = request.form['configuration_values']
    # Save the configuration values
    save_configuration_values(configuration_values)
    return redirect(url_for('index'))

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
