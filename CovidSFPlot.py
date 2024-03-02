import matplotlib.pyplot as plt

def fPlotSFCovid(pFileName):
    dates = []
    cases = []

    file = open(pFileName, 'r')
    for line in file:
        currColumn = line.split(',');
        dates.append(currColumn[0])
        cases.append(currColumn[2])

    ax = plt.axes()
    ax.xaxis.set_major_locator(plt.MaxNLocator(4))
    ax.yaxis.set_major_locator(plt.MaxNLocator(4))
    plt.scatter(dates, cases, c='blue')