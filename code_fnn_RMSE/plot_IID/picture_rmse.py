import pandas as pdimport seaborn as snsimport numpy as npimport matplotlib as mplimport matplotlib.pyplot as pltx = pd.Series([0.1, 0.3, 0.5, 0.7, 1.0])y1 = pd.Series([0.3583, 0.2902, 0.2044, 0.1248, 0.0462])y2 = pd.Series([0.3457, 0.2306, 0.1381, 0.0585, 0.0284])y3 = pd.Series([0.3096, 0.1063, 0.0442, 0.0217, 0.0096])y4 = pd.Series([0.0296, 0.0395, 0.0395, 0.0395, 0.0395])y5 = pd.Series([0.0445, 0.0643, 0.0161, 0.0148, 0.0247])y6 = pd.Series([0.0056, 0.0039, 0.0139, 0.0138, 0.0209])# data1 = {'x': x, 'y1': y1, 'y2': y2, 'y3': y3}# data1_pd = pd.DataFrame(data1)# sns.set_style("darkgrid")plt.scatter(x, y1, marker='d', color='deepskyblue')plt.plot(x, y1, color='deepskyblue', linestyle='--', label='CUSUM_n=100')plt.scatter(x, y2, marker='v', color='orange')plt.plot(x, y2, color='orange', linestyle='-.', label='CUSUM_n=200')plt.scatter(x, y3, marker='<', color='tomato')plt.plot(x, y3, color='tomato', linestyle='-.', label='CUSUM_n=500')plt.scatter(x, y4, marker='d', color='deepskyblue')plt.plot(x, y4, color='deepskyblue', linestyle='-', label='FNN_n=100')plt.scatter(x, y5, marker='v', color='orange')plt.plot(x, y5, color='orange',linestyle='-', label='FNN_n=200')plt.scatter(x, y6, marker='<', color='tomato')plt.plot(x, y6, color='tomato',linestyle='-', label='FNN_n=500')plt.xlabel('Signal Size')plt.ylabel('Values of RMSE')plt.legend()plt.savefig("RMSE_1.png",dpi=300)plt.show()