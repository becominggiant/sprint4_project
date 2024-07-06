# sprint4_project
Sprint 4 - TripleTen - Project




Project Title: Car Listings Analysis

--Description--

This project is a tool to analyze car listings data and visualize various aspects such as price distribution, model year distribution, odometer readings, and more. It uses Streamlit for the web interface and Plotly Express for the visualizations.

--Features--

- Histograms: Visualize distributions for price, model year, odometer readings, and days listed.
- Scatter Plots: Show relationships between price and other variables such as odometer, model year, and cylinders.
- Bar Plots: Display the number of listings by condition, fuel type, and transmission type.
- Box Plots: Compare price distributions by condition, fuel type, and transmission type.
- Correlation Matrix: Heatmap to show correlations between numeric variables.
- Scatter Matrix: Scatter matrix plot to visualize relationships between multiple variables.


--Methods and Libraries Used--

- Streamlit: Used for creating the web application.
- Plotly Express: Used for creating interactive plots and charts.
- Pandas: Used for data manipulation and analysis


Installation Instructions
To run this project on your local machine, follow these steps:

Clone the Repository:

bash

git clone https://github.com/becominggiant/sprint4_project.git
cd sprint4_project
Create and Activate a Conda Environment:

bash

conda create --name car_listings_env python=3.8
conda activate car_listings_env


Install the Required Libraries:

Ensure you have all the required libraries installed by using requirements.txt.

bash
code:
pip install -r requirements.txt

Run the Streamlit App:

bash
code:
streamlit run app.py

Additional Notes

Make sure to commit and push each new file change to your GitHub repository as soon as you’ve completed it. This ensures that the online service has the latest version of your project files to build and deploy.