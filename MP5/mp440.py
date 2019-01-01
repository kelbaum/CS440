import inspect
import sys
import numpy as np
import matplotlib.pyplot as plt

global ux_G
global p
global iterations

'''
Raise a "not defined" exception as a reminder
'''
def _raise_not_defined():
    print "Method not implemented: %s" % inspect.stack()[1][3]
    sys.exit(1)

'''
Kalman 2D
'''
def kalman2d(data):
    estimated = []
    # Your code starts here
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here
    #print data
    #Q = [[0.0001, 0.00002], [0.00002, 0.0001]]
    Q = [[2, 0.5], [0.5, 2]]
    #R = [[0.01, 0.005], [0.005, 0.02]]
    R = [[200, 50], [50, 300]]

    x_k_minus_1 = [1.6, 1.6]
    P_k_minus_1 = [[1000000, 0], [0, 1000000]]
    for i in range(len(data)):
        x_k = [x_k_minus_1[0] + data[i][0], x_k_minus_1[1] + data[i][1]]

        P_k = [[P_k_minus_1[0][0] + Q[0][0], P_k_minus_1[0][1] + Q[0][1]],
        [P_k_minus_1[1][0] + Q[1][0], P_k_minus_1[1][1] + Q[1][1]]]

        denominator = [[P_k[0][0] + R[0][0], P_k[0][1] + R[0][1]],
        [P_k[1][0] + R[1][0], P_k[1][1] + R[1][1]]]

        K_k = np.matmul(P_k, np.linalg.inv(denominator)).tolist()

        Y = [data[i][2] - x_k[0], data[i][3] - x_k[1]]
        Y = np.matmul(K_k, Y).tolist()

        estimated.append([x_k[0] + Y[0], x_k[1] + Y[1]])
        x_k_minus_1 = x_k

        X = [[1 - K_k[0][0], 0 - K_k[0][1]], [0 - K_k[1][0], 1 - K_k[1][1]]]
        P_k_minus_1 = np.matmul(X, P_k).tolist()

    '''
    # finding x_k : x_k = x_k-1 + u_k-1
    x_k = []
    x_k_minus_1 = [0, 0]
    for i in range(len(data)):
        if len(x_k) != 0:
            x_k_minus_1 = x_k[i - 1]
        x_k.append([x_k_minus_1[0] + data[i][0], x_k_minus_1[1] + data[i][1]])
    #print x_k

    # finding P_k : P_k = P_k-1 + Q
    P_k = []
    P_k_minus_1 = [[1, 0], [0, 1]]
    for i in range(len(x_k)):
        if len(P_k) != 0:
            P_k_minus_1 = P_k[i - 1]
        P_k.append([[P_k_minus_1[0][0] + Q[0][0], P_k_minus_1[0][1] + Q[0][1]],
        [P_k_minus_1[1][0] + Q[1][0], P_k_minus_1[1][1] + Q[1][1]]])
    #print P_k

    # finding K_k : K_k = P_k / (P_k + R) = P_k * (P_k + R)^-1
    K_k = []
    for i in range(len(P_k)):
        denominator = [[P_k[i][0][0] + R[0][0], P_k[i][0][1] + R[0][1]],
        [P_k[i][1][0] + R[1][0], P_k[i][1][1] + R[1][1]]]
        K_k.append(np.matmul(P_k[i], np.linalg.inv(denominator)).tolist())
    print K_k

    # finding final x_k : x_k = x_k- + K_k(z_k - x_k-)
    final_x_k = []
    for i in range(len(K_k)):
        Y = [data[i][2] - x_k[i][0], data[i][3] - x_k[i][1]]
        Y = np.matmul(K_k[i], Y).tolist()
        final_x_k.append([x_k[i][0] + Y[0], x_k[i][1] + Y[1]])
    #print final_x_k

    estimated = final_x_k
    '''

    #_raise_not_defined()
    return estimated

'''
Plotting
'''
def plot(data, output):
    # Your code starts here
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here

    #print output
    x = []
    y = []
    for i in range(len(data)):
        x.append(data[i][2])
        y.append(data[i][3])
    plt.plot(x, y, label='observations')
    a = []
    b = []
    for i in range(len(output)):
        a.append(output[i][0])
        b.append(output[i][1])
    '''
    for i in range(len(data)):
        print "(", x[i], y[i], ") (", a[i], b[i], ")"
    '''
    plt.plot(a, b, label='estimates')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis([0, 10, -5, 5])
    plt.legend()
    plt.show()
    #_raise_not_defined()
    return

'''
Kalman 2D
'''
def kalman2d_shoot(ux, uy, ox, oy, reset=False):
    decision = (0, 0, False)
    # Your code starts here
    R = np.array([[200, 50],[50, 300]])
    Q = np.array([[2, 0.5], [0.5, 2]])
    global iterations
    global ux_G
    global p

    if reset:
        iterations = 1
        p = np.identity(2)
        ux_G = np.array([0,0])
    xNewInit = ux_G + np.array([ux,uy])
    pTemp = p + Q
    K =  np.matmul(pTemp, np.linalg.inv(pTemp+R))

    xHat = xNewInit + np.matmul(K, np.array(ox,oy) - xNewInit)

    ux_G = xHat
    p = np.matmul((np.identity(2) - K),pTemp)
    iterations = iterations + 1
    #_raise_not_defined()
    if iterations < 180:
        return decision
    else:
        return (ux_G[0], ux_G[1], True)
    # Your code ends here

'''
Kalman 2D
'''
def kalman2d_adv_shoot(ux, uy, ox, oy, reset=False):
    decision = (0, 0, False)
    # Your code starts here
    # Your code ends here
    _raise_not_defined()
    return decision
