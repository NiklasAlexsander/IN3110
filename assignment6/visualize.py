import fitting
import data
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


def visualizer(prediction, df, feature_set, classifier=None):
    """
    Makes a scatterplot with a given DataFrame, feature set and its predictions.

    In the same fashion as the plotting in data.

    Tried to make colored areas where the predictions direct the colors and borders.
    The code in the docstring is two of my attempts trying to achieve this.

        args:
            prediction (list:string): containing predictions as strings
            df (pandas DataFrame): Containing data to be plotted
            feature_set (pandas DataFrame): features to be plotted
            classifier (sklearn.Classifier): trained classifier

        return:
            plt (matplotlib:scatter plot): scatter plot object

    """
    for x in feature_set:
        if x not in df.columns:
             raise ValueError(f"{x} not a col")
    if len(prediction) != df.shape[0]:
        raise ValueError("row count does not match")
    if len(feature_set) == 2:
        colors = {'pos': '#793A95', 'neg': '#F4365B'}
        #colors = {'pos': 'blue', 'neg': 'red'}
        #cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA'])
        #cmap_bold = ListedColormap(['#FF0000', '#00FF00'])
        plt.clf() #Resets plots

        """
        #I am not able to get pcolormesh to work as intended.
        #Here are two versions.
        #Version1:
        X = df

        x_min, x_max = X[feature_set[0]].min() - .1, X[feature_set[0]].max() + .1
        y_min, y_max = X[feature_set[1]].min() - .1, X[feature_set[1]].max() + .1
        xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                             np.linspace(y_min, y_max, 100))
        Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)


        #plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

        #plt.scatter(X[feature_set[0]], X[feature_set[1]], c=y, cmap=cmap_bold)
        #plt.axis('tight')
        """
        """
        #Version 2:
        test = []
        for e in prediction:
            if e == 'pos':
                test.append(1)
            else:
                test.append(0)

        test = np.array(test)

        #plt.pcolormesh(np.expand_dims(x,0), np.expand_dims(y,1), test*np.eye(len(prediction)))
        """
        for idx, row in df.groupby('diabetes'):
            plt.scatter(row[feature_set[0]], row[feature_set[1]], c=[colors[r] for r in row['diabetes']], label=idx)

        plt.xlabel(feature_set[0])
        plt.ylabel(feature_set[1])
        plt.legend(title="Diabetes")

        return plt


if __name__ == '__main__':
    features = ['glucose','pressure']
    targeted_column = 'diabetes'

    data_frame, training_set, validation_set = data.diabetes_dataset()

    trained_classifier = fitting.fit(training_set, 'KNN', features, targeted_column)
    prediction = trained_classifier.predict(validation_set[features])
    sctplt = visualizer(prediction, validation_set, ['glucose','pressure'],trained_classifier)

    sctplt.show(block=True)
