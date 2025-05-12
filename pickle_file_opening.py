import pickle
import pprint
path = r"cache\2019\2019-03-17_Australian_Grand_Prix\2019-03-17_Race\_extended_timing_data.ff1pkl"
with open(path,'rb') as file:
    data = pickle.load(file)
pprint.pprint(data)