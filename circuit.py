import fastf1
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load session and circuit info
session = fastf1.get_session(2025, 'Bahrain', 'Q')
session.load()
Circuit_Info = session.get_circuit_info()

# Convert nested dictionaries to DataFrames
corners = pd.DataFrame(Circuit_Info.corners)
marshal_lights = pd.DataFrame(Circuit_Info.marshal_lights)
marshal_sectors = pd.DataFrame(Circuit_Info.marshal_sectors)
rotation_angle = Circuit_Info.rotation


# Vectorized rotate function
def rotate(df, angle_deg):
    theta = np.radians(angle_deg)
    x_rot = df['X'] * np.cos(theta) - df['Y'] * np.sin(theta)
    y_rot = df['X'] * np.sin(theta) + df['Y'] * np.cos(theta)
    df['X_rot'] = x_rot
    df['Y_rot'] = y_rot
    return df

# Apply rotation
corners = rotate(corners, rotation_angle)
marshal_lights = rotate(marshal_lights, rotation_angle)
marshal_sectors = rotate(marshal_sectors, rotation_angle)

# Plot
plt.figure(figsize=(12, 10))
plt.plot(corners['X_rot'], corners['Y_rot'], '-o', label='Track')
plt.scatter(marshal_lights['X_rot'], marshal_lights['Y_rot'], color='yellow', label='Marshal Lights', s=50, marker='^')
plt.scatter(marshal_sectors['X_rot'], marshal_sectors['Y_rot'], color='red', label='Marshal Sectors', s=50, marker='s')

# Label corners
for i, row in corners.iterrows():
    plt.text(row['X_rot'], row['Y_rot'], f"{int(row['Number'])}", fontsize=8, ha='right')

plt.title("Race Track Map")
plt.xlabel("X (rotated)")
plt.ylabel("Y (rotated)")
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.tight_layout()
plt.show()
