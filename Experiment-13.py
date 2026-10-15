
from lab_utils import start, finish

start("program13_output.txt")

X = [(0, 0), (0, 1), (1, 0), (1, 1)]
y = [0, 0, 0, 1]

w1, w2, bias = 0.0, 0.0, 0.0
learning_rate = 0.2

for epoch in range(100):
    for (x1, x2), target in zip(X, y):
        total = w1*x1 + w2*x2 + bias
        prediction = 1 if total > 0 else 0
        error = target - prediction

        w1 += learning_rate * error * x1
        w2 += learning_rate * error * x2
        bias += learning_rate * error

print("Training results:")
for x1, x2 in X:
    total = w1*x1 + w2*x2 + bias
    prediction = 1 if total > 0 else 0
    print(x1, x2, "->", prediction)

finish()
