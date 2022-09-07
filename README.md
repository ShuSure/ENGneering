# ENGneering

Winery recommendation system
## Abstract
•	A e-commerce startup company want to design an winery recommendation system to attract more visitors for their websites.
•	We need to establish a winery recommendation app for them
## Design
### data pipline part
•	Download Data from Kaggle
•	Ingested Data into Sqlite by DB Browser
•	preprocessing Data by pySpark
• Further preprocessing and Model building by Python
•	Flask app build 
•	lauch Flask app onto Heroku
### NLP model part
•	By using K-Means, we clustered 130k blind-test reviews into 10 groups
•	Each group has a special ‘taste’ for wines
•	Build engine upon clusters by using cosine-similarity
## Data
•	Data comes from Kaggle program-wine reviews
•	Rows:130k wine reviews
•	Columns(used): description/variety/winery/province/region
## Algorithms
### pipline
To begin the process of creating a data pipeline that was deployed into the dashboard, a CSV containing winery data from kaggle was pulled. 
This data was uploaded into a SQLite database, and pulled into a Jupyter notebook using pySpark. PySpark was also used to clean the data prior to converting the pySpark dataframe to Pandas dataframe in which further cleaning and manipulation was carried out.
Data was uploaded to GitHub and deployed to a live Streamlit app
#### Feature Engineering
1.	Reduce varieties from 1500→10
2.	NLP: Tf - idf vectorizer/stem/lemmatize
3.	K Means cluster by 10 groups
4.	eyeball analysis the 1-1 relationship from clusters to wine varieties
5.	Count Vectorizer/Cosine similarity to build engine(Feature: features: region_1','province','variety','cluster','description)
#### Models
K-means cluster
## Tools
•	Flask
•	Pandas / NumPy / seaborn
•	Kmeans /cosine similarity
•	Matplotlib/WordCloud
•	TfidfVectorizer / RegexpTokenizer /
•	   Snowball Stemmer / Count Vectorizer
•	Matplotlib and Seaborn for plotting
## Communication
In addition to the slides and visuals presented, I also built a flask app to visualize my engine, LinkedIn link are also pasted.
