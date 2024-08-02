## Flask Application Design

### HTML Files

- **index.html**: The main web page of the application. This file should include elements for user input, such as a spreadsheet upload form and configuration options.

### Routes

- **index**: The root route of the application. It handles rendering the index.html page.
- **upload**: A POST route that processes the uploaded spreadsheet and extracts event data from it.
- **create_events**: A POST route that uses the extracted event data to create events in the specified Google Calendar.
- **configure**: A GET route that renders a configuration page where users can adjust settings such as the target calendar and column mappings.
- **save_configuration**: A POST route that saves the user-specified configuration values.