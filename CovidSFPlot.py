import matplotlib.pyplot as plt
from datetime import datetime

def fPlotSFCovid(pFileName, name):
    dates = []
    cases = []

    # Improved file handling
    with open(pFileName, 'r') as file:
        for line in file:
            currColumn = line.split(',')
            # Convert date string to datetime object
            date = datetime.strptime(currColumn[0], '%Y-%m-%d')
            dates.append(date)
            # Ensure cases are integers
            cases.append(float(currColumn[2].rstrip()))

    # Use a DateFormatter for the x-axis
    ax = plt.axes()
    ax.xaxis.set_major_locator(plt.MaxNLocator(4))
    ax.yaxis.set_major_locator(plt.MaxNLocator(4))
    plt.scatter(dates, cases, c='blue', s=10)
    plt.xlabel('Date')
    plt.ylabel('Cases')
    plt.title('COVID Cases Over Time in ' + name)
    plt.show()
