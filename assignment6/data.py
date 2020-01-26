import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def diabetes_dataset():
    """
    Reads the file diabetes.csv with pandas, and creating a training and validation set.

    The function will remove any rows with NA values.
    The training set includes 80 percent of the data from diabetes.csv, while the rest
    is included in the validation set.

        returns: data_frame (pandas DataFrame): diabetes dataset
                 training_set (pandas DataFrame): training set
                 validation_set (pandas DataFrame): validation set
    """
    data_frame = pd.read_csv('diabetes.csv',sep=',')
    data_frame = data_frame.dropna()

    pos_frame = data_frame[data_frame.diabetes == 'pos']
    neg_frame = data_frame[data_frame.diabetes == 'neg']

    percentage_pos_rounded = round(len(pos_frame.index)/100*80)
    percentage_neg_rounded = round(len(neg_frame.index)/100*80)

    training_set = pd.merge(pos_frame[:round(percentage_pos_rounded)], neg_frame[:round(percentage_neg_rounded)], how="outer")
    validation_set = pd.merge(pos_frame[round(percentage_pos_rounded):], neg_frame[round(percentage_neg_rounded):],how="outer")

    return data_frame, training_set, validation_set

def scatter_plot_diabetes_2_dimentions(df,feature_1,feature_2, colors=None):
    """
    Makes a scatter-plot with the given dataframe, features and colors.

    Iterates through the given dataframe, looking at the features compared to
    'diabetes' column, and color the classes differently. the different classes
    are saved in a legend.

        args:
            df (pandas DataFrame): DataFrame to collect values from.
            feature_1 (string): the name of the first column
            feature_2 (string): the name of the second column
            colors=None (Dictionary): class name as key, color as value
    """
    if colors == None:
        colors = {'pos': '#793A95', 'neg': '#F4365B'}

    for idx, row in df.groupby('diabetes'):
        plt.scatter(row[feature_1], row[feature_2], c=[colors[r] for r in row['diabetes']], label=idx)

    plt.xlabel(feature_1)
    plt.ylabel(feature_2)
    plt.legend(title="Diabetes")
    plt.show(block=True)


if __name__ == '__main__':
    data_frame, training_set, validation_set = diabetes_dataset()
    diff_color = {'pos': '#fcba03', 'neg': '#03fca5'}
    scatter_plot_diabetes_2_dimentions(data_frame,'glucose','pressure')
    scatter_plot_diabetes_2_dimentions(training_set,'pregnant','age',diff_color)
    scatter_plot_diabetes_2_dimentions(validation_set,'mass','triceps')
