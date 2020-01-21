#Justin Volckmar 100701687
import math

#Utilizes two function pointers (F and DF) for Newtonian nonlinear equation "solver"
#Computes sequence with initial point; x, max iterations; N, residual tolerance; tolres.
def steffensen(F,DF,x,tolres,N):
    y1 = x                                                    # Initialize the approximate solution.
    conv = 0                                                  # By default set the convergence flag to 0 (false).
    for k in range(1,N+1):
        y1 = x                                    # Loop over Newton iterations.
        dx = -F(y1)/DF(y1)                                    # Compute update step with y1.
        y2 = y1 + dx                                          # Apply update step y2.
        dx = -F(y2)/DF(y2)                                    # Compute update step with y2.
        y3 = y2 + dx                                          # Apply update step y3.
        x = y1 - (math.pow((y2-y1),2) / (y3 - (2 * y2) + y1)) # update x to new approximation.                                                # 
        res = abs(F(x))                                       # Compute residual.
        print('iteration: %d, approx. x: %e, residual: %e' % (k,x,res)) # Print current iteration values
        if res < tolres:                     # Check for convergence.
            conv = 1                                      # Flag convergence.
            break                                         # Exit loop.
    if conv == 0:                                         # if no convergence after kmax iterations print warning.
        print('No convergence was reached in %d iterations!' % (N))
    print('Final approx. solution: %e after %d iterations with %e residual.' % (x,k,res))
    return x,res

#Prove existance for any initial point x0 on (0,2]. x_k = g(x_k-1) converges to x*.
#with g(x) = 
def g(x):
    return (math.exp(-(x**2) + x) - x/2 - 1.0836)
#and g'(x) = 
def gp(x):
    return (math.exp(-(x**2) + x)*(-2*x + 1) - (1/2))

func = g
der = gp
residual_tol = 1E-6
max_iters = 20
init = 1
steffensen(func,der,init,residual_tol,max_iters)