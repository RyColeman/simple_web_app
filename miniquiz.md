Todays miniquiz is going to be visualizing a decision tree via sklearn.
Using the sklearn iris dataset...

1.  Create a decision tree classifier to classifiy each type of flower.  
2.  Then, Use pydot and graphviz to draw the decision tree to a .png image file.  

Your output should look a lot like this.
> ![](images/iris.png)

---
Here are the modules you will need to import,
```
import pandas as pd
from sklearn import tree
from sklearn.externals.six import StringIO
from sklearn.ensemble import RandomForestClassifier

#new import (possibly)
#!pip install pydot   #uncomment if you have not already installed
#!pip install graphviz   #uncomment if you have not already installed

import pydot
from sklearn.datasets import load_iris
iris = load_iris()
```
The main module you will be using is the sklearn.tree
