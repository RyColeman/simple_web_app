## Overview -- Data Products: Web apps with [Flask](http://flask.pocoo.org/) (mini-project)

Throughout the course we have been working with parsing data, tranforming text, building models, statistically validating our results, etc., etc., etc.  This has been much work and it might have been hard to see where it all was leading.  This sprint is designed to tie everything together, and after all, your best insight/model is only as good as your capacity to share it with the world!

In this sprint we will be taking one of our previous analyses and getting one online for the world to interact with. 

### Example Data Science workflow:
1. Run a scraper on an AWS EC2 instance to download NYT articles.
2. Store these articles intermediately on the EC2 machine (possibly in a database) for some querying and processing.
3. Batch upload a database dump to S3 periodically (as your database fills up).
4. Use Mortar (with Pig or Python) to locally (on your laptop) experiment with your data and build a model on a subset of the data.
5. Train a model at scale over all of your data located in S3 (Mortar runs in production on EC2 instances)
6. Serialize your trained model parameters to MongoDB (or [DynamoDB](http://aws.amazon.com/dynamodb/)) using the proper Pig [adapters](http://help.mortardata.com/reference/loading_and_storing_data/MongoDB).
7. (Optional) Deserialize trained model parameters from MongoDB into a Python [class](http://blog.yhathq.com/posts/image-classification-in-Python.html) (or [R function](http://blog.yhathq.com/posts/recommender-system-in-r.html)) and deploy to [yHat](http://yhathq.com/docs/quickstarts/py).
8. Write a simple web application with [Flask](http://flask.pocoo.org/) to expose your model to the world. This is essential to capture input from users and also provide output from your model.  In our case, this could be as simple as a form to input a url to an article, and provide the user back with the section of the NYT it should belong to.
9. If your model is deployed to yHat you simply use their API (and wrapper functions) and call it directly from the Flask application. Otherwise you need to query your MongoDB for your model parameters, deserialize these into a model class in Python (or R) and run your model's predict() function using the user's input.  Respond with the result of the prediction (HTTP response or HTML page).
10. [Deploy](http://ryaneshea.com/lightweight-python-apps-with-flask-twitter-bootstrap-and-heroku) your web application to [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)

__We are somewhere near step #6__

## Reading

* Agile Data: p. 38-54
* [Pete Skomoroch: Data Exhaust](http://www.slideshare.net/pskomoroch/distilling-data-exhaust)
* [Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)


## References

* [API design with Flask](http://blog.luisrei.com/articles/rest.html)
* [Flask + Bootstrap + Heroku](http://ryaneshea.com/lightweight-python-apps-with-flask-twitter-bootstrap-and-heroku)
* [Flask-restful](http://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful)
