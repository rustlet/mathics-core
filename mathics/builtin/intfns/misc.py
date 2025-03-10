# -*- coding: utf-8 -*-

"""
Miscelanea of Integer Functions
"""


from mathics.core.attributes import A_LISTABLE, A_PROTECTED
from mathics.core.builtin import MPMathFunction


class BernoulliB(MPMathFunction):
    """
    <url>:WMA link:https://reference.wolfram.com/language/ref/BernoulliB.html</url>

    <dl>
      <dt>'BernoulliB'[$n$]
      <dd>represents the Bernoulli number $B_n$.

      <dt>'BernouilliB'[$n$, $x$]
      <dd>represents the Bernoulli polynomial $B_n(x)$.
    </dl>

    >> BernoulliB[42]
     = 1520097643918070802691 / 1806

    First five Bernoulli numbers:

    >> Table[BernoulliB[k], {k, 0, 5}]
     = ...

    ## This must be (according to WMA)
    ## = {1, -1 / 2, 1 / 6, 0, -1 / 30, 0}
    ## but for some reason, in the CI the previous test produces
    ## the output:
    ## {1, 1 / 2, 1 / 6, 0, -1 / 30, 0}

    First five Bernoulli polynomials:

    >> Table[BernoulliB[k, z], {k, 0, 3}]
     = {1, -1 / 2 + z, 1 / 6 - z + z ^ 2, z / 2 - 3 z ^ 2 / 2 + z ^ 3}
    """

    attributes = A_PROTECTED | A_LISTABLE
    mpmath_name = "bernoulli"
    nargs = {1, 2}
    summary_text = "Bernoulli number and function"
    sympy_name = "bernoulli"
