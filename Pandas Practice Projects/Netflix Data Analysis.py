
# Netflix Data Analysis (Advanced)

# Questions
# Movies vs TV shows count
# Most common genres
# Top producing countries
# Content added each year
# Longest movie

import pandas as pd 

net_data = pd.read_csv("netflix_titles.csv")
print(net_data.head(5))

#Movies vs TV shows count

print('='*25)
print("IPL CRICKET ANALYSIS")
print('='*25)

print("\nNumber Of Movies and Tv Shows: \n",net_data["type"].value_counts())

#Most common genres

print('='*25)
print("MOST COMMON GENERS")
print('='*25)

genre_column = 'listed_in'

top_genre = (
    net_data[genre_column]
    .dropna()                      # Drop missing values
    .str.split(', ')               # Split comma-separated string into Python lists
    .explode()                     # Flatten the lists into separate rows
    .value_counts()                # Count occurrences of each individual genre
)

# most_common_genre = top_genre.idxmax()
# print("Most Common Genre: \n",most_common_genre)
print("\nTop Most Common Genres: \n", top_genre.head(5))

#Top Producing Countries 

print('='*25)
print("TOP PRODUCING COUNTRIES")
print('='*25)

top_country = (
    net_data['country']
    .dropna()                      # Drop missing values
    .str.split(', ')               # Split comma-separated string into Python lists
    .explode()                     # Flatten the lists into separate rows
    .value_counts()                # Count occurrences of each individual genre
)

print("\nTop Producing Countries: \n",top_country.head(5))

#Content Added Each year

print('='*25)
print("TOP PRODUCING COUNTRIES")
print('='*25)

net_data["date_added"] = net_data["date_added"].str.strip()
net_data["date_added"] = pd.to_datetime(net_data["date_added"])
net_data["Year_Added"] = net_data["date_added"].dt.year

# net_data.groupby('year_added')['title'].count()
content_per_year = (
    net_data.groupby("Year_Added")["title"]
      .count()
)

print("\nNumber of Content Added Each Year: \n",content_per_year)

#Longest Movie

print('='*25)
print("TOP PRODUCING COUNTRIES")
print('='*25)


movies = net_data[net_data["type"] == "Movie"]
movies = movies.dropna(subset=["duration"])
tv_shows = net_data[net_data["type"] == "TV Show"]

# movies["duration_minutes"] = (
#     movies["duration"]
#     .str.extract(r"(\d+)")
#     .astype(int)
# )

movies["duration_minutes"] = (
    movies["duration"]
    .str.replace(" min", "", regex=False)
    .astype(int)
)

longest_movie = movies.loc[movies["duration_minutes"].idxmax()]
print(longest_movie)
