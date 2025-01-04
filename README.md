# Do socioeconomic factors correlate with wind energy adoption in the United States?

# Introduction and Motivation 

Wind energy plays a significant role in the transition to renewable energy. However, the adoption of wind turbines across the United States varies by state. This project explores the relationship between socio-economic factors, such as poverty levels, median income, and education—and wind energy adoption. By analyzing these trends, this project seeks to address the primary question: Do favorable socio-economic conditions correlate with higher wind turbine adoption in the United States?

# Description of This Project

This project investigates the correlation between socio-economic factors and wind energy adoption across U.S. states. It follows a structured data pipeline that includes data extraction, cleaning, transformation, and integration. Detailed information about the data sources and preprocessing steps can be found in project/data-report.pdf. The results of the analysis are summarized in project/analysis-report.pdf. All visualizations generated during the analysis are saved in project/.
The pipeline includes unit tests to ensure data quality and correctness, and GitHub Actions are set up to run these tests automatically upon any changes to the repository.

# Datasets Used In This Project

U.S. Wind Turbine Database: The U.S. Wind Turbine Database is a U.S. Government Work, available for public access and use under the public domain. [source](https://catalog.data.gov/dataset/united-states-wind-turbine-database)

ACS 5-Year Socioeconomic Estimate Data: The ACS 5-Year Socioeconomic Estimate Data is also a U.S. Government Work. [source](https://hudgis-hud.opendata.arcgis.com/datasets/7d6504755b604e02afea342ac9cf748f/about)

# Datapipeline of This Project

![pipeline_IMG](https://github.com/user-attachments/assets/892a7958-3a47-448b-ab60-3f4018aef337)


# Key Visualizations From the Project

1. US-States With the Highest Number of Turbines

<img src="https://github.com/user-attachments/assets/94328ec0-7b5d-4d7e-8e66-445b438a6577" alt="US-States With the Highest Number of Turbines" width="380"/>

A bar chart displaying the top 10 US states with the highest number of wind turbines from 1982 to 2024.

2. Map of Top 10 Wind Energy States

<img src="https://github.com/user-attachments/assets/c5eb6ee9-5637-45e1-be2f-39af5c22fcef" alt="Map of Top 10 Wind Energy States" width="380"/>

A geographical map highlighting the US states with the highest number of wind turbines in blue.

3.  Top 10 States by Poverty, Income Ranking and College Education

<img src="https://github.com/user-attachments/assets/1eb3c403-fcfd-4e94-a950-fad710368e11" alt="Top 10 States by Poverty, Income Ranking and College Education" width="380"/>

Three bar charts comparing US states based on poverty, median income, and bachelor's degree attainment to identify states with the most favorable socioeconomic conditions.

4.  Intersections of Socioeconomic Factors by State

<img src="https://github.com/user-attachments/assets/26b437fe-c803-48b8-9a55-8e3dc8280c0f" alt="Intersections of Socioeconomic Factors by State" width="380"/>

A Venn diagram showing the overlap of states excelling in poverty, income, and education, highlighting those with the best overall socioeconomic conditions.

5. Correlation Matrix: Socio-Economic Factors vs. Wind Turbines Per State

<img src="https://github.com/user-attachments/assets/353d43de-eaa7-42e1-9816-644190575416" alt="Correlation Matrix: Socio-Economic Factors vs. Wind Turbines Per State" width="420"/>

A correlation matrix comparing states with high wind turbine adoption to those with favorable socioeconomic factors, identifying overlaps and relationships.

# Further Information

Please note that the final results outlined in the final report in project/analysis-report.pdf are based on only two datasets, for a holistic analysis of the research questions further research should be conducted. 

If there are any questions about the pipeline or analysis please write an E-Mail to: christoph.sommermann@fau.de
