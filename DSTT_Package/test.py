import warnings
warnings.filterwarnings('ignore')
print('Importing packages..')
# Data manipulation
import pandas as pd
import numpy as np
import os
print('Packages imported')
#make sure the scripts are executed in the correct pacakage location.
if os.path.exists('DSTT_Package'):
    print('Changing working directory to DSTT_Package..')
    os.chdir('DSTT_Package')
import sys
sys.path.append('.') 

from DSTT_utils import *

# Load the data
num_hours = 1
interval_type = 'hourly'
data_dir = 'data'
num_hours = str(num_hours) 
day_dir = interval_type[0]
# Set paths to the training and testing data files
train_file_name ='solar_wind_parameters_data_' + str(num_hours) + '_'+ interval_type + '_train.csv'
test_file_name ='solar_wind_parameters_data_' + str(num_hours) + '_'+ interval_type + '_test.csv'
data_file_full = 'solar_wind_parameters_data_'+ str(num_hours) + '_' + interval_type + '_all.csv'

tr_file = data_dir + os.sep + 'custom' + os.sep + num_hours + day_dir + os.sep +  train_file_name
ts_file = data_dir + os.sep + 'custom' + os.sep + num_hours + day_dir + os.sep + test_file_name

        
all_data = pd.read_csv(tr_file)

# Extract all param except the Dst values
test_data = pd.read_csv(ts_file)

# To extract the original Dst values for the test data
orig_y_test = test_data[dst_col].values
log('all_data.columns:', all_data.columns, verbose=False)
data_add = test_data.drop(columns=[dst_col])
all_data = pd.concat([all_data,data_add])
all_data.sort_values(by=['Timestamp'])
# print('all_data.shape:', all_data.shape)
print('all_data.type:', type(all_data))
all_data.head()