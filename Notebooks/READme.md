## Notebooks Overview

### Barplot.ipynb
Barplot.ipynb is a notebook that visualizes happiness across different regions. It loads the necessary datasets and displays the happiness distribution across the world map for each region. After illustrating regional differences, it checks for changes in mean happiness scores over the years. Lastly, it presents the most and least happy countries from 2015 to 2019.

### Maxcolumn.ipynb
Maxcolumn.ipynb is a notebook that identifies the columns with the biggest impact on the happiness score. It loads the required datasets and creates a new column indicating the variable with the most significant impact on the happiness score. Additionally, it showcases the distribution of the maximum column based on happiness scores. The final cell plots the world map, coloring countries based on the maximum column in each country. The analysis is based on the years 2015 and 2016.

### World map.ipynb
World map.ipynb is a notebook that plots the world map using the Folium library. It loads the necessary datasets and utilizes Folium for plotting. Initially, it plots the world map with all countries colored pink. Then, it fills the colors based on the happiness score.

### Correlation.ipynb
Correlation.ipynb is a notebook designed to analyze correlations between different columns in datasets from the "Is the World Happy" project. The notebook allows users to specify the year (x) for which they want to see correlations. The 'read(x)' function reads in the datasets and ensures uniformity in column names and sorting. It creates a new column "target" to visualize correlations based on the ranking of each country. Correlations with heatmaps are generated for each year, along with correlations between the happiness score and other columns. The notebook also produces residual graphs to illustrate the evolution of correlations over the years. Lastly, scatter plots of individual columns versus each other are created, as well as all columns against each other for a specific year (x).

### all in one notebook.ipynb

- **Libraries and Setup**: Imports Numpy, Pandas, Seaborn, and Matplotlib; configures the environment.
- **Data Loading**: Reads happiness data from 2015, 2016, and 2017; adjusts column names for consistency.
- **Exploratory Data Analysis**: Shows initial data, checks for missing values, and lists unique regions.
- **Visualization**: Generates pair plots, heatmaps, bar charts, and more to visualize data relationships.
- **Comparative Analysis**: Assesses GDP per capita trends and happiness ratios by region.
- **Aggregated Trends**: Combines yearly data to analyze overall happiness trends.
- **Clustering**: Applies hierarchical and K-means clustering on social support and life expectancy data.





