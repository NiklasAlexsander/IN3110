import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn import metrics
import data

def fit(training_set, classifier_type, list_of_features, targeted_column):
    """
    Fitting a given set with a given classifier, features and targeted column.
    KNN: n_neighbors=1
    SVC: gamma='scale'
    LR: solver='lbfgs', max_iter=200
    
        args:
            training_set (pandas DataFrame): the DataFrame to fit the features
            classifier_type(string): The classifier to be used
            list_of_features(list:string): List containing all the features to be fitted
            targeted_column(string): column to compare. (contains classes to check if right or wrong)

        return:
            classifier(sklearn.classification.(KNN|SVC|LR)): a fitted classifier. Could be either (KNN,SVC or LR)
    """
    if classifier_type == 'KNN':
        classifier = KNeighborsClassifier(n_neighbors=1)
    elif classifier_type == 'SVC':
        classifier = SVC(gamma='scale')
    elif classifier_type == 'LR':
        classifier = LogisticRegression(solver='lbfgs', max_iter=200)
    else:
        raise ValueError("classifier")
    for x in (list_of_features + [targeted_column]):
        if x not in training_set.columns:
             raise ValueError(f"{x} not a col")
    classifier.fit(training_set[list_of_features],
		   training_set[targeted_column].values.ravel())

    return classifier

if __name__ == '__main__':
    feature_bundle =    [['glucose', 'pregnant', 'mass', 'age'],
                        ['triceps', 'pedigree','pregnant'],
                        ['pregnant','glucose','triceps','insulin','mass','pedigree','age']]
    targeted_column = 'diabetes'

    data_frame, training_set, validation_set = data.diabetes_dataset()

    for features in feature_bundle:
        print("feature_set: ", features)
        #Testing
        for x in ['KNN', 'SVC', 'LR']:
            trained_classifier = fit(training_set, x, features, targeted_column)
            prediction = trained_classifier.predict(validation_set[features])
            print(f"{x}: ", metrics.accuracy_score(validation_set[targeted_column], prediction)
        print("\n\n")
