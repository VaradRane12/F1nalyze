import os
import pickle
import json
import pandas as pd
import numpy as np

def serialize(obj):
    """Recursively convert non-serializable types to JSON-safe types."""
    if isinstance(obj, pd.DataFrame):
        return obj.to_dict(orient="records")
    elif isinstance(obj, pd.Series):
        return obj.to_dict()
    elif isinstance(obj, pd.Timestamp):
        return obj.isoformat()
    elif isinstance(obj, pd.Timedelta):
        return str(obj)  # or use obj.total_seconds() if you prefer numeric
    elif isinstance(obj, (np.integer,)):
        return int(obj)
    elif isinstance(obj, (np.floating,)):
        return float(obj)
    elif isinstance(obj, (np.bool_, bool)):
        return bool(obj)
    elif isinstance(obj, (dict,)):
        return {str(k): serialize(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple, set)):
        return [serialize(v) for v in obj]
    else:
        try:
            json.dumps(obj)
            return obj
        except Exception:
            return str(obj)

def convert_pickle_files_to_json(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".ff1pkl"):
                file_path = os.path.join(root, file)
                json_path = os.path.splitext(file_path)[0] + ".json"

                try:
                    with open(file_path, "rb") as f:
                        data = pickle.load(f)
                except Exception as e:
                    print(f"❌ Failed to load {file}: {e}")
                    continue

                try:
                    cleaned_data = serialize(data)
                    with open(json_path, "w", encoding="utf-8") as out:
                        json.dump(cleaned_data, out, indent=2, ensure_ascii=False)
                    print(f"✅ Converted: {file} -> {json_path}")
                except Exception as e:
                    print(f"❌ Failed to convert {file}: {e}")

# Change this to your actual folder path
# Use the actual path where your files are located:
convert_pickle_files_to_json(r"..\cache\2023\2023-04-02_Australian_Grand_Prix\2023-04-02_Race")
