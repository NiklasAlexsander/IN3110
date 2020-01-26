import matplotlib
matplotlib.use("TkAgg") #Need to have this line to stop python from crashing. Believe it's a bug with the newer versions of python
from flask import Flask, render_template, request
from sklearn import metrics
from io import BytesIO
import data, fitting
import visualize
import base64
import os

app = Flask(__name__)
app.secret_key = b'_5#3qdas_-_]0+/3G' #random key

@app.route('/')
def start():
    """
    Starting template of the 'server' when running 'web_visualization.py'.

        return:
            render_template('INSERT-HTML-PATH') (render-function): renders the given html.
    """
    return render_template('web.html')

@app.route('/handle_features', methods=['POST'])
def handle_feature_1():
    """
    Handles the button-action from submitting checkbox-choices.

    The returns will render the given html, while the arguments given will 'send'
    variables to the html-file.
    If two checkboxes are marked, the return function will be given some file-paths
    for displaying three different scatterplots corresponding to the given parameters,
    as well as the validation accuracy and the training accuracy.
    If 1-7 hitboxes are checked (except 2) the return will only be given two parameters, the
    validation accuracy and the training accuracy.
    In any other instance the return will only return to the default html 'web.html'

        returns:
            render_template('INSERT-HTML-PATH',args) (render-function): renders the given html.
            OR
            render_template('web.html') (render-function): renders the 'standard'-html.
    """
    if request.method == 'POST':
        classifier = request.form['classifier']
        features_checkbox = request.form.getlist('features_checkbox')
        targeted_column = 'diabetes'

        if len(features_checkbox) == 0:
            message = 'ERROR: Please pick between 1-7 features'
            return render_template('web.html', error_message = message)
        else:
            t_ac, v_ac, img1, img2 = picture_prosess(features_checkbox, targeted_column, classifier)
            if img1 is not None and img2 is not None:
                return render_template('web.html', name = 'classifier validation',
                                                   url1 = 'static/web_visualization.png',
                                                   url2 = f'data:image/png;base64,{img1}',
                                                   url3 = f'data:image/png;base64,{img2}',
                                                   training_accuracy = t_ac,
                                                   validation_accuracy = v_ac)

            else:
                return render_template('web.html', training_accuracy = t_ac,
                                                   validation_accuracy = v_ac)
    else:
        return render_template('web.html')

@app.route('/help_page')
def help_page():
    """
    Handles the link to the help page.

        Return:
            render_template('docfiles/Assignment6_web_help.html'): renders Assignment6_web_help.html
    """
    return render_template('docfiles/Assignment6_web_help.html')

@app.route('/data.html')
def data_page():
    """
    Handles the link to the help page of 'data.py'.

        Return:
            render_template('docfiles/data.html'): renders data.html
    """
    return render_template('docfiles/data.html')

@app.route('/fitting.html')
def fitting_page():
    """
    Handles the link to the help page of 'fitting.py'.

        Return:
            render_template('docfiles/fitting.html'): renders fitting.html
    """
    return render_template('docfiles/fitting.html')

@app.route('/visualize.html')
def visualize_page():
    """
    Handles the link to the help page of 'visualize.py'.

        Return:
            render_template('docfiles/visualize.html'): renders visualize.html
    """
    return render_template('docfiles/visualize.html')

@app.route('/web_visualization.html')
def web_visualization_page():
    """
    Handles the link to the help page of 'web_visualization.py'.

        Return:
            render_template('docfiles/web_visualization.html'): renders web_visualization.html
    """
    return render_template('docfiles/web_visualization.html')



def picture_prosess(features, targeted_column, classifier):
    """
    Calls upon data.diabetes_dataset() and fitting.fit() to predict and calculate
    accuracy to be displayed on the web-page. Visualize.visualizer() will also be
    called if only two checkboxes are checked.

    The scatterplots are saved in buffers to avoid problems with matplotlib, flask,
    and python. There has been some problems occurring testing (Mac) with all
    the latest updates to the packages. Without the buffers the scatterplots would not
    be updated in real time when checking new checkboxes without having to restart
    the page. Since the scatterplots should only be displayed when 2 checkboxes are
    marked, the whole buffer and scatter-plot action is inside an if-statement.

        args:
            features (list:String): list containing names of features(columns)
            targeted_column (String): name of column
            classifier (String): name of classifier

        returns:
            t_ac (float):
            v_ac (float):
            img1 (string): scatter plot object 1
            img2 (string): scatter plot object 2
    """
    data_frame, training_set, validation_set = data.diabetes_dataset()
    trained_classifier = fitting.fit(training_set, classifier, features, targeted_column)

    img1 = None
    img2 = None

    prediction1 = trained_classifier.predict(training_set[features])
    t_ac = metrics.accuracy_score(training_set[targeted_column], prediction1)

    prediction2 = trained_classifier.predict(validation_set[features])
    v_ac = metrics.accuracy_score(validation_set[targeted_column], prediction2)

    if(len(features) == 2):
        buf = BytesIO()
        #add to buffer
        (visualize.visualizer(prediction1, training_set, features)).savefig(buf, format="png")
        img1 = base64.b64encode(buf.getbuffer()).decode("ascii")

        buf = BytesIO()
        #add to buffer
        (visualize.visualizer(prediction2, validation_set, features)).savefig(buf, format="png")
        img2 = base64.b64encode(buf.getbuffer()).decode("ascii")

    return t_ac, v_ac, img1, img2

if __name__ == '__main__':
    """
    features = ['glucose', 'pregnant', 'mass', 'age']
    targeted_column = 'diabetes'

    data_frame, training_set, validation_set = data.diabetes_dataset()

    trained_classifier = fitting.fit(training_set, 'KNN', features, targeted_column)
    prediction = trained_classifier.predict(training_set[features])
    t_ac = metrics.accuracy_score(training_set[targeted_column], prediction)
    prediction = trained_classifier.predict(validation_set[features])
    v_ac = metrics.accuracy_score(validation_set[targeted_column], prediction)
    """

    os.system(r'pydoc -w Assignment6_web_help')
    os.system(r'pydoc -w web_visualization')
    os.system(r'pydoc -w data')
    os.system(r'pydoc -w fitting')
    os.system(r'pydoc -w visualize')
    os.system(r'mv *.html templates/docfiles')
    app.run(debug=True)
