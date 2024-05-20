# E-Commerce Scraper

This is a Python application that scrapes e-commerce data from https://www.laptopsdirect.co.uk/ct/monitors-and-projectors/monitors/curved and provides various functionalities like showing the data in a graph or matrix form, and exporting the data.

## Installation

You can download this project directly from GitHub by clicking on the `Code` button and then `Download ZIP`. After downloading and extracting the ZIP file, navigate to the project directory in your terminal.

Alternatively, you can clone the repository:

1. Clone the repository:

    `git clone https://github.com/yourusername/yourrepository.git`

2. Navigate to the project directory:
    `cd path/to/repository`

Then, follow these steps:

3. Create a virtual environment:
    `python -m venv venv`

4. Activate the virtual environment:
    - On Windows, run: `.\venv\Scripts\activate`
    - On Unix or MacOS, run: `source venv/bin/activate`

5. Install the requirements:
    `pip install -r requirements.txt`


## Usage

Run the main script:
    - on Windows, run: `python src/app.py`
    - On Unix or MacOS, run: `python3 src/app.py`


## Features

- Retrieve data: Fetches the e-commerce data.
- Show graph: Displays the data in a graph form.
- Show matrix: Displays the data in a matrix form.
- Export data: Exports the data to a CSV file.

## Cross Platform

The app has been tested on a Windows 11 machine and also on Ubuntu 22.04 via Windows Subsystem for Linux (WSL).