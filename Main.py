# %%
# Importing libraries
import numpy as np
import matplotlib.pyplot as plt


# %%
# Part A
# ODE: x' = lambda*x, initial condition: x(0) = 2
# Solution to ODE: x(t) = e^(lambda*t) * x(0)

# Defined parameteres
x_0 = 2 # Initial Condition
t_array = ([0, 1, 2, 3, 4, 5]) # t = 0, 1, 2,..,5
lambda_array = ([-5, -1, 0, 0.01, 0.1]) # lambda = -5, -1,..,0.1
lambda_steps = len(lambda_array) # Number of iterations needed to loop through lambda values (n lambda values)
time_steps = len(t_array) # Number of iterations needed to loop through the values of t 

# Function that evalutes the solution to the ODE (x(t) = e^(lambda*t) * x(0))
# Parameters: array with values of t, array with lambda values, number of iterations - number of values t
def ode_solve(time, lambda_val, steps):
    x_t = np.zeros(steps)

    for i in range(0, steps):
        x_t[i] = np.exp(time[i]*lambda_val) * x_0
    return x_t

# Function that calls 'ode_solve' for each value of lambda and returns a matrix with the outputs of all lambda values
# Parameters: number of iterations - number of values of lambda, array with lambda values
def results(lambda_steps, lambda_vals):
    ode_arrays = np.zeros((5,6)) # dimensions are hard coded, would be nice to make dynamic based off of input arrays

    for i in range(0, lambda_steps):
        ode_arrays[i] = ode_solve(t_array, lambda_vals[i], time_steps)

    return ode_arrays


# %%
# Calling results function to get outputs for the solution to the ode for varying lambda values
ode_results = results(lambda_steps, lambda_array)
print(ode_results)

# %%
# Plotting x(t) outputs that were calculated above
# Parameters: array with time values, elements from ode_results matrix
x = t_array

fig, ax = plt.subplots()
ax.plot(x, ode_results[0], label='lambda 1')
ax.plot(x, ode_results[1], label='lambda 2')
ax.plot(x, ode_results[2], label='lambda 3')
ax.plot(x, ode_results[3], label='lambda 4')
ax.plot(x, ode_results[4], label='lambda 5')
ax.set_xlabel('Time')
ax.set_ylabel('x(t)')
ax.set_title('x(t) for varying lambda values at each time t')
ax.legend()
plt.show()


