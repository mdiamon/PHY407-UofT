# SolveLinear.py
# Python module for PHY407
# Paul Kushner, 2015-09-26
# Modifications by Nicolas Grisouard, 2018-09-26
# This module contains useful routines for solving linear systems of equations.
# Based on gausselim.py from Newman
from numpy import empty, copy


def GaussElim(A_in, v_in, pivot=False):
    """Implement Gaussian Elimination. This should be non-destructive for input
    arrays, so we will copy A and v to temporary variables
    It is actually clever to modify this function, rather than copy it and
    modify it in a separate function. The reason is that if you find a bug in
    the common parts, then you only need to fix it once.
    IN:
    A_in [np.array], the matrix to pivot and triangularize
    v_in [np.array], the RHS vector
    pivot [bool, default-False]: user decides if we pivot or not.
    OUT:
    x, the vector solution of A_in x = v_in """
    # copy A and v to temporary variables using copy command
    A = copy(A_in)
    v = copy(v_in)
    N = len(v)

    for m in range(N):
        if pivot:  # This is where I modify GaussElim
            # compare the mth element to all other mth elements below
            ZeRow = m
            for mm in range(m+1, N):
                if abs(A[mm, m]) > abs(A[ZeRow, m]):
                    ZeRow = mm  # I could swap everytime I find a hit, but that
                    # would be a lot of operations. Instead, I just take note
                    # of which row emerges as the winner

            if ZeRow != m:  # now we know if and what to swap
                A[ZeRow, :], A[m, :] = copy(A[m, :]), copy(A[ZeRow, :])
                v[ZeRow], v[m] = copy(v[m]), copy(v[ZeRow])

        # Divide by the diagonal element
        div = A[m, m]
        A[m, :] /= div
        v[m] /= div

        # Now subtract from the lower rows
        for i in range(m+1, N):
            mult = A[i, m]
            A[i, :] -= mult*A[m, :]
            v[i] -= mult*v[m]

    # Backsubstitution
    # create an array of the same type as the input array
    x = empty(N, dtype=v.dtype)
    for m in range(N-1, -1, -1):
        x[m] = v[m]
        for i in range(m+1, N):
            x[m] -= A[m, i]*x[i]
    return x


def PartialPivot(A_in, v_in):
    """ In this function, code the partial pivot (see Newman p. 222) """
    return GaussElim(A_in, v_in, True)
