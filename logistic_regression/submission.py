import numpy as np



def sigmoid(a):
    return 1.0 / (1 + np.exp(-a))

def logistic_regression(data, labels, weights, num_epochs, learning_rate):
    z = np.ones((data.shape[0],1), dtype='int64')
    data = np.append(z, data, axis=1)
    xt=data.transpose()


    for n in range(num_epochs):
        print(n)
        hypo= sigmoid(np.dot(data, weights))
        error= labels - hypo

        gradient= np.dot(xt, error) 

        weights = weights + learning_rate * gradient
        print(weights)

    return weights


