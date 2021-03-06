from numpy import *


def loadDataSet(fileName):  # general function to parse tab -delimited floats
    numFeat = len(open(fileName).readline().split('\t')) - 1  # get number of fields
    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat


def standRegres(xArr, yArr):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    xTx = xMat.T * xMat
    if linalg.det(xTx) == 0.0:
        print("This matrix is singular, cannot do inverse")
        return
    ws = xTx.I * (xMat.T * yMat)  # 或者写做 ws = linalg.solve(xTx, xMat.T*yMat)
    # ws = linalg.solve(xTx, xMat.T * yMat)
    return ws


def plotBestFit(xArr, yArr, ws):
    xMat = mat(xArr)
    yMat = mat(yArr)
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xMat[:, 1].flatten().A[0], yMat.T[:, 0].flatten().A[0])

    xCopy = xMat.copy()
    xCopy.sort(0)
    yHat = xCopy * ws

    ax.plot(xCopy[:, 1], yHat)
    plt.show()


# 计算相关系数
def calcCorrcoef(xArr, yArr, ws):
    xMat = mat(xArr)
    yMat = mat(yArr)
    yHat = xMat * ws

    return corrcoef(yHat.T, yMat)
