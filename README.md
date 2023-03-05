# Mid-Bootcamp Project: Creating an API and Dashboard

# Description
In this project, i created an API to serve data from a penguin dataset that was enriched with data obtained from another API. We used webscraping to extract additional information and stored it in a database. I designed the API with multiple endpoints that used various parameters to allow for different types of requests.

Also created a Streamlit dashboard to visualize the data obtained from the API. The dashboard allowed for interactive visualizations, and i used different streamlit widgets to allow for user interaction with the visualizations. I have also been able to add functionalities to be able to create a user and add it to the database, for later verification so that users are not repeated. Also in the same dashboard you can have contact via email for the user.

Before creating the API and dashboard, i cleaned and formatted the penguin dataset, eliminating penguins with missing values in multiple columns. Also used the available data to determine the sex of some of the penguins that had missing values in the sex column.


<p align="center">
  <img src="https://github.com/Santiagoestremadoyro/mid-bootcamp-work/blob/main/img/NA_colums.png?raw=true" width="3000">
</p>

<p align="center">
  <img src="https://github.com/Santiagoestremadoyro/mid-bootcamp-work/blob/main/img/sexo.png?raw=true" width="3000">
</p>


## Dataset
I used the Palmer Archipelago Penguins dataset, which contained information on the body size, sex, survival, etc of Adélie, Chinstrap, and Gentoo penguins.
The database provides a lot of data about each of the penguins, which allows us to create features in the dashboard that allow us to do a more in-depth monitoring of each of these subjects.

## Data Preparation
I cleaned and formatted the dataset by eliminating penguins with missing values in multiple columns using a query: 
```python
   {$or: [{culmen_length_mm: "NA"}, {culmen_depth_mm: "NA"}, {flipper_length_mm: "NA"}, {body_mass_g: "NA"}, {sex: "NA"}] }
```

I also determined the sex of some of the penguins using the available data.

🐧 Males are just bigger. They weigh from 4 to 5 kg and measure 45 cm. They have longer and broader beaks and a more pronounced forehead.


## Database
I stored the cleaned and formatted dataset in a MongoDB database, organized in collections based on the penguin species, sex and island where they come from.

## API
I designed an API that used different endpoints to serve data from the database. I used various parameters to allow for different types of requests, such as filtering by species, sex, or islan.

## Dashboard
I created a Streamlit dashboard that visualized the data obtained from the API. The dashboard included interactive visualizations that allowed for user interaction, such as filtering by species or sex. We used different streamlit widgets to allow for user interaction with the visualizations.

<p align="center">
  <img src="https://github.com/Santiagoestremadoyro/mid-bootcamp-work/blob/main/img/dashboard-2.png?raw=true" width="3000">
</p>


# Conclusion
This project allowed us to practice our knowledge of Python and explore a problem on our own in search of solutions. I created an API and dashboard that served and visualized data obtained from a penguin dataset that was enriched with additional information. We also cleaned and formatted the dataset, stored it in a database, and used different endpoints and parameters to allow for different types of requests. Overall, this project helped me deepen me knowledge of Python and web development.