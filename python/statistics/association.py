import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('python\statistics\nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print('*' * 55)
print(nba_2014.head())
print('*' * 55)
print(nba.fran_id.unique())
print('*' * 55)

# Knicks and Nets 2010
knicks_pts_10 = nba_2010.pts[nba.fran_id == 'Knicks']
knicks_mean_score_10 = np.mean(knicks_pts_10)
knicks_median_score_10 = np.median(knicks_pts_10)
nets_pts_10 = nba_2010.pts[nba.fran_id == 'Nets']
nets_mean_score_10 = np.mean(nets_pts_10)
nets_median_score_10 = np.median(nets_pts_10)

diff_means_2010 = knicks_mean_score_10 - nets_mean_score_10
print(f'Average Diff in 2010: {diff_means_2010}')
print('*' * 55)


diff_median_2010 = knicks_median_score_10 - nets_median_score_10
print(f'Median in 2010: {diff_median_2010}')
print('*' * 55)

plt.hist(knicks_pts_10, alpha = 0.8, normed = True, label = 'Knicks')
plt.hist(nets_pts_10,  alpha = 0.8, normed = True, label = 'Nets')
plt.legend()
plt.title('2010 Season')
plt.show()
plt.clf()

knicks_pts_14 = nba_2014.pts[nba.fran_id == 'Knicks']
knicks_mean_score_14 = np.mean(knicks_pts_14)
knicks_median_score_14 = np.median(knicks_pts_14)
nets_pts_14 = nba_2014.pts[nba.fran_id == 'Nets']
nets_mean_score_14 = np.mean(nets_pts_14)
nets_median_score_14 = np.median(nets_pts_14)

diff_means_2014 = knicks_mean_score_14 - nets_mean_score_14
print(f'Average Diff in 2014: {diff_means_2014}')
print('*' * 55)

diff_median_2014 = knicks_median_score_14 - nets_median_score_14
print(f'Median in 2014: {diff_median_2014}')
print('*' * 55)

plt.hist(knicks_pts_14, alpha = 0.8, normed = True, label = 'Knicks')
plt.hist(nets_pts_14,  alpha = 0.8, normed = True, label = 'Nets')
plt.legend()
plt.title('2014 Season')
plt.show()
plt.clf()

# Analyzing relationships between Categorical Variables
location_result_freq = pd.crosstab(nba_2010.game_result, nba_2010.game_location)
print(location_result_freq)
print('*' * 55)

location_result_proportions = location_result_freq/len(nba_2010)
print(location_result_proportions)
print('*' * 55)

point_diff_forecast_cov = np.cov(nba_2010.forecast, nba_2010.point_diff)
print(point_diff_forecast_cov)
print('*' * 55)

point_diff_forecast_corr = pearsonr(nba_2010.forecast, nba_2010.point_diff)
print(point_diff_forecast_corr)
print('*' * 55)

plt.scatter('forecast', 'point_diff', data = nba_2010)
plt.xlabel('Forecasted Win Prob.')
plt.ylabel('Point Differential')
plt.plot()
