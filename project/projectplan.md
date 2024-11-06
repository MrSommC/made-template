# Project Plan
 
## Project Title

Adoption of Wind Energy Technology in the United States

## Main Question

Which states in the United States are leading in wind energy adoption, and what factors contribute to this?

## Description

This project will analyze the adoption rates of wind energy across different states in the United States. 
By investigating wind turbine installation data and correlating it with socioeconomic factors, 
the goal is to identify states leading in wind adoption and understand the contributing factors. 
This analysis can help highlight regions where further wind energy initiatives could be beneficial, 
potentially guiding future policies and investments in renewable energy infrastructure.

## Dataset 1 ##

**Title**: United States Wind Turbine Database  
**Source**: [https://catalog.data.gov/dataset/united-states-wind-turbine-database](https://catalog.data.gov/dataset/united-states-wind-turbine-database)  
**Description**: This dataset provides detailed locations and technical specifications for utility-scale wind turbines in the U.S., 
covering attributes such as turbine capacity, hub height, rotor diameter, installation year, and manufacturer. 
Updated quarterly, it reflects up to date information on wind energy infrastructure and includes verification ratings for location and turbine characteristics. 
This dataset will be used to analyze state-level trends in wind energy adoption and identify leading states
**Data Type**: Zip -> CSV

## Dataset 2 ##
**Title**: ACS 5YR Socioeconomic Estimate Data by State 
**Source**: [https://hudgis-hud.opendata.arcgis.com/datasets/7d6504755b604e02afea342ac9cf748f/about](https://hudgis-hud.opendata.arcgis.com/datasets/7d6504755b604e02afea342ac9cf748f/about)  
**Description**: The 2016-2020 ACS 5-Year estimates provide comprehensive socioeconomic data compiled at the state level, covering a range of characteristics like income, employment, and poverty. Key metrics include household income distribution, median earnings by education level, poverty rates by family and living arrangements, and workforce participation segmented by age and occupation. This dataset offers valuable insights into the economic and demographic composition of the U.S., making it suitable for analyzing regional socioeconomic trends and their potential impact on renewable energy adoption and other state-level initiatives
**Data Type**: Zip -> CSV


## Work Packages

1. Dataset Selection and Integration

Identify and gather relevant datasets, including wind turbine data and socioeconomic characteristics. Merge datasets at the state level to enable correlation analysis.

2. Automated Data Pipeline Construction

Build a pipeline for data ingestion, cleaning, and preprocessing to ensure consistency across data sources.

3. Exploratory Data Analysis (EDA) and Feature Engineering

Perform EDA to understand the distribution, trends, and relationships in the data. Engineer relevant features to capture socioeconomic and geographic factors that may influence wind energy adoption.

4. Statistical Analysis and Modeling

Apply statistical models to assess correlations between wind turbine adoption and socioeconomic indicators, identifying key factors that contribute to wind energy potential and deployment.

5. Model Evaluation: Performance, Interpretation, and Insights

Evaluate model accuracy and interpret findings to understand the socioeconomic and geographic factors impacting wind turbine placement and density. Extract actionable insights and trends.

6. Visualization and Geographic Mapping

Develop geographic maps and visualizations to present findings on wind energy adoption across states, highlighting key socioeconomic drivers.

7. Reporting and Documentation

Document all findings, methodologies, and insights in a comprehensive report. Summarize results in a presentation format to convey project insights to stakeholders.