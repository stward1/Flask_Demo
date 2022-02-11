# Setup
Assuming you already have Python and Pip installed:
1. Run `pip install Flask` and `pip install CORS` to install dependencies (`pip install` would may work too)
2. Run `flask run`; if you get an error about sockets/ports already in use, try `flask run --port=3000` (`3000` can be any port, just an example)
3. Navigate to `localhost:3000` (the URL in the terminal works too; `3000` is whatever your port number is, swap out accordingly)

# Notes on Data and Client
The data is just an excel file in the `datatest` folder.
The client is just a basic HTML file with JavaScript to fetch from the Flask API. You should be able to load the excel data in by just opening `index.html` while running the Flask API (double check the port number on the fetch request URL if you don't use `3000`).