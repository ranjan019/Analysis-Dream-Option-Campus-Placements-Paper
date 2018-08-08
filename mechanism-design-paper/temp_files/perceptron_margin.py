import matplotlib.pyplot as plt


w1=[(1,2,7), (1,8,1), (1,7,5), (1,6,3), (1,7,8), (1,5,9), (1,4,5)]
w2=[(-1,-4,-2), (-1,1,1), (-1,-1,-3), (-1,-3,2), (-1,-5,-3.25), (-1,-2,-4), (-1,-7,-1)]
eta=0.3     #learning constant
dataset = [(1,2,7), (1,8,1), (1,7,5), (1,6,3), (1,7,8), (1,5,9), (1,4,5), (-1,-4,-2), (-1,1,1), (-1,-1,-3), (-1,-3,2), (-1,-5,-3.25), (-1,-2,-4), (-1,-7,-1)]

def single_sample_perceptron():
    weight = [1,1,1]
    noOfIterations = 0
    count = 0
    while(count<len(dataset)):
        count = 0
        noOfIterations = noOfIterations + 1
        print "Iteration-No: ",
        print noOfIterations
        print "Weights: ",
        print weight

        for i in xrange(len(dataset)):
            ansEval = 0
            for j in xrange(3):
                ansEval = ansEval + float(weight[j]*dataset[i][j])                     # ansEval is a^Ty.
            if(ansEval<0):                                             # a^Ty>0 for all the data to be classified correctly.else incorrect classification.
                for j in xrange(len(weight)):
                    weight[j] = weight[j] + eta*dataset[i][j]              #  updating the weights along with learning constant(eta).
                break                                                  # break so that the process starts again with the new weight values.
            count+=1

    print "Total Iterations: ",
    print noOfIterations
    print "Final Weights: ",
    print weight
    return weight

def plotGraph(a):
    x1 = []
    x2 = []
    y1 = []
    y2 = []
    for i in xrange(len(w1)):
        x1.append(w1[i][1])
        y1.append(w1[i][2])
    for i in xrange(len(w2)):
        x2.append(w2[i][1])
        y2.append(w2[i][2])

    plt.plot(x1,y1,'ro')
    plt.plot(x2,y2,'bo')
    m1 = (a[2]/(1-a[1]))
    print a[1], a[2]
    m2 = (-1)/(m1)
    c = a[0]/(1-a[1])-7
    ya = m1*100+c
    yb = m1*(-100)+c
    plt.plot([100,-100],[ya,yb],'r')
    plt.axis([-50,50,-50,50])
    plt.show()

def main():
    final_weight = single_sample_perceptron()
    plotGraph(final_weight)

if __name__ == "__main__":
    main()
