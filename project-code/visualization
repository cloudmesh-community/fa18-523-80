import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame, read_csv
from matplotlib.backends.backend_pdf import PdfPages

def main():
    
    df = pd.read_csv('breastcancer.csv', na_values = '?')
    df = df.fillna(df['A7'].median())
    print (df)
    column_header = ['A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10']
    columns = ['Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape', 'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli', 'Mitoses', 'Class']
    
    mean = df.mean(axis = 0) 
    mean = round(mean, 2)
    
    median = df.median(axis = 0)
    
    sd = df.std(axis = 0)
    sd = round(sd, 2)
    
    variance = df.var(axis = 0)
    variance = round(variance, 2)
    
    counter_2 = 1
    for i in range (9):
        print ("\nRow A", counter_2)
        print ("Mean:", mean[counter_2])
        print ("Median:", median[counter_2])
        print ("Standard Deviation:", sd[counter_2])
        print ("Variance:", variance[counter_2])
        counter_2 = counter_2 + 1
    
    counter = 0
    with PdfPages('finalproject.pdf') as pp:
        for i in range (9):
            fig1 = plt.figure()
            sp1 = fig1.add_subplot(1, 1, 1)
            sp1.set_title(columns[counter])
            sp1.set_xlabel("Results")
            sp1.set_ylabel("Number of Cases")
            plt.xticks((1,2,3,4,5,6,7,8,9,10))
            sp1.hist(df[(column_header[counter])], bins=10, color="blue", edgecolor = "black", alpha=0.5, label = [1,2,3,4,5,6,7,8,9,10])
            pp.savefig(fig1)
            counter = counter + 1
    pp.close()
    
main()
