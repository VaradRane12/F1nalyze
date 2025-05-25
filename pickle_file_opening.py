import pickle
import pprint
path = r"cache\2023\2023-04-02_Australian_Grand_Prix\2023-04-02_Race\car_data.ff1pkl"
with open(path,'rb') as file:
    data = pickle.load(file)
pprint.pprint(len(data["data"]))
for i in data['data']:
    print(i)
# pprint.pprint(data["data"])