## Assignment: 

There are a lot of great tools for building a website without knowing (or wrestling) with the quirks of HTML and CSS.  If you want to learn HTML/CSS/Javascript, Jonathan knows too much about these technologies (and teaching them) so please bug him.  If you do not care too much for HTML, there are some great graphical tools below for making a quick prototype of a front end for a site.

![asset/img](asset/Schibsted.115.png)

#### Web Interface Tools:

* [Easel.io: Browser base dinterface builder](https://www.easel.io/)
* [Divshot: Mockup editor](http://www.divshot.com/)
* [Bootswatch: Free themes for Bootstrap](http://bootswatch.com/)
* [LayoutIt: Bootsrtap GUI designer](http://www.layoutit.com/)

We Have already created much of these "products", now is the fun part to complete the process. First choose which adventure you will complete: 

### Options

* NMF
	* Expose your NMF algorithm by allowing a user to input a URL or paste in text to a text box.
	* Return the top topics/themes of the users article/document and associated words for those themes.
* Naive Bayes
	* Same as above (NMF) but return the section an article belongs to.
	* Play around with new NYT articles or articles from a completely different publication/text.
* Recommender
	* Expose your recommender such that a user can input an Amazon product, and you tell them similar products.
* A/B
* Clustering
* Hadoop++
	* Train your Naive Bayes algorithm on a massive amount of data (Wikipedia or Common Crawl) in S3 with EMR.
	* Expose your trained model with the Flask web app.
* other

### Implementation

You can choose to implement whatever you want for this mini-project but you will have to present what you build tomorrow morning.  Ideally the class could access you application and play around with it themselves.  Take this as a chance to finish up one of the old assignments to completion as well as an opportunity to get experience with web technologies.  Whichever project you choose to implement, the following steps will be somewhat universal.  We will be using Flask to create our application.

__NOTE: You do not need to build an application with a front-end.  You can simply build an API that exposes your model, i.e. `curl --data text="Awesome new article abou..." http://api.mymodel.com/bayes`__

1. Play with a Machine Learning API on Mashape.  This will let you know what type of abstraction to create.  Here is one for NLTK: [https://www.mashape.com/japerk/text-processing](https://www.mashape.com/japerk/text-processing)

2. First read through this 'hello world' of Flask: [ReSTful API](http://blog.luisrei.com/articles/flaskrest.html)

3. Now hopefully you are a bit more familiar with the way the web works.  For our application there are a few requirements:

* Model training (offline)
* User input (i.e. article to classify)
* Prediction/analysis
* Return results
* Make it pretty?

4. You may already have a trained model (or analyses) that you want to expose to the world via an API.  First we need to serialize our model parameters.  For Naive Bayes this means our CPTs and Prior table.  For the recommender it will be the similarity matrix.  For NMF you will have to run the algorithm every time someone inputs data.  Serialize your parameters/model using [pickle](http://scikit-learn.org/stable/tutorial/basic/tutorial.html#model-persistence) to a flat file, or serialize your parameters (i.e. CPT tables for Naive Bayes) to a hosted database (this will allow you to access your model in the cloud):

* [Heroku Postgres](https://addons.heroku.com/heroku-postgresql)
* [MongoLab](https://mongolab.com/welcome/)
* [EC2](http://aws.amazon.com/ec2/)

5. Now that we have our model serialized, we are ready to start exposing it.  We will not worry about a front end right now.  We need to setup routes for our app.  We need:

* POST -- user submits new data classify/recommend/etc., you return a label/recommendation/etc.
* GET -- accept no data, simply return instructions for the API (routes list, data format, etc.) 

Test your API locally on your laptop before sending it up to the cloud.  Make sure your GET and POST routes work.

6. For the POSTing of new data, you will accept user input in a somewhat raw form (text, URL, HTML, etc.).  In your web app you will need to scrub and transform this data to get it into a suitable form for classification.  Remember the layer cake!

![asset/Datado.087.png](asset/Datado.087.png)

7. Once you have the new input data in a properly vectorized form, you can run it through your model.  Write code in your Flask route to read in data from the database contianing the model parameters.  Predict the new label for the user input.  Return this in a [Response](http://flask.pocoo.org/docs/api/#flask.Response) object as JSON.

8. Now that you know your model works locally on your laptop, it is time to send it to the cloud!  You should already have an EC2 account setup.  Follow this [guide](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-instance_linux.html) to setup a virtual server.  Things to watch out for:
    * Be sure to chose the AMI image with scikit-learn on it: __ami-765b3e1f__.
    * Configure security groups to open the port your Flask app is running on.
    * Remember to log in with user: ubuntu

9. Connect to your server deploy your app.  If you need any additional help, please refer back to the AWS [sprint](https://github.com/zipfian/aws-and-the-cloud).  Gotchas:
    * Permission on your key file: chmod 400
    * scp your pickled model to your server
    * make sure flask is installed on your EC2 machine

![architecture](https://s3.amazonaws.com/heroku.devcenter/manual_uploads/Screen%20shot%202012-04-12%20at%203.59.12%20PM.png)

#### Example: Twitter sentiment app

__Web Process: Flask app__
__Background Service: scikit model__
__External Service: Twitter API you call out to__

10. You application will not have an interface (yet).  Here you can build one using some of the tools listed above.  Or you can leave your app simply as an API.  Once deployed to the cloud, use `curl` (or another HTTP library) to POST data to your application and hopefully it responds with a label/recommendation/etc.

__WARNING: Memory might be an issue with Heroku or other free hosting.  If you need more, I would recommend just using EC2__

10. $$$

![squidward](http://media.giphy.com/media/SsTcO55LJDBsI/giphy.gif)

## Extra

Now that you have felt the pain of deploying a model with EC2, use [yHat](http://yhathq.com/) to deploy your same model.  You will still need your Flask app to expose you model via the web, but now instead of dealing with pickling your model, transferring files to EC2, etc., you can simply deploy your model to yHat.  Their blog and site have excellent tutorials which you can follow along with.
