#!/usr/bin/env python3

import pandas as pd

def main():
    # file variable
    excel_file = 'movies.xls'
    
    # create a dataframe (DF) file
    # because we did not specify a sheet
    # only the first sheet is read in
    movies = pd.read_excel(excel_file)
    
    # shows the first five rows of our DF
    # DF has 5 rows and 25 columns
    print(movies.head())
    
    # select the 'Titles' column using index = 0
    movies_sheet1 = pd.read_excel(excel_file, sheet_name = 0, index_col = 0)
    
    # display top 10 movies in the DF
    print(movies_sheet1.head())
    
    # expoert 5 movies to excel
    movies_sheet1.head(5).to_excel("5movies.xlsx")
    
    # export to json
    movies_sheet1.head(5).to_json("5movies.json")
    
    # export to csv
    movies_sheet1.head(5).to_csv("5movies.csv")

if __name__ == '__main__':
    main()
