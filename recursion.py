#Justin Volckmar 100701687
import math

#Utilizes two function pointers (F and DF) for Newtonian nonlinear equation "solver"
#Computes sequence with initial point; x0, max iterations; kmax, error tolerance; tolerr, residual tolerance; tolres.
#k=1 because by default its just a counter but it needs to be passed and increase as it recurses.
def recursion(F,DF,x0,tolres,tolerr,kmax,k=1):
    x = x0                                            # Initialize the approximate solution.
    conv = 0                                          # By default set the convergence flag to 0 (false).
    dx = -F(x)/DF(x)                                  # Compute update step.
    x = x + dx                                        # Apply update step.
    err = abs(dx)                                     # Estimate error.
    res = abs(F(x))                                   # Compute residual.
    print('i: %d, approx. x: %e, error: %e, residual: %e' % (k,x,err,res)) # Print current iteration values
    if err < tolerr and res < tolres:                 # Check for convergence.
        conv = 1                                      # Flag convergence.
        print('Final approx. solution: %e after %d iterations with %e error and %e residual.' % (x,k,err,res))
        return x,err,res
    elif k == kmax:                                     # if no convergence after kmax iterations print warning.
        print('No convergence was reached in %d iterations!' % (kmax))
        print('Final approx. solution: %e after %d iterations with %e error and %e residual.' % (x,k,err,res))
        return x,err,res
    else:
        return recursion(F,DF,x,tolres,tolerr,kmax,k+1)

#Prove existance for any initial point x0 on (0,2]. x_k = g(x_k-1) converges to x*.
#with g(x) = (sin(pi * x) / (2 * pi)) - ((x^2) / (2 * pi)) + (x) 
def g(x):
    return (math.sin(math.pi * x) - math.pow(x,2) / (2 * math.pi) + x) 
#and g'(x) = (cos(pi * x) - (x / pi))
def gp(x):
    return (math.cos(math.pi * x) - x / math.pi)

func = g
der = gp
error_tol = 1E-6
residual_tol = 1E-6
max_iters = 20

#loop for 20 values of (0,2] to show convergence to point x*
#in this case, this function converges to 2 different points. 6.807 and 5.308.
init = 0.1
while init <= 2:
    recursion(func,der,init,residual_tol,error_tol,max_iters)
    init += 0.1

#initial point x0 = 0
print('init=0')
init = 0
recursion(func,der,init,residual_tol,error_tol,max_iters)

#initial point of x0 = 0: immidiately terminates the program as expected
#because convergence is reached at x0 = 0 as it is an intersection
# of sin(pi * x) = x^2 (given g(x) = x or f(x) = 0)

#initial point x0 < 0 (x0=-0.4)
print('init=-0.4')
init = -0.4
recursion(func,der,init,residual_tol,error_tol,max_iters)

#initial point of x0 < 0: reaches solution after 16 iterations with
#1E-6 tolerances, still computes just fine with other various values 
#because the absolute value of dx and F(x) is taken for error and residual