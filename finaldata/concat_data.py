#concat all csv files across all cities for different file types
import pandas as pd
import glob
import os

#loadfiles() function gets the file type and loop through all the folders and append those filetypes to filetype+"_all" file
#in finaldata folder

def loadfiles(filetype):
    df = pd.DataFrame([])
    k=0
    for filename in glob.iglob("*_"+filetype+".csv.gz"):
        df2 = pd.DataFrame([])
        df2= pd.read_csv(filename)
        #add city and file_date derived from filename to the dataframe
        df2["city"],df2["file_date"]=filename.split("_")[0],filename.split("_")[1]
        if not os.path.isfile("finaldata\\"+filetype+"_all.csv"):
            df2.to_csv("finaldata\\"+filetype+"_all.csv",mode='a')
        else:
            df2.to_csv("finaldata\\"+filetype+"_all.csv",mode='a', header=False)
        k=k+1
        print(k,filename)


loadfiles("reviews")
loadfiles("listings")
loadfiles("calendar")
