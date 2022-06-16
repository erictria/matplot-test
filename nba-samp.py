import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

nba_df = pd.read_csv('latest_RAPTOR_by_team.csv')
# reg_season_df = nba_df[nba_df['season_type'] == 'RS']
playoffs_df = nba_df[(nba_df['season_type'] == 'PO') & (nba_df['poss'] >= 200)]

playoffs_df.sort_values('raptor_total', ascending = False, inplace = True)
summary_playoffs_df = playoffs_df[['player_name', 'player_id', 'team', 'poss', 'raptor_offense', 'raptor_defense', 'raptor_total']]

playoffs_top_poss = playoffs_df.sort_values('poss', ascending = False).drop_duplicates(['team'])[['team', 'poss']]
playoffs_top_poss.rename(columns = {'poss': 'max_poss'}, inplace = True)

final_playoffs_df = summary_playoffs_df.merge(playoffs_top_poss, how = 'inner', on = 'team')
final_playoffs_df['percent_poss'] = final_playoffs_df['poss'] / final_playoffs_df['max_poss']
filtered_playoffs_df = final_playoffs_df[final_playoffs_df['percent_poss'] >= 0.7]

# breakpoint()

# matplotlib scatter plot - Not annotating
# plt.scatter(x = filtered_playoffs_df['raptor_offense'], y = filtered_playoffs_df['raptor_defense'])
# plt.annotate(filtered_playoffs_df['player_name'], (filtered_playoffs_df['raptor_offense'], filtered_playoffs_df['raptor_defense']))
# plt.show(block = True)

# pandas scatter plot - NOT WORKING
# summary_playoffs_df.plot(kind = 'scatter', x = 'raptor_offense', y = 'raptor_defense')
# ax = summary_playoffs_df.plot(kind = 'scatter', x = 'raptor_offense', y = 'raptor_defense', figsize = (10,10))
# summary_playoffs_df[['x', 'y', 'label']].apply(lambda x: ax.text(*x), axis = 1)

# seaborn scatter plots - OK
fig, ax = plt.subplots(figsize = (8, 8))
ax = sns.scatterplot(x = 'raptor_offense', y = 'raptor_defense', hue = 'player_name', data = filtered_playoffs_df, legend = 'full')
                     #,palette = {1:'red',2:'orange',3:'yellow',4:'green',5:'blue'})
ax.legend(loc = 'lower left')
plt.show(block = True)


# Reference: https://projects.fivethirtyeight.com/nba-player-ratings/
# Data: https://github.com/fivethirtyeight/data/tree/master/nba-raptor
# TODO: https://stackoverflow.com/questions/7908636/how-to-add-hovering-annotations-in-matplotlib
# TODO: https://stackoverflow.com/questions/13306519/get-data-from-plot-with-matplotlib/13306887#13306887