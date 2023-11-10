import ast
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def randomly_choosing_value_from_array(arr):
    """
    Funtion to Seperate gener type from a list of geners

    Parameters:
    - array
    """
    arr = ast.literal_eval(arr)
    if len(arr) == 0:
        return np.nan
    elif len(arr) == 1:
        return arr[0]
    else:
        return random.choice(arr)


def lineplot(x, y, xlabel, ylabel, title, color, labels):
    """
    Create a Line plot using Matplotlib's pyplot with x and y values.

    Parameters:
    - x: List of x-axis values.
    - y: List of corresponding y-axis values.
    - x_label: Label for the x-axis (default is "X-axis").
    - y_label: Label for the y-axis (default is "Y-axis").
    - title: Title of the plot (default is "Scatter Plot").
    - color: Color of Lines
    - labels: labels for the lines
    """
    plt.figure(figsize=(10, 5))
    for index in range(len(x)):
        plt.plot(x[index], y[index], label=labels[index], color=color[index])
    plt.xticks(rotation=90)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.savefig('Netflix_line_plot.jpg', dpi=500)
    plt.show()
    return


def barplot(catagories, values_set, xlabel, ylabel, title, label, color):
    """
    Create a Bar plot using Matplotlib's pyplot with x and y values.

    Parameters:
    - catagories: List of x-axis values.
    - values_set: List of corresponding y-axis values.
    - xlabel: Label for the x-axis (default is "X-axis").
    - ylabel: Label for the y-axis (default is "Y-axis").
    - title: Title of the plot (default is "Scatter Plot").
    - label: Labels for the graph type
    - color: color for the graph
    """
    x = np.arange(len(catagories))  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots(figsize=(10, 5))
    bars1 = ax.bar(x - width/2, values_set[0], width, label=label[0])
    bars2 = ax.bar(x + width/2, values_set[1], width, label=label[1])
    for bars in ax.containers:
        ax.bar_label(bars)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation=90)
    ax.set_xticks(x)
    ax.set_xticklabels(catagories)
    plt.legend()
    plt.savefig('Netflix_Bar_plot.jpg', dpi=500)
    plt.show
    return


def scatter_plot(x_values, y_values, labels, title="Scatter Plot",
                 x_label="X-axis", y_label="Y-axis"):
    """
    Create a scatter plot using Matplotlib's pyplot with x and y values.

    Parameters:
    - x_values: List of x-axis values.
    - y_values: List of corresponding y-axis values.
    - title: Title of the plot (default is "Scatter Plot").
    - x_label: Label for the x-axis (default is "X-axis").
    - y_label: Label for the y-axis (default is "Y-axis").
    """
    # Create a scatter plot
    plt.figure(figsize=(10, 5))
    for i in range(len(x_values)):
        plt.scatter(x_values[i], y_values, label=labels[i], alpha=0.6)

    # Add title and labels
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.savefig('Netflix_scatter_plot.jpg', dpi=500)
    # Show the plot
    plt.show()


def data_for_lineplot(dataframe):
    """
    Function to retrive information for the line plot

    Parameters:
    - Dataframe
    """
    imdb_score_avg = dataframe.groupby(['genres', 'release_year'])[
                    'imdb_score'].mean().reset_index()
    action_imdb = imdb_score_avg[(imdb_score_avg['genres'] == 'action')]
    war_imdb = imdb_score_avg[(imdb_score_avg['genres'] == 'war')]
    comedy_imdb = imdb_score_avg[(imdb_score_avg['genres'] == 'comedy')]
    romance_imdb = imdb_score_avg[(imdb_score_avg['genres'] == 'romance')]
    european_imdb = imdb_score_avg[(imdb_score_avg['genres'] == 'european')]
    horror_imdb = imdb_score_avg[(imdb_score_avg['genres'] == 'horror')]
    labels = ['action', 'war', 'comedy', 'romance', 'european', 'horror']
    y_values_list = [action_imdb['imdb_score'], war_imdb['imdb_score'],
                     comedy_imdb['imdb_score'], romance_imdb['imdb_score'],
                     european_imdb['imdb_score'], horror_imdb['imdb_score']]
    x_values_list = [action_imdb['release_year'], war_imdb['release_year'],
                     comedy_imdb['release_year'],
                     romance_imdb['release_year'],
                     european_imdb['release_year'],
                     horror_imdb['release_year']]
    color = ['red', 'green', 'blue', 'lightblue', 'black', 'brown']
    x_label = 'Years'
    y_label = 'Average IMDB Rating'
    titel = 'Variation In IMDB Rating For Genres From 2000 to 2020'
    lineplot(x_values_list, y_values_list, x_label, y_label,
             titel, color, labels)


def data_for_barplot(dataframe):
    """
    Function to retrive information for the Bar plot

    Parameters:
    - Dataframe
    """
    gener_type_count = dataframe.groupby(['genres', 'type'
                                          ])['show_id'].count().reset_index()
    action_type = gener_type_count[gener_type_count['genres'] == 'action']
    animation_type = gener_type_count[gener_type_count['genres'] == 'animation'
                                      ]
    crime_type = gener_type_count[gener_type_count['genres'] == 'crime']
    comedy_type = gener_type_count[gener_type_count['genres'] == 'comedy']
    drama_type = gener_type_count[gener_type_count['genres'] == 'drama']
    fantasy_type = gener_type_count[gener_type_count['genres'] == 'fantasy']
    labels = ['MOVIE', 'TV-SHOW']
    type_movie = []
    for i in range(2):
        type_movie.append([list(action_type['show_id'])[i],
                           list(animation_type['show_id'])[i],
                           list(crime_type['show_id'])[i],
                           list(comedy_type['show_id'])[i],
                           list(drama_type['show_id'])[i],
                           list(fantasy_type['show_id'])[i]])
    catagories = ['action', 'animation', 'crime', 'comedy', 'drama', 'fantasy']
    xlabel = 'Gener'
    ylabel = 'Total Shows'
    color = ['red', 'green', 'blue', 'lightblue', 'black', 'brown']
    title = "Comparision Between Sum of Tv-shows and Movies with Respect"\
         " to Genre"
    barplot(catagories, type_movie, xlabel, ylabel, title, labels, color)


def get_data_for_scatter_plot(dataframe):
    """
    Function to retrive information for the Scatter plot

    Parameters:
    - Dataframe
    """
    imdb_type_movie_score = dataframe[dataframe['type'] == "MOVIE"]
    imdb_type_movie_score_ = imdb_type_movie_score['imdb_score'][:1000]
    imdb_type_show_score = dataframe[dataframe['type'] == "SHOW"]
    imdb_type_show_score_ = imdb_type_show_score['imdb_score'][:1000]

    labels = ['MOVIE', 'SHOW']
    title = "Distribution of IMDB Rating of TV-Shows and Movies with respect"\
         " to tmdb_score"
    x_label = 'imdb_score'
    y_label = 'tmdb show score'
    scatter_plot([imdb_type_movie_score_,
                 imdb_type_show_score_],
                 dataframe['tmdb_score'][:1000], labels, title,
                 x_label, y_label)
    return

dataframe = pd.read_csv('netflix_titles.csv')
dataframe = dataframe.drop(['release_year', 'type'], axis=1)
dataframe1 = pd.read_csv('titles.csv')
dataframe = pd.concat([dataframe, dataframe1], axis=1, join="inner")
dataframe = dataframe.drop(['director', 'seasons',
                            'age_certification'], axis=1)
dataframe = dataframe.dropna()
dataframe = dataframe[dataframe[
                    'release_year'] > 2000]
dataframe["genres"] = dataframe["genres"].apply(
    randomly_choosing_value_from_array)
data_for_lineplot(dataframe)
data_for_barplot(dataframe)
get_data_for_scatter_plot(dataframe)
