# How to build a text classifier web app.  
Today we are going to train a model, build a web interface that allows people to submit data, send that data to our model, make a prediction on it, then return the results.

##### This is how your app directory should look.  
```
MyProject/
|-- my_app/
|   |-- app.py
|   |-- build_model.py
|   |-- data
|   |   |-- articles.csv
|   |   |-- model.pkl
|   |   |-- vectorizer.pkl
```

## Step 1: Build your model

***This exercise isn't about model tuning, so just build a basic model and don't worry about tuning it.***

1. In `build_model.py`, build a text classifier model using the `articles.csv` dataset. You can use the `body` field to get the text and use it to predict the `section_name`.

    You should save the model as a pickle file. The template for this code is in [build_model.py](my_app/build_model.py).

2. Check that you can reload your model and vectorizer by running these lines of code:

    ```python
    import cPickle as pickle
    import pandas as pd

    with open('data/vectorizer.pkl') as f:
        vectorizer = pickle.load(f)
    with open('data/model.pkl') as f:
        model = pickle.load(f)

    df = pd.read_csv('data/articles.csv')
    X = vectorizer.transform(df['body'])
    y = df['section_name']

    print "Accuracy:", model.score(X, y)
    print "Predictions:", model.predict(X)
    ```

## Step 2:  Build your site

You can use the [word count form example](examples/example_with_form.py) as a guide.

1. In the `app.py` file, build a welcome homepage. It should have a link to a `/submit` page.

2. Build the `/submit` page as an html form which accepts text data.

3. Build the `/predict` page which will display the result of the model prediction.
