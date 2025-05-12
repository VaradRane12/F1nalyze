import fastf1

fastf1.Cache.enable_cache('cache') 

year = 2023
gp = 'Australian Grand Prix'
session_type = 'R'  
try:
    session = fastf1.get_session(year, gp, session_type)
    session.load(telemetry=True, weather=False) 
    print("Session loaded from cache successfully.")
    print(session.get_driver("HAM")["HeadshotUrl"])
except Exception as e:
    print(f"Error loading session: {e}")
