def newton_forward_difference_interpolation(x, y): 
    n = len(x) 
    # Calculating the forward difference table 
    forwardDiff = [[0 for i in range(n)] 
                      for j in range(n)] 
  
    for i in range(n): 
        forwardDiff[i][0] = y[i] 
  
    # Calculating the forward difference table of order n-1 
    for i in range(1, n): 
        for j in range(n - i): 
            forwardDiff[j][i] = (forwardDiff[j + 1][i - 1] -
                                 forwardDiff[j][i - 1]) / (x[i + j] - x[j]) 
   
    value = float(input("Enter the value of x for which we have to interpolate: ")) 
  
    sum = forwardDiff[0][0] 
  
    # Calculating the value of y using forward difference table 
    for i in range(1, n): 
        term = 1
        for j in range(i): 
            term = term * (value - x[j]) 
        sum = sum + (forwardDiff[0][i] * term) 
  
    # Displaying the value of interpolated variable 
    print("Value at",value,"is",sum) 
 
x = [0, 1, 2, 3] 
y = [-3, 6, 8, 12] 
  
newton_forward_difference_interpolation(x, y) 