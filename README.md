# Page View Time Series Visualizer

This project is a Page View Time Series Visualizer that analyzes and visualizes freeCodeCamp forum page view data over time. The aim is to provide insights into user engagement with the forum by displaying trends and patterns in page views from May 2016 to December 2019.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Functionality](#functionality)
- [Contributing](#contributing)
- [License](#license)

## Features

- Visualize daily page views using line plots.
- Display average monthly page views grouped by year in bar charts.
- Analyze distribution of page views with box plots for seasonal trends.
  
## Technologies Used

- Python 3.x
- Pandas for data manipulation
- Matplotlib for plotting
- Seaborn for statistical data visualization

## Installation

To run this project, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

git clone https://github.com/freeCodeCamp/boilerplate-page-view-time-series-visualizer.git
cd boilerplate-page-view-time-series-visualizer


### Step 2: Install Dependencies

You will need to install the required libraries. You can do this using pip:

pip install pandas matplotlib seaborn


## Usage

To use the Page View Time Series Visualizer, run the `main.py` script. This script will execute the analysis and generate visualizations based on the page view data.

### Example Command Line Usage

1. Open your terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command:
   python main.py


## Functionality

The main functionalities of this project include:

1. **Data Loading**: The program reads page view data from `fcc-forum-pageviews.csv`.
2. **Data Cleaning**: It filters out outliers by removing the top and bottom 2.5% of page views.
3. **Visualization**:
   - Draws a line plot showing daily page views over time.
   - Creates a bar plot showing average daily page views for each month grouped by year.
   - Generates box plots to visualize the distribution of page views by year and month.
