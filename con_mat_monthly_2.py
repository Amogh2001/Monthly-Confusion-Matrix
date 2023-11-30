import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc

import day_classify as dc
from month_classifier import Rainfall_Year
from monthly_mat_classifier import monthly_rain_classifier
#Region 77.4684E, 12.7098N, 77.7129E, 13.1081N




#========================================IMERG Data=====================================


list_year = (2002, 2003, 2004, 2005, 2006, 2008, 2009, 2010, 2011)

r_2001 = Rainfall_Year('Year_IMERG_2001.nc', leap = False)
r_2001.month_imerg_getter()
r_arr01 = np.array(r_2001.r_imerg_arr)
r_arr = np.array(r_arr01)

for inc_imerg in list_year:
    if inc_imerg % 4 == 0:
        r_imerg = Rainfall_Year('Year_IMERG_' + str(inc_imerg) + '.nc', leap = True)
        r_imerg.month_imerg_getter()
        r_arr_imerg = np.array(r_imerg.r_imerg_arr)
        r_arr = np.append(r_arr, r_arr_imerg)

    else:
        r_imerg = Rainfall_Year('Year_IMERG_' + str(inc_imerg) + '.nc')
        r_imerg.month_imerg_getter()
        r_arr_imerg = np.array(r_imerg.r_imerg_arr)
        r_arr = np.append(r_arr, r_arr_imerg)

df_gpm = pd.DataFrame(r_arr)

#================================ Mean of 3 stations =======================================


stat1_df1 = pd.DataFrame(stat1_4_array_test)
stat2_df1 = pd.DataFrame(stat2_4_array_test)
stat3_df1 = pd.DataFrame(stat3_4_array_test)


frames_1_mon = [stat1_df1, stat3_df1]
mon_cat_1 = pd.concat(frames_1_mon, axis = 1, join = 'inner')

frames_2_mon = [mon_cat_1, stat2_df1]
mon_cat2 = pd.concat(frames_2_mon, axis = 1, join = 'inner')

mon_sum1 = mon_cat2.sum(axis=1)
mon_mean1 = mon_sum1.div(3.0)



#================================= Plotting =======================================

plt.scatter(r_arr, mon_mean1)
plt.title = 'IMERG vs Bangalore Mean Scatter Plot'
plt.hist(r_arr)
plt.title = '2000-2011 Rainfall'
plt.show()

#----------------------------------Confusion Matrix--------------------------------

con_mat = np.zeros((15,15))
for r_months in range(0,120):
    con_mat[monthly_rain_classifier(r_arr[r_months]), monthly_rain_classifier(mon_mean1[r_months])] =(con_mat[monthly_rain_classifier(r_arr[r_months]), monthly_rain_classifier(mon_mean1[r_months])]) + 1.0
print(con_mat)
