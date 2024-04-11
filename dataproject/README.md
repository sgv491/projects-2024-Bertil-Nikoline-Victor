# Data analysis project(Assignment 2)
This project is the second assignment completed by the group consisting of Victor V. Kristensen (gcp458), Nikoline K. L. Laursen (mxh836), Bertil D. H. Spring (fpg798) in the course **Introduction to Programming and Numerical Analysis** at the University of Copenhagen in Spring 2024.

## The purpose of the project
The project investigates the applicability of the Phillips curve theory across three distinct countries. It examines the data for each country individually, analyzing the curves within the context of each nation and over time.

## Files in the project
The project consists of a Jyputer-notebook file (InauguralProject2024.ipynb) and two python-files: ExchangeEconomy.py and GraphHelper.py.
* The **dataproject.ipynb** file provides an overview with the results of the exploration of the datasets and the theoretical analysis supported by graphs.
* The **Datahelper.py** file contains a wrapper for multiple APIs with a pandas interface and a help tool to merg the datasets.
* The **GraphHelper.py** file contains a helper function to create the Phillips-Curve, a Box-Plot, a Times Series Plot, and an Exponential fit to use for the Phillips-Curves.

## To run the project
* The project has been tested using Python 3.11.7.

## We apply the following datasets:
*'FPCPITOTLZGUSA' (FRED)
*'UNRATE'(FRED)
*'PRIS9'(DSTAPI)
*'LRUN74TTDKA156S'(FRED)
*'FPCPITOTLZGJPN'(FRED)
*'LRHUTTTTJPA156S'(FRED)

## **Dependencies:** Apart from a standard Anaconda Python 3 installation, the project requires the following installations:
DstAPi: %pip install git+https://github.com/alemartinello/dstapi

