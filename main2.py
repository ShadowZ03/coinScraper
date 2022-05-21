import investpy
import trendet
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='darkgrid')
data = investpy.get_crypto_historical_data(crypto='vgx-usd',
                                           from_date='01/01/2022',
                                           to_date='02/04/2022')




res = trendet.identify_df_trends(df=data, column='Close')

data.reset_index(inplace=True)

plt.figure(figsize=(20, 10))

ax = sns.lineplot(x=data.index, y=data['Close'])
ax.set(xlabel='Date')

labels = data['Up Trend'].dropna().unique().tolist()

for label in labels:
    sns.lineplot(x=data[data['Up Trend'] == label].index,
                 y=data[data['Up Trend'] == label]['Close'],
                 color='green')

    ax.axvspan(data[data['Up Trend'] == label].index[0],
               data[data['Up Trend'] == label].index[-1],
               alpha=0.2,
               color='green')

labels = data['Down Trend'].dropna().unique().tolist()

for label in labels:
    sns.lineplot(x=data[data['Down Trend'] == label].index,
                 y=data[data['Down Trend'] == label]['Close'],
                 color='red')

    ax.axvspan(data[data['Down Trend'] == label].index[0],
               data[data['Down Trend'] == label].index[-1],
               alpha=0.2,
               color='red')
               
locs, _ = plt.xticks()
labels = []

for position in locs[1:-1]:
    labels.append(str(data['Date'].loc[position])[:-9])

plt.xticks(locs[1:-1], labels)
plt.show()

print(data.head())