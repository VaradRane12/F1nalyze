import pandas as pd
import pickle
import os
# Load the pickle file

for i in os.listdir(r"cache\2023\2023-04-02_Australian_Grand_Prix\2023-04-02_Race"):

    with open(r"cache\2023\2023-04-02_Australian_Grand_Prix\2023-04-02_Race\car_data.ff1pkl", "rb") as f:
        data = pickle.load(f)
    data = data["data"]
    # Assuming data is a tuple: (df1, df2, list_of_timedeltas)
    laps, timedeltas,_J = data

    # If you want to add the list of timedeltas as a DataFrame:
    # df3 = pd.DataFrame(timedeltas, columns=[ "Timedeltas"])

    # Optionally combine into one Excel file with multiple sheets:
    with pd.ExcelWriter("output.xlsx") as writer:
        laps.to_excel(writer, sheet_name="Lap Times", index=False)
        timedeltas.to_excel(writer, sheet_name="Timedeltas", index=False)
