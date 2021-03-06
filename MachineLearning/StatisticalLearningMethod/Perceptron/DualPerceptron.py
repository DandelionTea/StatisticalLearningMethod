import numpy as np
import random
import matplotlib.pyplot as plt

def Newtrain(train_set):
    size = train_set.shape
    count = 0
    Newset = np.zeros((size[0], size[1]+1))
    for i in train_set:
        Newset[count] = np.append(i, 1)
        count += 1
    return Newset

def train(train_set, iteration_num, eta):
    m, n = np.shape(train_set)
    w = np.zeros((train_set.shape[1] - 1, 1))
    RNS = np.random.randint(1, m+1, (iteration_num, 1))
    i_count = 0
    for i in RNS:
        i_count += 1
        x = train_set[int(i)-1]
        x = np.reshape(x, (1, train_set.shape[1]))
        j_count = 0
        if x[0][0]*x[0, 1:].reshape((1, train_set.shape[1]-1))@w <= 0:
            for j in RNS[0:i_count, :].reshape((i_count,1)):
                if int(j) == int(i):
                    j_count += 1
            w += (eta*j_count*x[0][0]*x[0, 1:].reshape((1, train_set.shape[1]-1))).transpose()
    return w

def Visualization(train_set,w):
    plt.figure()
    x1 = np.linspace(0, 8, 100)
    x2 = (-w[-1]-w[0]*x1)/w[1]
    plt.plot(x1, x2, color='r', label='DualPerceptron')
    for i in range(train_set.shape[0]):
        if train_set[i][0] == 1:
            plt.scatter(train_set[i][1], train_set[i][2], s=100)
        else:
            plt.scatter(train_set[i][1], train_set[i][2], marker='+', s=100)
    plt.show()

if __name__ == '__main__':
    train_set1 = [[1, 1, 3], [1, 2, 2], [1, 3, 8], [1, 2, 6]]  # Positives
    train_set2 = [[-1, 2, 1], [-1, 4, 1], [-1, 6, 2], [-1, 7, 3]]  # Negatives
    train_set = train_set1 + train_set2  # concatenate
    train_set = np.array(train_set)
    NewTrain_set = Newtrain(train_set)
    weight = train(train_set=NewTrain_set, iteration_num=1000, eta=0.01)
    print(weight)
    Visualization(NewTrain_set, weight)

