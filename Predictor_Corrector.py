def predictor_corrector(f, x_0, y_0, h, N):
    x = x_0
    y = y_0
    for i in range(0, N):
        y_predictor = y + h*f(x,y)
        x = x + h
        y_corrector = y + (h/2)*(f(x,y_predictor) + f(x,y))
        y = y_corrector
    return y

#Example:
# f(x,y) = x + y
# x_0 = 0, y_0 = 1, h = 0.1, N = 10

def f(x,y):
    return x + y

x_0 = 0
y_0 = 1
h = 0.1
N = 10

print(predictor_corrector(f, x_0, y_0, h, N)) # Output: 2.105