import os
import fastf1
import pandas as pd

# Ensure cache folder exists
os.makedirs('./cache', exist_ok=True)

# Enable FastF1 cache
fastf1.Cache.enable_cache('./cache')

fastf1.Cache.enable_cache('./cache')

def get_season_standings(year):
    race_names = fastf1.get_event_schedule(year)
    driver_points = {}

    for _, race in race_names.iterrows():
        
        try:
            session = fastf1.get_session(year, race['RoundNumber'], 'R')  # 'R' for Race
            session.load()
            results = session.results
        except Exception as e:
            print(f"Skipping round {race['RoundNumber']} due to error: {e}")
            continue

        for i, row in results.iterrows():
            print(row)
            driver = row['DriverNumber']
            points = row['Points']

            if driver not in driver_points:
                driver_points[driver] = {
                    'Name': f"{row["FullName"]}",
                    'Constructor': row['TeamName'],
                    'Points': 0,
                    'Wins': 0
                }

            driver_points[driver]['Points'] += points
            if row['Position'] == 1:
                driver_points[driver]['Wins'] += 1

    df = pd.DataFrame.from_dict(driver_points, orient='index')
    df = df.sort_values(by='Points', ascending=False).reset_index().rename(columns={'index': 'Code'})
    df.index += 1  # For ranking positions
    return df

# Example usage:
standings_df = get_season_standings(2023)
print(standings_df)
