stop = False
N = 2
while not stop:
    for r in range(2, N):
        p_inv = N*(N-1) / (r*(r-1))
        print( "r + b = N: %d + %d = %d,  P = 1 / %s" % (r, N-r, N, p_inv) )
        if p_inv == 2 and (N-r)%2 == 0:
            stop = True
            break
    N += 1
