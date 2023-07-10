import xarray as xr
import numpy as np
import pandas as pd
import netCDF4 as nc
from day_classify import day_range


class Rainfall_Year:
    
    
    def __init__(self, year_nc, leap = None):
        self.year = year_nc
        
        self.data = xr.open_dataset(year_nc)
        
        self.rainfall_data = self.data['GPM_3IMERGHH_06_precipitationCal']
        
        self.mon_rainfall_arr = []
        
        self.months = range(1,13)
        for j in self.months:
            self.monthly_rainfall = self.rainfall_data.groupby('time.month')[j].groupby('time.day')
            self.mon_rainfall_arr.append(self.monthly_rainfall)
        
        self.days = []
        
        self.days_rain = []
        
        self.leap = leap
        self.monthly_rain = []
        
        
#=========================    Monthly Stuff    =================================
        self.r_imerg_arr = []
        self.monthly = self.rainfall_data.groupby('time.month')
        
#===============================================================================     
        
    def __sum(arr1):
        sum = 0.0
        for i in arr1:
            sum = sum + i
        return sum
    
    def monthly_mean(self):
        #self.day_rain_arr = []
        if self.leap == True:
            for month_l in range(0,12):
               for day_l in range(1,day_range((month_l), leap = True)+1):
                   rfm= xr.DataArray(np.array(self.mon_rainfall_arr[month_l][day_l]))  
                   rfm_sum = sum(rfm)
                   rfm_float = float(rfm_sum*0.5)
                   self.monthly_rain.append(rfm_float)
               month_l += 1    

        else:
             for month_l in range(0,12):
                for day_l in range(1,day_range(month_l)+1):
                    rfm= xr.DataArray(np.array(self.mon_rainfall_arr[month_l][day_l]))  
                    rfm_sum = sum(rfm)
                    rfm_float = float(rfm_sum*0.5)
                    self.monthly_rain.append(rfm_float)
                month_l += 1


    def month_imerg_getter(self):

        for k in range(1,13):
            self.r_daily = xr.DataArray(np.array(self.monthly[k]))
            self.r_daily_sum = sum(self.r_daily)
            self.r_daily_mean = self.r_daily_sum*0.5
            self.r_imerg_arr = np.append(self.r_imerg_arr, self.r_daily_mean)        
            
    
    def daily_mean(self):   #Depreciated function, use monthly_mean
        for i in range(1,31):
            self.day_mean = xr.DataArray(np.array(self.daily_rainfall[i])) 
            self.sum_day = sum(self.day_mean)
            self.mean_day = self.sum_day/48.0
            self.mean_day_flt = float(self.mean_day)
            self.mean_day_daily = self.mean_day_flt*24.0
            self.days.append(float(i))
            self.days_rain.append(self.mean_day_daily)
       

              
            
        

