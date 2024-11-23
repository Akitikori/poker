import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.cm as cm

# Data for each poker night
data_0207 = {
    'Names': ['Couper', 'Ade', 'Ropo', 'DJ', 'Duardo', 'Lovemore', 'Ebube'],
    'Buy in': [20, 10, 10, 10, 20, 20, 10],
    'Final Balance': [15.75, 0, 0, 75.40, 0, 9.05, 0],
}
data_0214 = {
    'Names': ['DJ', 'Lovemore', 'Ropo', 'Seun'],
    'Buy in': [15, 20, 20, 10],
    'Final Balance': [0, 3.20, 3.05, 58.75],
}
data_0221 = {
    'Names': ['Lovemore', 'Ropo', 'Seun', 'Ade', 'Ian', 'Couper'],
    'Buy in': [20, 10, 20, 10, 10, 10],
    'Final Balance': [16.975, 11.525, 10.025, 14.975, 4.325, 22.175],
}
data_0228 = {
    'Names': ['Lovemore', 'Ropo', 'Ebube', 'Ade', 'DJ'],
    'Buy in': [20, 20, 10, 20, 10],
    'Final Balance': [8.20, 11.10, 0, 15.05, 60.65],
}
data_0306 = {
    'Names': ['Lovemore', 'Ropo', 'Couper', 'Ade', 'DJ', 'Richmond', 'Duardo', 'Ebube'],
    'Buy in': [10, 10, 20, 15, 15, 10, 20, 0],
    'Final Balance': [14.80, 21.65, 12.20, 8.10, 28.90, 19.30, 0, 0],
}
data_0313 = {
    'Names': ['Lovemore', 'Ropo', 'Couper', 'Ade', 'DJ', 'Ian', 'Duardo', 'Ebube'],
    'Buy in': [10, 10, 10, 20, 20, 15, 20, 10],
    'Final Balance': [26.32, 29.12, 4.02, 6.27, 13.67, 0, 18.67, 13.77],
}
data_0320 = {
    'Names': ['Lovemore', 'Ropo', 'Couper', 'DJ', 'Duardo', 'Richmond', 'Ian'],
    'Buy in': [10, 10, 10, 26, 15, 10, 0],
    'Final Balance': [14.97, 11.57, 12.12, 23.12, 0, 19.22, 0],
}
data_0327 = {
    'Names': ['Ropo', 'Couper', 'DJ', 'Duardo', 'Numfor', 'Ade'],
    'Buy in': [10, 10, 10, 10, 10, 10],
    'Final Balance': [0, 21.60, 11.10, 14.90, 0, 12.40],
}
data_0417 = {
    'Names': ['Ropo', 'Couper', 'DJ', 'Ade', 'Lovemore'],
    'Buy in': [10, 10, 10, 20, 10],
    'Final Balance': [14.30, 20.25, 0, 14.75, 10.70],
}
data_0424 = {
    'Names': ['Couper', 'DJ', 'Lovemore', 'Jonny'],
    'Buy in': [10, 10, 10, 10],
    'Final Balance': [18.35, 16.15, 13.85, 5],
}
data_0515 = {
    'Names': ['Ropo', 'Couper', 'Ade', 'Lovemore', 'Ian'],
    'Buy in': [10, 10, 10, 10, 10],
    'Final Balance': [9.00, 14.70, 3.45, 6.05, 14.57],
}
data_0529 = {
    'Names': ['Ropo', 'Couper', 'Ade', 'Lovemore', 'DJ', 'Jonny'],
    'Buy in': [10, 20, 10, 20, 23.95, 20],
    'Final Balance': [17.20, 15.85, 10.80, 24.25, 0, 35.85],
}
data_0605 = {
    'Names': ['Ropo', 'Couper', 'Ade', 'Lovemore', 'DJ', 'Jonny', 'Ebube'],
    'Buy in': [10, 10, 20, 30, 25, 10, 20],
    'Final Balance': [0, 48.84, 0, 8.89, 37.14, 25.04, 5.09],
}
# add for 0606
data_0606 = {
    'Names': ['Couper', 'DJ', 'Lovemore', 'Jonny'],
    'Buy in': [20, 10, 10, 30],
    'Final Balance': [10.10, 25.90, 35.90, 0],
}
data_0613 = {
    'Names': ['Ropo', 'Couper', 'Ade', 'Lovemore', 'Duardo', 'Seun'],
    'Buy in': [10, 10, 20, 10, 20, 15],
    'Final Balance': [21.20, 26.85, 14.30, 8.50, 5.25, 8.90],
}

data_0620 = {
    'Names': ['Ropo', 'Couper', 'Ade', 'Lovemore', 'DJ', 'Jonny', 'Seun'],
    'Buy in': [20, 10, 15, 10, 10, 20, 15],
    'Final Balance': [8.75, 3.05, 7.80, 30.40, 26, 18.80, 5.20],
}
data_0627 = {
    'Names': ['Ropo', 'Couper', 'Ade', 'Lovemore', 'Jonny', 'Seun', 'DJ', 'Shady', 'Akin', 'Duardo'],
    'Buy in': [10, 10, 20, 10, 15, 10, 10, 10, 10, 10],
    'Final Balance': [16.825, 6.125, 17.525, 24.875, 20.275, 0, 10.775, 17.975, 0.625, 0],
}
data_0711 = {
    'Names': ['Couper', 'DJ', 'Ade', 'Lovemore', 'Jonny'],
    'Buy in': [20, 10, 10, 20, 10],
    'Final Balance': [16.2, 0, 15.6, 77.35, 14.95],
}
data_0718 = {
    'Names': ['Ropo', 'Couper', 'Lovemore', 'Jonny', 'DJ'],
    'Buy in': [10, 15, 10, 10, 10],
    'Final Balance': [10.75, 7.40, 12.55, 0, 24.30],
}
data_0725 = {
    'Names': ['Ropo', 'Ade', 'Lovemore', 'Bam', 'DJ', 'Andrew', 'Oore', 'Numfor', 'Ebube'],
    'Buy in': [20, 20, 10, 10, 10, 10, 25, 10, 15],
    'Final Balance': [8.15, 0, 26.05, 0, 25.35, 28.75, 4.85, 31.85, 4.95],
}
data_0808 = {
    'Names': ['Ebube', 'Ade', 'Lovemore', 'Jonny', 'DJ', 'Sameer'],
    'Buy in': [30, 20, 30, 10, 19, 20],
    'Final Balance': [23.10, 16.30, 0, 49.90, 3.15, 36.55],
}
data_0815 = {
    'Names': ['Ade', 'Couper', 'DJ', 'Lovemore', 'Ropo', 'Shady'],
    'Buy in': [15, 10, 20, 10, 10, 10],
    'Final Balance': [14.40, 17.55, 12.50, 16.65, 4.95, 8.95],
}
data_0822 = {
    'Names': ['Couper', 'DJ', 'Ade', 'Lovemore', 'Ropo'],
    'Buy in': [10, 20, 15, 10, 10],
    'Final Balance': [17.7, 12.65, 14.55, 16.8, 5.1],
}
data_0829 = {
    'Names': ['Ade', 'Couper', 'Ropo', 'Toluwani'],
    'Buy in': [10, 10, 10, 10],
    'Final Balance': [12.10, 20.40, 7.50, 10],
}
data_0902 = {
    'Names': ['Ade', 'Couper', 'DJ', 'Lovemore', 'Ropo', 'Jonny'],
    'Buy in': [15, 15, 18, 10, 10, 20],
    'Final Balance': [0, 28.60, 6.45, 24.25, 5, 23.70],
}
data_0912 = {
    'Names': ['Ade', 'Couper', 'Shady', 'DJ', 'Lovemore', 'Ropo', 'Jonny'],
    'Buy in': [10, 15, 40, 10, 10, 10, 40],
    'Final Balance': [35.15, 13.50, 9.80, 38.75, 20.30, 17.50, 0],
}
data_0919 = {
    'Names': ['Ade', 'Couper', 'Satya', 'Lovemore', 'Ropo', 'Jonny'],
    'Buy in': [20, 10, 10, 20, 10, 15],
    'Final Balance': [18.05, 17.85, 4.65, 40.30, 4.15, 0],
}
data_0926 = {
    'Names': ['Ade', 'Couper', 'Lovemore', 'Ropo', 'DJ', 'Duardo'],
    'Buy in': [30, 10, 30, 10, 20, 20],
    'Final Balance': [9.89, 53.94, 14.94, 6.54, 14.14, 20.54],
}
data_1003 = {
    'Names': ['Ade', 'Couper', 'Shady', 'Ebube', 'Ropo', 'DJ', 'Duardo'],
    'Buy in': [15, 20, 25, 10, 20, 10, 10],
    'Final Balance': [20.44, 14.64, 8.24, 32.54, 10.19, 16.64, 7.29],
}
data_1017 = {
    'Names': ['Couper', 'DJ', 'Ade', 'Jonny'],
    'Buy in': [15, 15, 10, 10],
    'Final Balance': [29.75, 4.1, 13.30, 18.20],
}
data_1024 = {
    'Names': ['Ade', 'Couper', 'Jonny', 'Ropo', 'DJ', 'Lovemore'],
    'Buy in': [20, 20, 20, 20, 30, 40],
    'Final Balance': [39.10, 44.20, 34.20, 32.50, 0, 0],
}
data_1031 = {
    'Names': ['Couper', 'DJ', 'Ade', 'Lovemore', 'Jonny'],
    'Buy in': [30, 20, 50, 20, 50],
    'Final Balance': [30.20, 57.70, 4.90, 86.70, 34.40],
}
data_1107 = {
    'Names': ['Luke', 'Couper', 'Jonny', 'Ropo', 'DJ', 'Lovemore', 'Gideon', 'Michael'],
    'Buy in': [20, 20, 40, 20, 35, 40, 20, 20],
    'Final Balance': [41.30, 31.70, 33.70, 14.30, 0, 53.70, 20.30, 20],
}
data_1114 = {
    'Names': ['Duardo', 'Couper', 'Jonny', 'Ropo', 'DJ', 'Ebube', 'Shady', 'Ade'],
    'Buy in': [20, 20, 60, 20, 40, 50, 20, 50],
    'Final Balance': [60.18, 23.38, 0, 24.18, 72.78, 9.98, 89.48, 0],
}
data_1121 = {
    'Names': ['Couper', 'Ropo', 'DJ', 'Lovemore'],
    'Buy in': [20, 20, 20, 40],
    'Final Balance': [0, 43.30, 19.70, 17],
}

# Create DataFrames for each poker night
df_0207 = pd.DataFrame(data_0207)
df_0214 = pd.DataFrame(data_0214)
df_0221 = pd.DataFrame(data_0221)
df_0228 = pd.DataFrame(data_0228)
df_0306 = pd.DataFrame(data_0306)
df_0313 = pd.DataFrame(data_0313)
df_0320 = pd.DataFrame(data_0320)
df_0327 = pd.DataFrame(data_0327)
df_0417 = pd.DataFrame(data_0417)
df_0424 = pd.DataFrame(data_0424)
df_0515 = pd.DataFrame(data_0515)
df_0529 = pd.DataFrame(data_0529)
df_0605 = pd.DataFrame(data_0605)
df_0606 = pd.DataFrame(data_0606)
df_0613 = pd.DataFrame(data_0613)
df_0620 = pd.DataFrame(data_0620)
df_0627 = pd.DataFrame(data_0627)
df_0711 = pd.DataFrame(data_0711)
df_0718 = pd.DataFrame(data_0718)
df_0725 = pd.DataFrame(data_0725)
df_0808 = pd.DataFrame(data_0808)
df_0815 = pd.DataFrame(data_0815)
df_0822 = pd.DataFrame(data_0822)
df_0829 = pd.DataFrame(data_0829)
df_0902 = pd.DataFrame(data_0902)
df_0912 = pd.DataFrame(data_0912)
df_0919 = pd.DataFrame(data_0919)
df_0926 = pd.DataFrame(data_0926)
df_1003 = pd.DataFrame(data_1003)
df_1017 = pd.DataFrame(data_1017)
df_1024 = pd.DataFrame(data_1024)
df_1031 = pd.DataFrame(data_1031)
df_1107 = pd.DataFrame(data_1107)
df_1114 = pd.DataFrame(data_1114)
df_1121 = pd.DataFrame(data_1121)

# Calculate winnings (Winnings - Buy in)
df_0207['Winnings'] = df_0207['Final Balance'] - df_0207['Buy in']
df_0214['Winnings'] = df_0214['Final Balance'] - df_0214['Buy in']
df_0221['Winnings'] = df_0221['Final Balance'] - df_0221['Buy in']
df_0228['Winnings'] = df_0228['Final Balance'] - df_0228['Buy in']
df_0306['Winnings'] = df_0306['Final Balance'] - df_0306['Buy in']
df_0313['Winnings'] = df_0313['Final Balance'] - df_0313['Buy in']
df_0320['Winnings'] = df_0320['Final Balance'] - df_0320['Buy in']
df_0327['Winnings'] = df_0327['Final Balance'] - df_0327['Buy in']
df_0417['Winnings'] = df_0417['Final Balance'] - df_0417['Buy in']
df_0424['Winnings'] = df_0424['Final Balance'] - df_0424['Buy in']
df_0515['Winnings'] = df_0515['Final Balance'] - df_0515['Buy in']
df_0529['Winnings'] = df_0529['Final Balance'] - df_0529['Buy in']
df_0605['Winnings'] = df_0605['Final Balance'] - df_0605['Buy in']
df_0606['Winnings'] = df_0606['Final Balance'] - df_0606['Buy in']
df_0613['Winnings'] = df_0613['Final Balance'] - df_0613['Buy in']
df_0620['Winnings'] = df_0620['Final Balance'] - df_0620['Buy in']
df_0627['Winnings'] = df_0627['Final Balance'] - df_0627['Buy in']
df_0711['Winnings'] = df_0711['Final Balance'] - df_0711['Buy in']
df_0718['Winnings'] = df_0718['Final Balance'] - df_0718['Buy in']
df_0725['Winnings'] = df_0725['Final Balance'] - df_0725['Buy in']
df_0808['Winnings'] = df_0808['Final Balance'] - df_0808['Buy in']
df_0815['Winnings'] = df_0815['Final Balance'] - df_0815['Buy in']
df_0822['Winnings'] = df_0822['Final Balance'] - df_0822['Buy in']
df_0829['Winnings'] = df_0829['Final Balance'] - df_0829['Buy in']
df_0902['Winnings'] = df_0902['Final Balance'] - df_0902['Buy in']
df_0912['Winnings'] = df_0912['Final Balance'] - df_0912['Buy in']
df_0919['Winnings'] = df_0919['Final Balance'] - df_0919['Buy in']
df_0926['Winnings'] = df_0926['Final Balance'] - df_0926['Buy in']
df_1003['Winnings'] = df_1003['Final Balance'] - df_1003['Buy in']
df_1017['Winnings'] = df_1017['Final Balance'] - df_1017['Buy in']
df_1024['Winnings'] = df_1024['Final Balance'] - df_1024['Buy in']
df_1031['Winnings'] = df_1031['Final Balance'] - df_1031['Buy in']
df_1107['Winnings'] = df_1107['Final Balance'] - df_1107['Buy in']
df_1114['Winnings'] = df_1114['Final Balance'] - df_1114['Buy in']
df_1121['Winnings'] = df_1121['Final Balance'] - df_1121['Buy in']

# Combine all DataFrames into one for plotting
df_combined = pd.concat([
    df_0207[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '02/07'}),
    df_0214[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '02/14'}),
    df_0221[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '02/21'}),
    df_0228[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '02/28'}),
    df_0306[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '03/06'}),
    df_0313[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '03/13'}),
    df_0320[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '03/20'}),
    df_0327[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '03/27'}),
    df_0417[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '04/17'}),
    df_0424[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '04/24'}),
    df_0515[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '05/15'}),
    df_0529[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '05/29'}),
    df_0605[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '06/05'}),
    df_0606[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '06/06'}),
    df_0613[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '06/13'}),
    df_0620[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '06/20'}),
    df_0627[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '06/27'}),
    df_0711[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '07/11'}),
    df_0718[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '07/18'}),
    df_0725[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '07/25'}),
    df_0808[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '08/08'}),
    df_0815[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '08/15'}),
    df_0822[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '08/22'}),
    df_0829[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '08/29'}),
    df_0902[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '09/02'}),
    df_0912[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '09/12'}),
    df_0919[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '09/19'}),
    df_0926[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '09/26'}),
    df_1003[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '10/03'}),
    df_1017[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '10/17'}),
    df_1024[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '10/24'}),
    df_1031[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '10/31'}),
    df_1107[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '11/07'}),
    df_1114[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '11/14'}),
    df_1121[['Names', 'Winnings']].set_index('Names').rename(columns={'Winnings': '11/21'}),
], axis=1)

# Collect all unique player names across all poker nights
all_players = pd.concat([
    df_0207[['Names']],
    df_0214[['Names']],
    df_0221[['Names']],
    df_0228[['Names']],
    df_0306[['Names']],
    df_0313[['Names']],
    df_0320[['Names']],
    df_0327[['Names']],
    df_0417[['Names']],
    df_0424[['Names']],
    df_0515[['Names']],
    df_0529[['Names']],
    df_0605[['Names']],
    df_0606[['Names']],
    df_0613[['Names']],
    df_0620[['Names']],
    df_0627[['Names']],
    df_0711[['Names']],
    df_0718[['Names']],
    df_0725[['Names']],
    df_0808[['Names']],
    df_0815[['Names']],
    df_0822[['Names']],
    df_0829[['Names']],
    df_0902[['Names']],
    df_0912[['Names']],
    df_0919[['Names']],
    df_0926[['Names']],
    df_1003[['Names']],
    df_1017[['Names']],
    df_1024[['Names']],
    df_1031[['Names']],
    df_1107[['Names']],
    df_1114[['Names']],
    df_1121[['Names']],
]).drop_duplicates()['Names'].reset_index(drop=True)

# Ensure all players are included in df_combined
df_combined = df_combined.reindex(all_players).fillna(0)  

# Generate a list of distinct colors for players in all_players
colors = cm.get_cmap('tab20c', len(all_players)).colors 
player_colors = dict(zip(all_players, colors))  # Map each player to a unique color

# # Plot player winnings over poker nights
# plt.figure(figsize=(14, 7))
# for player in df_combined.index:
#     plt.plot(df_combined.columns, df_combined.loc[player], marker='o', label=player, color=player_colors[player])


# plt.title('Player Winnings Over Poker Nights')
# plt.xlabel('Poker Nights')
# plt.ylabel('Winnings ($)')
# plt.legend()
# plt.grid(True)
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# Summarize the total winnings per player
player_sums = df_combined.sum(axis=1).sort_values(ascending=False)

# Plot total winnings per player
plt.figure(figsize=(14, 7))
plt.bar(player_sums.index, player_sums.values, color=[player_colors[player] for player in player_sums.index])  # Use unique colors for bars
plt.title('Total Winnings per Player')
plt.xlabel('Player')
plt.ylabel('Total Winnings ($)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Calculate cumulative winnings for each player across poker nights
df_cumulative = df_combined.cumsum(axis=1)

# Plot cumulative winnings over poker nights
# plt.figure(figsize=(14, 7))
# for player in df_cumulative.index:
#     plt.plot(df_cumulative.columns, df_cumulative.loc[player], marker='o', label=player, color=player_colors[player])

# plt.title('Cumulative Winnings Over Poker Nights')
# plt.xlabel('Poker Nights')
# plt.ylabel('Cumulative Winnings ($)')
# plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize='small')  # Adjust legend for clarity
# plt.grid(True)
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# Step 1: Identify players with fewer than 5 data points
player_counts = (df_combined != 0).sum(axis=1)  # Count non-zero points
players_to_remove = player_counts[player_counts < 5].index

# Step 2: Remove these players from the combined DataFrame
df_combined_filtered = df_combined.drop(index=players_to_remove)

# Define distinct colors for filtered players
filtered_players = df_combined_filtered.index
filtered_colors = cm.get_cmap('tab10', len(filtered_players)).colors  # Use tab10 colormap
player_filtered_colors = dict(zip(filtered_players, filtered_colors))  # Map filtered players to colors


# # Step 3: Plot the filtered data (Winnings Over Poker Nights)
# plt.figure(figsize=(14, 7))
# for player in df_combined_filtered.index:
#     plt.plot(df_combined_filtered.columns, df_combined_filtered.loc[player], marker='o', label=player, color=player_filtered_colors[player])

# plt.title('Filtered Winnings Over Poker Nights')
# plt.xlabel('Poker Nights')
# plt.ylabel('Winnings ($)')
# plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize='small')
# plt.grid(True)
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# Step 4: Cumulative Winnings Plot
df_cumulative_filtered = df_combined_filtered.cumsum(axis=1)

plt.figure(figsize=(14, 7))
for player in df_cumulative_filtered.index:
    plt.plot(df_cumulative_filtered.columns, df_cumulative_filtered.loc[player], marker='o', label=player, color=player_filtered_colors[player])

plt.title('Filtered Cumulative Winnings Over Poker Nights')
plt.xlabel('Poker Nights')
plt.ylabel('Cumulative Winnings ($)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize='small')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

