# csci2072u lab01
1a)
f(x) = (sin(pi * x) - x^2) = 0
so sin(pi * x) = x^2, where a solution x* can be found to both functions such that f(x*) = 0.
sin(pi * 0) = 0^2 --> sin(0) = 0 --> (0 = 0); x* = 0, the point of intersection between the curves of sin(pi * x) and x^2 is 0.

1b)
given g(x) = x, f(x) = 0, and g(x) = [sin(pi * x) / (2*pi)] - [x^2/(2*pi)] + x
x (-x) = [sin(pi * x) / (2*pi)] - [x^2/(2*pi)] + x (-x)
0 = [sin(pi * x) / (2*pi)] - [x^2/(2*pi)]
0 = [sin(pi * x) - x^2]/(2*pi) where f(x) = (sin(pi * x) - x^2) from 1a)
0 * (2*pi) = [f(x) / (2*pi)] * (2*pi)
so f(x) = 0

1cd) see iteration.py and recursion.py for code.
The solutions found using the newton method over 20 tests within (0,2] were 5.308121 and 6.807632.

1e) When x0 = 0, the function will immediately terminate after running 1 iteration
as the residual and error (both 0) are lower then the tolerance. 
When x0 < 0, the function still works and approximates the solution as though it was positive,
this is due to the absolute values used to compute residual and error.

2a) see steffensen.py for code.

2b)
steffensen.py:
iteration: 1, approx. x: 3.546001e-01, residual: 3.735449e-03
iteration: 2, approx. x: 3.006332e-01, residual: 7.347056e-05
iteration: 3, approx. x: 3.074036e-01, residual: 3.268170e-05
iteration: 4, approx. x: 3.058879e-01, residual: 1.750423e-07
Final approx. solution: 3.058879e-01 after 4 iterations with 1.750423e-07 residual.

iteration.py:
iteration: 1, approx. x: 6.109333e-01, error: 3.890667e-01, residual: 1.207459e-01
iteration: 2, approx. x: 4.564079e-01, error: 1.545255e-01, residual: 3.021620e-02
iteration: 3, approx. x: 3.785844e-01, error: 7.782351e-02, residual: 7.656717e-03
iteration: 4, approx. x: 3.388631e-01, error: 3.972124e-02, residual: 1.916870e-03
iteration: 5, approx. x: 3.190605e-01, error: 1.980267e-02, residual: 4.619788e-04
iteration: 6, approx. x: 3.098768e-01, error: 9.183678e-03, residual: 9.759948e-05
iteration: 7, approx. x: 3.065214e-01, error: 3.355400e-03, residual: 1.291781e-05
iteration: 8, approx. x: 3.059175e-01, error: 6.038397e-04, residual: 4.171155e-07
iteration: 9, approx. x: 3.058967e-01, error: 2.084388e-05, residual: 4.967664e-10
iteration: 10, approx. x: 3.058967e-01, error: 2.488343e-08, residual: 6.661338e-16
Final approx. solution: 3.058967e-01 after 10 iterations with 2.488343e-08 error and 6.661338e-16 residual from initial point 1.000000e+00.

steffensen converges quickly to the correct point of 0.3059, within 4 iterations, while iteration of newtonian methods
take longer to converge and not quadratically, looking at the residuals of each, steffensen narrows in on the residual tolerance
much quicker because its jumping quadratically while iteration of newtons method is fairly linear residual change until nearing the solution.