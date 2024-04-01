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

    # Getting the data from the API
    inflation = pandas_datareader.data.DataReader('FPCPITOTLZGUSA', 'fred', startDate, endDate)

    # Extract the year from the index and assign it back
    inflation.index = inflation.index.year

    # Rename the index to 'Year' and reset the index to make it a column
    inflation = inflation.rename_axis('Year').reset_index()

    # Rename column
    inflation = inflation.rename(columns={'FPCPITOTLZGUSA': 'Inflation_US'})

    return inflation

def unemployment_annual_US(startDate = datetime.datetime(1900,1,1), endDate = datetime.datetime(2024,1,1)):
    
    # Getting the data from the API
    unemployment_monthly = pandas_datareader.data.DataReader('UNRATE', 'fred', startDate, endDate)

    # Resample the data to annual frequency
    unemployment_annual = unemployment_monthly.resample('AS', convention='start').asfreq()

    # Extract the year from the index and assign it back
    unemployment_annual.index = unemployment_annual.index.year

    # Rename the index to 'Year' and reset the index to make it a column
    unemployment_annual = unemployment_annual.rename_axis('Year').reset_index()

    # Rename column
    unemployment_annual = unemployment_annual.rename(columns={'UNRATE': 'Unemployment_US'})

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

    # Rename column
    inflation_dk_api = inflation_dk_api.rename(columns={'TID': 'Year'})

    # Delete the TYPE column
    del inflation_dk_api['TYPE']

    # Rename INDHOLD column to DK_Inflation
    inflation_dk_api = inflation_dk_api.rename(columns={'INDHOLD': 'Inflation_DK'})

    # Convert the column to integer type
    inflation_dk_api['Inflation_DK'] = pd.to_numeric(inflation_dk_api['Inflation_DK'], errors='coerce')

    return inflation_dk_api


def unemployment_annual_DK(startDate = datetime.datetime(1900,1,1), endDate = datetime.datetime(2024,1,1)):
    # Getting unemployment data from FRED instead of DST because FRED has a longer timeseries
    # Note that there is missing data from 1965 until 1969 in the dataset

    # Getting the data from the API
    unemployment = pandas_datareader.data.DataReader('LRUN74TTDKA156S', 'fred', startDate, endDate)

    # Extract the year from the index and assign it back
    unemployment.index = unemployment.index.year

    # Rename the index to 'Year' and reset the index to make it a column
    unemployment = unemployment.rename_axis('Year').reset_index()

    # Rename column
    unemployment = unemployment.rename(columns={'LRUN74TTDKA156S': 'Unemployment_DK'})

    return unemployment



###########################
#     Merged Datasets     #
###########################

def merged_data():

    # Outer merge all of the four data sources
    merged_US_data = pd.merge(inflation_annual_US(), unemployment_annual_US(), on='Year', how='outer')
    merged_DK_inflation = pd.merge(merged_US_data, inflation_annual_DK(), on='Year', how='outer')
    final_merged_df = pd.merge(merged_DK_inflation, unemployment_annual_DK(), on='Year', how='outer')

    # Filter data for years before 1960 since most data is missing
    final_merged_df = final_merged_df[final_merged_df['Year'] > 1960]

    # Filter data for years after 2022 since most data is missing
    final_merged_df = final_merged_df[final_merged_df['Year'] <= 2022]

    return final_merged_df
