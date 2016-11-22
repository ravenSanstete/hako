"""
Tangle: depict the interaction of multi-hetero entities

Basic Form: f: (x,y,z,...) -> R^k,
where x,y,z,... are types that can be evaluated(defineable).

######################### Illustration for Concept
For example, user A and user B are assumed always to be evaluable when,
U_A -> Vector_Machine of dim(i) u_a
U_B -> Vector_Machine of dim(i) u_b
with no fuzziness.
Thus, we define
Const_Tangle(UA,UB)=<U_A,U_B>; # the predefined inner product, with no parameter
Thus the tangle then degenerate into a function form from a functional form.
######################### Illustration for Concept

More complicated form should be under consideration.

Parameterized Tangle will be united into the whole world for training.

Interface is defined as the base class Tangle

"""
