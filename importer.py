import pandas as pd
from os import listdir
from os.path import isfile, join

def importFolder(folder):
    onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
    print('Attempting to load: '+str(onlyfiles))
    dataframes = []
    for file in onlyfiles:
        try:
            final = pd.read_json('Data/'+file)['games']
            dataframes.append(final)
        except(e):print(e)
    out = pd.concat(dataframes)
    print('Succesfully loaded data files. Total games: '+str(len(out)))
    return out