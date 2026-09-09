#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_parquet("data/RMDC26_Beginner_Tier_test.parquet")

print(df.shape)
print(df.head())
print(df.dtypes)
print(df.describe())

print(df["filt"].value_counts())
print(df["saturation_flag"].value_counts())

print("number of stars:", df["name"].nunique())
print("epochs per star:", df.groupby("name").size().mean())
print("time range:", df["bjd"].min(), df["bjd"].max())
print("mag range:", df["mag"].min(), df["mag"].max())
print("median mag error:", df["mag_err"].median())

#%%
plt.figure()
plt.scatter(df["l_deg"], df["b_deg"], s=1)
plt.xlabel("l (deg)")
plt.ylabel("b (deg)")
plt.title("Star positions")
plt.savefig("figures/sky.png")

plt.figure()
plt.hist(df["mag"], bins=100)
plt.xlabel("mag")
plt.ylabel("count")
plt.title("Magnitude distribution")
plt.savefig("figures/mag_hist.png")

plt.figure()
plt.scatter(df["mag"], df["mag_err"], s=1, alpha=0.1)
plt.yscale("log")
plt.xlabel("mag")
plt.ylabel("mag_err")
plt.title("Error vs magnitude")
plt.savefig("figures/err_vs_mag.png")

star = df[df["name"] == "RMDC26_000001"]
star = star[star["filt"] == "F146"]

plt.figure(figsize=(10, 4))
plt.scatter(star["bjd"], star["mag"], s=1)
plt.gca().invert_yaxis()
plt.xlabel("BJD")
plt.ylabel("mag")
plt.title("Light curve RMDC26_000001 (F146)")
plt.savefig("figures/light_curve.png")

plt.show()

# %%
