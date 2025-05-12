import pickle
import sys
import os
from pprint import pprint

try:
    import pandas as pd
except ImportError:
    print("❌ pandas is required. Install it using `pip install pandas`.")
    sys.exit(1)


def convert_to_dataframe(data):
    try:
        if isinstance(data, pd.DataFrame):
            return data
        elif isinstance(data, (list, dict)):
            return pd.DataFrame(data)
        else:
            return pd.DataFrame([data])  # wrap primitive/unknown into a DataFrame
    except Exception as e:
        print(f"❌ Could not convert to DataFrame: {e}")
        return None


def view_and_export_pickle(file_path, output_dir="test_output"):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    try:
        with open(file_path, 'rb') as f:
            data = pickle.load(f)

        print(f"\n📂 Loaded: {file_path}\n")
        df = convert_to_dataframe(data)

        if df is not None:
            print("🔍 Converted to DataFrame:\n")
            print(df.head())
            print(f"\n🧾 Shape: {df.shape}")

            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, "output.xlsx")
            df.to_excel(output_path, index=False)

            print(f"\n✅ Exported to Excel: {output_path}")
        else:
            print("❌ Failed to convert data to DataFrame.")

    except Exception as e:
        print(f"❌ Failed to load or export pickle file: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pkl_to_excel.py <path_to_pickle_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    view_and_export_pickle(file_path)
