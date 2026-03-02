import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([[1000],[3000],[3500],[5000]])
y = np.array([120,150,175,300])

model = LinearRegression.batch()

model.fit(x,y)

New_house = np.array([[2000]])
pridicted = model.predict(New_house)

print(f"The pridicted price:{pridicted}")