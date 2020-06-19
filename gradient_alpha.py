weight = 0.5
goal_prediction = 0.8
input = 1
alpha = 0.9

for iteration in range(20):
    prediction = input * weight
    error = (prediction - goal_prediction)** 2
    derivative = input * (prediction - goal_prediction)
    weight = weight - (derivative * alpha)
    print("Error:  " + str(error) + "  Prediction:  " + str(prediction))
