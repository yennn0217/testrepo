import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
from colorspacious import cspace_converter
from collections import OrderedDict
import matplotlib.cm as cm
'''
cmaps = OrderedDict()
cmaps['Sequential'] = [
            'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
            'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
            'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']
'''
cmaps = plt.get_cmap('Spectral')

#input the csv document, and clean the data
fn = 'Global Temperature.csv'
with open(fn) as csvfile:
    csvReader = csv.reader(csvfile)
    listReader = list(csvReader)
listReader.pop(0)
listReader.pop(-1)
print(listReader)
Year = []
Jan = []
Feb = []
Mar = []
Apr = []
May = []
Jun = []
July = []
Aug = []
Sep = []
Oct = []
Nov = []
Dec = []
for i in listReader:
    Year.append(i[0])
    Jan.append(i[1])
    Feb.append(i[2])
    Mar.append(i[3])
    Apr.append(i[4])
    May.append(i[5])
    Jun.append(i[6])
    July.append(i[7])
    Aug.append(i[8])
    Sep.append(i[9])
    Oct.append(i[10])
    Nov.append(i[11])
    Dec.append(i[12])
month = [Jan, Feb, Mar, Apr, May, Jun, July, Aug, Sep, Oct, Nov, Dec]
#{'Jan':Jan, 'Feb':Feb, 'Mar':Mar, 'Apr':Apr, 'May':May, 'Jun':Jun, 'July':July, 'Aug':Aug, 'Sep':Sep, 'Oct':Oct, 'Nov':Nov, 'Dec':Dec}

#column_set = {'Jan':Jan,'Feb':Feb, 'Mar':Mar, 'Apr':Apr, 'May':May, 'Jun':Jun, 'July':July, 'Aug':Aug, 'Sep':Sep, 'Oct':Oct, 'Nov':Nov, 'Dec':Dec}

#transfer it into a dataframe which is earsier to plot
data = pd.DataFrame([Jan, Feb, Mar, Apr, May, Jun, July, Aug, Sep, Oct, Nov, Dec], columns=Year, index=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
print(data)

for i in range(1880, 2020, 15):
    data[str(i)] = data[str(i)].astype(float)

'''
data['Feb'] = data['Feb'].astype(float)
data['Mar'] = data['Mar'].astype(float)
data['Apr'] = data['Apr'].astype(float)
data['May'] = data['May'].astype(float)
data['Jun'] = data['Jun'].astype(float)
data['July'] = data['July'].astype(float)
data['Aug'] = data['Aug'].astype(float)
data['Sep'] = data['Sep'].astype(float)
data['Oct'] = data['Oct'].astype(float)
data['Nov'] = data['Nov'].astype(float)
data['Dec'] = data['Dec'].astype(float)
'''
colors = cm.RdYlGn(np.linspace(1,0,len(data)))              #pandas的漸變色設置
data.plot(title = "Temperature", color = colors)
#plt.legend(loc='lower right')
plt.legend(bbox_to_anchor=(1.0, 1.0))
plt.plasma()
plt.xlabel('Month')
plt.ylabel('Global Mean * 100')
plt.show()
