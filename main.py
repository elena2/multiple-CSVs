
#how to find path
import pandas as pd
import os
working_directory = os.getcwd()
print(working_directory)

#efficient way
df = pd.concat([pd.read_csv(f) for f in glob.glob('/Users/elenaprimes/Test_Folder/*.csv')], ignore_index = True)
df.to_csv(r'/Users/elenaprimes/Results_Folder/Test1.csv', index = False)

#longer way
import pandas as pd
import os
import glob

path = "/Users/elenaprimes/Test_Folder/"
all_files = glob.glob(path + "/*.csv")
dfs = pd.DataFrame()

for filename in all_files:
    # file = '/Users/elenaprimes/Test_Folder/March2021.csv'
    df = pd.read_csv(filename, index_col=None, header=0)
    print(df.shape)
    dfs = pd.concat([dfs,df], axis=0, ignore_index = True)


    # pd.concat - attach two dataframes to each other on whatever basis
    # name of dataframes -> [ df, dfs]
    # axis = 1 - attach by column [0,0,0] , [1,2,1] -> [0,0,0,1,2,1]
    # axis = 0 attach by row [0,0,0] , [1,2,1] -> [[0,0,0], [1,2,1]]
    
