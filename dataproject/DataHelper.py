# Importing the datetime module
import datetime

# A wrapper for multiple APIs with a pandas interface
# Run this in your terminal to use the pandas-datareader: %pip install pandas-datareader
# Importing the pandas_datareader module
import pandas_datareader


#####################
#     U.S. Data     #
#####################

def inflation_annual_US(startDate = datetime.datetime(1900,1,1), endDate = datetime.datetime(2024,1,1)):

    # Getting inflation data
    inflation = pandas_datareader.data.DataReader('FPCPITOTLZGUSA', 'fred', startDate, endDate)

    return inflation

def unemployment_annual_US(startDate = datetime.datetime(1900,1,1), endDate = datetime.datetime(2024,1,1)):
    
    # Getting unemployment data
    unemployment_monthly = pandas_datareader.data.DataReader('UNRATE', 'fred', startDate, endDate)

    # Resample the data to annual frequency
    unemployment_annual = unemployment_monthly.resample('AS', convention='start').asfreq()

    return unemployment_annual



########################
#     Denmark Data     #
########################

# Importing the DstApi to fetch data from the API
# Run this in your terminal to use the DstAPi: %pip install git+https://github.com/alemartinello/dstapi
from dstapi import DstApi

# Import pandas
import pandas as pd


def inflation_annual_DK():

    # Initializing DstApi object
    inflation_dk = DstApi('PRIS9')

    # Define the parameters for the API call
    params = inflation_dk._define_base_params(language='en')
    params

    # Get the inflation data
    inflation_dk_api = inflation_dk.get_data(params=params)

    # Set TID as the new index
    inflation_dk_api.set_index('TID', inplace=True)

    # Rename the index column to YEAR
    inflation_dk_api = inflation_dk_api.rename_axis('YEAR')

    # Delete the TYPE column
    del inflation_dk_api['TYPE']

    # Rename INDHOLD column to DK_Inflation
    inflation_dk_api = inflation_dk_api.rename(columns={'INDHOLD': 'DK_INFLATION'})

    # Delete 1900 because it doesn't have an inflation number
    inflation_dk_api = inflation_dk_api.drop(index=1900)

    # Convert the column to integer type
    inflation_dk_api['DK_INFLATION'] = pd.to_numeric(inflation_dk_api['DK_INFLATION'], errors='coerce')

    return inflation_dk_api


def unemployment_annual_DK(startDate = datetime.datetime(1900,1,1), endDate = datetime.datetime(2024,1,1)):
    # Getting unemployment data from FRED instead of DST because FRED has a longer timeseries
    # Note that there is missing data from 1965 until 1969 in the dataset

    # Getting inflation data
    unemployment = pandas_datareader.data.DataReader('LRUN74TTDKA156S', 'fred', startDate, endDate)

    return unemployment