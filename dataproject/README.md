# Data project (Assignment 2)
This project is the second assignment completed by the group consisting of Victor V. Kristensen (gcp458), Nikoline K. L. Laursen (mxh836), Bertil D. H. Spring (fpg798) in the course **Introduction to Programming and Numerical Analysis** at the University of Copenhagen in Spring 2024.

## The purpose of the project
The project investigates the applicability of the Phillips curve theory across three distinct countries. It examines the data for each country individually, analyzing the curves within the context of each nation and over time.

## Files in the project
The project consists of a Jyputer-notebook file (dataproject.ipynb) and two python-files: DataHelper.py and GraphHelper.py.
* The **dataproject.ipynb** file provides an overview with the results of the exploration of the datasets and the theoretical analysis supported by graphs.
* The **DataHelper.py** file contains a wrapper for multiple APIs with a pandas interface and a help tool to merge the datasets.
* The **GraphHelper.py** file contains a helper function to create the Phillips-Curve, a Box-Plot, a Times Series Plot, and an Exponential fit to use for the Phillips-Curves.

## To run the project:
* The project has been tested using Python 3.11.7.


## **Dependencies:** Apart from a standard Anaconda Python 3 installation, the project requires the following installations:
* API for Statistics Denmark (DstAPi): 
    * Command to install package: ```pip install git+https://github.com/alemartinello/dstapi```
* We access the FRED API using the pandas-datareader package:
    * Command to install package: ```pip install pandas-datareader```


## We use the following datasources / API's in the project:

### Federal Reserve Economic Data (FRED) API
* 'FPCPITOTLZGUSA' (Inflation U.S.)
* 'UNRATE' (Unemployment U.S.)
* 'LRUN74TTDKA156S' (Unemployment Denmark)
* 'FPCPITOTLZGJPN' (Inflation Japan)
* 'LRHUTTTTJPA156S' (Unemployment Japan)

### Statistics Denmark API
* 'PRIS9' (Inflation Denmark)


