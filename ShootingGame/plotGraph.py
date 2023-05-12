import matplotlib.pyplot as plt
from matplotlib.figure import Figure

def getResultsToPlot() -> list[str]:
    MAX_NUMBER_OF_RESULTS_ON_PLOT = 25

    with open("results.dat") as fp:
        results = [p.strip() for p in fp.read().split('\n')]

    if len(results) <= MAX_NUMBER_OF_RESULTS_ON_PLOT:
        return results[:-1]
    else:
        return results[-(MAX_NUMBER_OF_RESULTS_ON_PLOT+1):-1]
    

def plotGraph() -> Figure:
    fig,ax=plt.subplots(figsize = (5,3))

    results = getResultsToPlot()

    scoreResults = [int(result.split()[0]) for result in results]
    accuracyResults = [int(result.split()[1]) for result in results]

    ax.plot(scoreResults, color="green",marker="o",markersize=5)
    ax.set_ylabel("Score",color="green")
    ax.set_xticks([])
    ax.set_ybound(0, None)

    ax2=ax.twinx()
    ax2.plot(accuracyResults,color="blue",marker="o",markersize=5)
    ax2.set_ylabel("Accuracy",color="blue")
    ax2.set_ybound(0, 100)
    plt.tight_layout()

    return fig