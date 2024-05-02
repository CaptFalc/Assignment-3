import csv
import pandas as pd
from math import isnan

sampleID = 'SM16O-VJARN'
jacSims = []

df = pd.read_csv('mistCompSheet.csv')
df.drop(columns = ['Registration Option'], inplace=True)
mistDict = df.set_index('MIST ID').apply(list, axis=1).to_dict()

mistDict= {key: [value for value in values if pd.notna(value)] for key, values in mistDict.items()}



def jaccardSimilarity(mistID):
    refSet = set()
    testSet = set()
    for x in mistDict[sampleID]:
        refSet.add(x)
    for x in mistDict[mistID]:
        testSet.add(x)

    intersection = refSet.intersection(testSet)
    union = refSet.union(testSet)
    jaccardSimilarity = float(len(intersection)) / float(len(union)) if union != 0 else 0 

    return [mistID, jaccardSimilarity]

for x in mistDict:
    jacSims.append(jaccardSimilarity(x))

jacSims = sorted(jacSims, key=lambda tup: tup[1], reverse=True)
print("The 10 competitors with the most similar competitions to the sample student are: ", jacSims[1:11])