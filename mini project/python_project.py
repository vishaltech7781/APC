import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import messagebox

# Function to load data
def load_data():
    global df
    try:
        df = pd.read_csv("data_all.csv")
        df = df.dropna(subset=['city', 'pollutant_id', 'pollutant_avg'])
        df['last_update'] = pd.to_datetime(df['last_update'], errors='coerce')
        messagebox.showinfo("Success", "Dataset Loaded Successfully ✅")
    except:
        messagebox.showerror("Error", "File Not Found or Invalid Format")

# 1️⃣ City-wise pollution graph
def plot_city_pollution():
    city_pollution = df.groupby('city')['pollutant_avg'].mean().sort_values(ascending=False)
    plt.figure(figsize=(12,6))
    city_pollution.head(15).plot(kind='bar', color='teal')
    plt.title("Top 15 Cities with Highest Average Pollution Levels")
    plt.ylabel("Average Pollutant Concentration (µg/m³)")
    plt.xlabel("City")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# 2️⃣ Pollutant category distribution
def plot_pollutant_distribution():
    plt.figure(figsize=(8,6))
    sns.countplot(y='pollutant_id', data=df, order=df['pollutant_id'].value_counts().index, palette="viridis")
    plt.title("Distribution of Recorded Pollutant Types")
    plt.xlabel("Count of Records")
    plt.ylabel("Pollutant Type")
    plt.tight_layout()
    plt.show()

# 3️⃣ Heatmap
def plot_heatmap():
    pivot = df.pivot_table(values='pollutant_avg', index='city', columns='pollutant_id', aggfunc='mean')
    plt.figure(figsize=(10,6))
    sns.heatmap(pivot, cmap="coolwarm", linewidths=0.5)
    plt.title("Heatmap of Pollutant Concentration by City")
    plt.xlabel("Pollutant Type")
    plt.ylabel("City")
    plt.show()

# 4️⃣ Pollution Hotspot Map
def plot_map():
    plt.figure(figsize=(10,6))
    sns.scatterplot(data=df, x='longitude', y='latitude', hue='pollutant_avg', size='pollutant_avg', palette='coolwarm')
    plt.title("Geographic Distribution of Pollution Levels")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.legend(title="Pollution Level")
    plt.tight_layout()
    plt.show()

# ---------------- GUI Window ----------------
root = tk.Tk()
root.title("Air Pollution Data Visualization")
root.geometry("1080x720")
root.config(bg="#e6e6fa")

title_label = tk.Label(root, text="Air Pollution Analysis Dashboard", font=("Arial", 14, "bold"), bg="#e0f7fa")
title_label.pack(pady=10)

# Buttons
btn1 = tk.Button(root, text="Load Dataset", command=load_data, width=25, height=2, bg="#0288d1", fg="black")
btn1.pack(pady=5)

btn2 = tk.Button(root, text="City-wise Avg Pollution (Bar Chart)", command=plot_city_pollution, width=25, height=2, bg="#0288d1", fg="black")
btn2.pack(pady=5)

btn3 = tk.Button(root, text="Pollutant Type Distribution", command=plot_pollutant_distribution, width=25, height=2, bg="#0288d1", fg="black")
btn3.pack(pady=5)

btn4 = tk.Button(root, text="Heatmap (City vs Pollutant)", command=plot_heatmap, width=25, height=2, bg="#0288d1", fg="black")
btn4.pack(pady=5)

btn5 = tk.Button(root, text="Pollution Hotspots Map", command=plot_map, width=25, height=2, bg="#0288d1", fg="black")
btn5.pack(pady=5)

root.mainloop()
