import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import math

    
def monthly_rain_classifier(flt):
        if flt >= 0.0 and flt < 50.0:
            return 14
        elif flt >= 50.0 and flt < 100.0:
            return 13
        elif flt >= 100.0 and flt < 150.0:
            return 12
        elif flt >= 150.0 and flt < 200.0:
            return 11
        elif flt >= 200.0 and flt < 250.0:
            return 10
        elif flt >= 250.0 and flt < 300.0:
            return 9
        elif flt >= 300.0 and flt < 350.0:
            return 8
        elif flt >= 350.0 and flt < 400.0:
            return 7
        elif flt >= 400.0 and flt < 450.0:
            return 6
        elif flt >= 450.0 and flt < 500.0:
            return 5
        elif flt >= 500.0 and flt < 550.0:
            return 4
        elif flt >= 550.0 and flt < 600.0:
            return 3
        elif flt >= 600.0 and flt < 650.0:
            return 2
        elif flt >= 650.0 and flt < 700.0:
            return 1
        elif flt >= 700.0:
            return 0
        else:
            return("Error")