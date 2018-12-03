import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time
from pandas import DataFrame, read_csv
from matplotlib.backends.backend_pdf import PdfPages

def main():
    
    start = time.time()
    
    df = pd.read_csv('breastcancer.csv', na_values = '?')
    df = df.fillna(df['A7'].median())
    
    counter = 0
    
    r = np.random.randint(0, len(df))
    row = df.iloc[r]
    r2 = np.random.randint(0, len(df))
    row2 = df.iloc[r2]
        
    u2_cluster, u4_cluster = assignment (df, row, row2)
    
    u2_cluster_check, u4_cluster_check = u2_cluster, u4_cluster
    
    u2_mean, u4_mean = recalculation (df, u2_cluster, u4_cluster)
    
    for t in range (1500):
        
        u2_cluster, u4_cluster = assignment(df, u2_mean, u4_mean)
        u4_mean, u2_mean = recalculation (df, u2_cluster, u4_cluster)
        
        if u2_cluster_check == u2_cluster and u4_cluster_check == u4_cluster:
            break
        else:
            pass
        
        u2_cluster_check = u2_cluster
        u4_cluster_check  = u4_cluster
        
        counter = counter + 1
        
    mean_columns = ["A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10"]   
    u2_mean_series = [] 
    u4_mean_series = [] 
    for s in range (9):
        u2_mean_series.append(u2_mean[mean_columns[s]])
    for v in range (9):
        u4_mean_series.append(u4_mean[mean_columns[v]])
        
    print ("-----------Final Mean----------\n")
    print ("mu_2:", u2_mean_series)
    
    print ("\n")
    print ("mu_4: ", u4_mean_series) 
    
    u2_df = pd.DataFrame()
    u4_df = pd.DataFrame()
    
    for i in u2_cluster:
        u2_df = u2_df.append(df.iloc[i])
    u2_df["Predicted_Class"] = 2
    for t in u4_cluster:
        u4_df = u4_df.append(df.iloc[t])
    
    final = [u2_df, u4_df]
    result = pd.concat(final)
    result = result.sort_index(axis = 0)
    result = result.fillna(4) 
    final_df = pd.concat([result["Scn"], result["CLASS"], result["Predicted_Class"]], axis = 1, keys = ["ID", "Class", "Predicted_Class"])
    

    print ("\n\n----------Cluster Assignment----------")
    print(final_df[0:21])
    
    error_rate = error (final_df, u2_cluster, u4_cluster)
    
    end = time.time()
    print ("\nTotal time taken to perform analysis: ", end - start)
         
def assignment (df, row, row2):
    u2_cluster = []
    u4_cluster = []
    
    for i in range (len(df)):
        u2_dist = df.iloc[i] - row
        u4_dist = df.iloc[i] - row2
        
        u2_dist_final = np.square(u2_dist[1:10])
        u4_dist_final = np.square(u4_dist[1:10])
        
        u2_dist_final = u2_dist_final.astype(int)
        u4_dist_final = u4_dist_final.astype(int)
        
        u2_final = 0
        u4_final = 0
        
        for t in u2_dist_final:
            u2_final = t + u2_final
            
        for q in u4_dist_final:
            u4_final = q + u4_final
        
        u2_final = np.sqrt(u2_final)
        u4_final = np.sqrt(u4_final)
        
        if u2_final > u4_final:
            u2_cluster.append(i)
        else:
            u4_cluster.append(i)
    return (u2_cluster, u4_cluster)

def recalculation(df, u2_cluster, u4_cluster):
    u2_df = pd.DataFrame()
    u4_df = pd.DataFrame()
    
    for i in u2_cluster:
        u2_df = u2_df.append(df.iloc[i])
    for t in u4_cluster:
        u4_df = u4_df.append(df.iloc[t])
    
    u2_mean = u2_df.mean(axis = 0)
    
    u4_mean = u4_df.mean(axis = 0)
    
    return (u2_mean, u4_mean)
    
def error(final_df, u2_cluster, u4_cluster):
    count_df_u2 = pd.DataFrame()
    count_df_u2 = pd.DataFrame()
    
    final_df["Error"] = np.where(final_df["Class"] != final_df["Predicted_Class"], 'Yes', 'No')
    
    count_df_u2 = final_df.loc[(final_df['Class'] == 2) & final_df['Error'].str.contains('Yes'), :]
    
    
    count_df_u4 = final_df.loc[(final_df['Class'] == 4) & final_df['Error'].str.contains('Yes'), :]
    
    
    u2_error = (len(count_df_u2) / (len(u2_cluster))) * 100
    print ("\nAmount of Benign tumor samples: ", len(u2_cluster))
    u4_error = (len(count_df_u4) / (len(u4_cluster))) * 100
    print ("\nAmount of Malignant tumor samples: ", len(u4_cluster))
    
    print ("\n\nU2 Error Rate: ", round(u2_error,2))
    print ("\nU4 Error Rate: ", round(u4_error,2))
    
    combined_error = (len(count_df_u2)) + (len(count_df_u4))
    total_error = (combined_error / (len(final_df))) * 100
    print ("\nTotal Error Rate: ", round(total_error, 2))
    
    
main()
