import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc

import day_classify as dc
from month_classifier import Rainfall_Year
from monthly_mat_classifier import monthly_rain_classifier
#Region 77.4684E, 12.7098N, 77.7129E, 13.1081N

#--------------------------------------Station 1 Data-----------------------------------------

list01_11 = ['AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AN', 'AO', 'AP', 'AQ'] #include 'AM' for 2007
list12_22 = ['AR', 'AS','AT', 'AU', 'AV', 'AW', 'AX', 'AY', 'AZ']
list2 =['D','H', 'L', 'P', 'T','X', 'AB', 'AF', 'AJ', 'AN', 'AR']


bang_stat1_df4 = pd.DataFrame()
bang_stat1_df5 = pd.DataFrame()


for m in list01_11:
    bang_stat1_4 = pd.read_excel('DataSheet1.xlsx', usecols=m)
    bang_stat1_df4 = pd.concat([bang_stat1_df4, (bang_stat1_4[1:369])], axis = 0, ignore_index= True)
bang_stat1_df4 = bang_stat1_df4.stack().reset_index()


for n in list12_22:
    bang_stat1_5 = pd.read_excel('DataSheet1.xlsx', usecols=n)
    bang_stat1_df5 = pd.concat([bang_stat1_df5, (bang_stat1_5[1:369])], axis = 0, ignore_index= True)
bang_stat1_df5 = bang_stat1_df5.stack().reset_index()

bang_stat1_df4.rename(columns = {0: 'Rainfall'}, inplace=True)
bang_stat1_df5.rename(columns = {0: 'Rainfall'}, inplace=True)


bang_stat1_df4['Rainfall'] = pd.to_numeric(bang_stat1_df4['Rainfall'], errors = 'coerce')
df4_rarr = bang_stat1_df4['Rainfall'].array
df4_rarr = np.insert(df4_rarr, 0, 0.0)
#df4_rarr = np.delete(df4_rarr, 4017)   #include when including 2007

bang_stat1_df5['Rainfall'] = pd.to_numeric(bang_stat1_df5['Rainfall'], errors = 'coerce')
df5_rarr = bang_stat1_df5['Rainfall'].array
df5_rarr = np.insert(df5_rarr, 0, 0.0)
df5_rarr = np.delete(df5_rarr, 3288)

bang_stat1_4_month2001 = dc.month_rain_getter(df4_rarr[1:369])
bang_stat1_4_array = np.array(bang_stat1_4_month2001)
bang_stat1_4_array_test = np.array(bang_stat1_4_month2001)

for num1 in range(1, 11):
    num2 = num1 + 1
    if num2/4 ==1 or num2/7 == 1:
        bang_stat1_4_iter = dc.month_rain_getter(df4_rarr[(369*num1):(369*num2)], leap = True)
        bang_stat1_4_array_test = np.append(bang_stat1_4_array_test, bang_stat1_4_iter)
    else:
        bang_stat1_4_iter = dc.month_rain_getter(df4_rarr[(369*num1):(369*num2)])
        bang_stat1_4_array_test = np.append(bang_stat1_4_array_test, bang_stat1_4_iter)



#========================================== Station 2 Data ============================================

list01_11 = ['AJ', 'AK', 'AL', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AS','AT']
list12_22 = ['AU', 'AV']#, 'AW', 'AX', 'AY', 'AZ']
list2 =['D','H', 'L', 'P', 'T','X', 'AB', 'AF', 'AJ', 'AN', 'AR']

bang_stat2_df4 = pd.DataFrame()
bang_stat2_df5 = pd.DataFrame()

for m in list01_11:
    bang_stat2_4 = pd.read_excel('DataSheet_2.xlsx', usecols=m)
    bang_stat2_df4 = pd.concat([bang_stat2_df4, (bang_stat2_4[1:368])], axis = 0, ignore_index= True)
bang_stat2_df4 = bang_stat2_df4.stack().reset_index()

for n in list12_22:
    bang_stat2_5 = pd.read_excel('DataSheet_2.xlsx', usecols=n)
    bang_stat2_df5 = pd.concat([bang_stat2_df5, (bang_stat2_5[1:368])], axis = 0, ignore_index= True)
bang_stat2_df5 = bang_stat2_df5.stack().reset_index()

bang_stat2_df4.rename(columns = {0: 'Rainfall'}, inplace=True)
bang_stat2_df5.rename(columns = {0: 'Rainfall'}, inplace=True)

bang_stat2_df4['Rainfall'] = pd.to_numeric(bang_stat2_df4['Rainfall'], errors = 'coerce')
df4_rarr_stat2 = bang_stat2_df4['Rainfall'].array
df4_rarr_stat2 = np.insert(df4_rarr_stat2, 0, 0.0)
#df4_rarr_stat2 = np.delete(df4_rarr_stat2, 4017)

bang_stat2_df5['Rainfall'] = pd.to_numeric(bang_stat2_df5['Rainfall'], errors = 'coerce')
df5_rarr_stat2 = bang_stat2_df5['Rainfall'].array
df5_rarr_stat2 = np.insert(df5_rarr_stat2, 0, 0.0)
#df5_rarr_stat2 = np.delete(df5_rarr_stat2, 3288)

bang_stat2_4_month2001 = dc.month_rain_getter(df4_rarr_stat2[1:368])
bang_stat2_4_array = np.array(bang_stat2_4_month2001)
bang_stat2_4_array_test = np.array(bang_stat2_4_month2001)

for num1_stat2 in range(1, 11):
    num2_stat2 = num1_stat2 + 1
    if num2_stat2 % 4 == 0:
        bang_stat2_4_iter = dc.month_rain_getter(df4_rarr_stat2[(368*num1_stat2):(368*num2_stat2)], leap = True)
        bang_stat2_4_array_test = np.append(bang_stat2_4_array_test, bang_stat2_4_iter)
    else:
        bang_stat2_4_iter = dc.month_rain_getter(df4_rarr_stat2[(368*num1_stat2):(368*num2_stat2)])
        bang_stat2_4_array_test = np.append(bang_stat2_4_array_test, bang_stat2_4_iter)


#==================================== Station 3 Data=============================

list01_11 = [ 'AJ', 'AK', 'AL', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AS','AT']
list12_22 = ['AU', 'AV']#, 'AW', 'AX', 'AY', 'AZ']
list2 =['D','H', 'L', 'P', 'T','X', 'AB', 'AF', 'AJ', 'AN', 'AR']

bang_stat3_df4 = pd.DataFrame()
bang_stat3_df5 = pd.DataFrame()

for m in list01_11:
    bang_stat3_4 = pd.read_excel('DataSheet_3.xlsx', usecols=m)
    bang_stat3_df4 = pd.concat([bang_stat3_df4, (bang_stat3_4[1:368])], axis = 0, ignore_index= True)
bang_stat3_df4 = bang_stat3_df4.stack().reset_index()


for n in list12_22:
    bang_stat3_5 = pd.read_excel('DataSheet_3.xlsx', usecols=n)
    bang_stat3_df5 = pd.concat([bang_stat3_df5, (bang_stat3_5[1:369])], axis = 0, ignore_index= True)
bang_stat3_df5 = bang_stat3_df5.stack().reset_index()

bang_stat3_df4.rename(columns = {0: 'Rainfall'}, inplace=True)
bang_stat3_df5.rename(columns = {0: 'Rainfall'}, inplace=True)

bang_stat3_df4['Rainfall'] = pd.to_numeric(bang_stat3_df4['Rainfall'], errors = 'coerce')
df4_rarr_stat3 = bang_stat3_df4['Rainfall'].array
df4_rarr_stat3 = np.insert(df4_rarr_stat3, 0, 0.0)
#df4_rarr = np.delete(df4_rarr, 4017)

bang_stat3_df5['Rainfall'] = pd.to_numeric(bang_stat3_df5['Rainfall'], errors = 'coerce')
df5_rarr_stat3 = bang_stat3_df5['Rainfall'].array
df5_rarr_stat3 = np.insert(df5_rarr_stat3, 0, 0.0)
#df5_rarr_stat3 = np.delete(df5_rarr_stat3, 3288)


bang_stat3_4_month2001 = dc.month_rain_getter(df4_rarr_stat3[1:368])
bang_stat3_4_array = np.array(bang_stat3_4_month2001)
bang_stat3_4_array_test = np.array(bang_stat3_4_month2001)

for num1_stat3 in range(1, 11):
    num2_stat3 = num1_stat3 + 1
    if num2_stat3 % 4 == 0:
        bang_stat3_4_iter = dc.month_rain_getter(df4_rarr_stat3[(368*num1_stat3):(368*num2_stat3)], leap = True)
        bang_stat3_4_array_test = np.append(bang_stat3_4_array_test, bang_stat3_4_iter)
    else:
        bang_stat3_4_iter = dc.month_rain_getter(df4_rarr_stat3[(368*num1_stat3):(368*num2_stat3)])
        bang_stat3_4_array_test = np.append(bang_stat3_4_array_test, bang_stat3_4_iter)



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


stat1_df1 = pd.DataFrame(bang_stat1_4_array_test)
stat2_df1 = pd.DataFrame(bang_stat2_4_array_test)
stat3_df1 = pd.DataFrame(bang_stat3_4_array_test)


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
