# Dependencies
import numpy as np

# Function that evalutes the solution to the ODE (x(t) = e^(lambda*t) * x(0))
# Parameters: array with values of t, array with lambda values, number of iterations - number of values 
def ode_solve(time, lambda_val, steps, initial_condition):
    x_t = np.zeros(steps)

    for i in range(0, steps):
        x_t[i] = np.exp(time[i]*lambda_val) * initial_condition
    return x_t

# Function that calls 'ode_solve' for each value of lambda and returns a matrix with the outputs of all lambda values
# Parameters: number of iterations - number of values of lambda, array with lambda values
def results(time_steps, time_vals, lambda_steps, lambda_vals, initial_condition):
    ode_arrays = np.zeros((5,6)) # dimensions are hard coded, would be nice to make dynamic based off of input arrays

    for i in range(0, lambda_steps):
        ode_arrays[i] = ode_solve(time_vals, lambda_vals[i], time_steps, initial_condition)

    return ode_arrays