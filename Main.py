# %%
# Importing libraries   
import numpy as np
import matplotlib.pyplot as plt
import Module1
import importlib


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


# %%
importlib.reload(Module1)
# Calling results function to get outputs for the solution to the ode for varying lambda values
ode_results = Module1.results(time_steps, t_array, lambda_steps, lambda_array, x_0)
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


