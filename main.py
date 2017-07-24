import pandas as pd
import importer
import analyze

data = importer.importFolder('Data')
analyze.analyzeData(data,'Output/data.json') 
