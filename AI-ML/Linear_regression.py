# Linear regression tutorial in .py

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Let's declare some fake data first. Let's say that x is an engine displacement in liters and y is it's horsepower.

x=np.array([0.8,1.0,1.1,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0]).reshape((-1,1))
y=[50,63,55,86,90,115,106,125,140,90,130]

# Let's visualise it first. 

plt.figure()
plt.scatter(x,y)
plt.show()

# Looks like that's we can use linear regression here.

LRmodel=LinearRegression()
LRmodel.fit(x,y)

# Let's check the properties of our model.

r_sq = LRmodel.score(x,y)
b0 = LRmodel.intercept_
b1 = LRmodel.coef_

print("This is our linear model: \n f(x) = " + str(b0) + " + " + str(b1[0]) + " x\n It's R squared is equal to " + str(r_sq) + " which is a decent score.")

# We can also predict using that model. So let's check the y for x=1.75

prediction = LRmodel.predict(np.array([1.75]).reshape((-1,1)))
print("For x=1.75 y equals " + str(prediction))

# Let's check how this model behawes with our training data (x array declared at the beggining)...

model_prediction = LRmodel.predict(x)

# ... and let's show it on a plot.
plt.figure()
plt.scatter(x,y)
plt.plot(x,model_prediction)
plt.show()

# So it looks like this model is good when we are considering it's quality using r squared and our plot.

# Please note that you can provide more dimensions in x array, logistic regression could be more complex. 