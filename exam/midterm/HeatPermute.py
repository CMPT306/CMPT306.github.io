def permute(A, n):
    if n==1:
        print A
    else:
        for i in range(1,n+1):
            permute(A, n-1)
            if n%2:
                A[0], A[n-1] = A[n-1], A[0]
            else:
                A[i-1], A[n-1] = A[n-1], A[i-1]

A = ['a', 'b', 'c', 'd']
permute(A, 4)
        