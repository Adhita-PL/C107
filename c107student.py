import pandas as pd
import plotly.graph_objects as go
import csv

df = pd.read_csv("data1.csv")
student_df = df.loc[df["student_id"] == "TRL_987"] 
print(student_df.groupby("level")["attempt"].mean())

fig = go.Figure(go.Bar(
    x = student_df.groupby("level")["attempt"].mean(),
    y = ["Level 1", "Level 2", "Level 3", "Level 4"], 
    orientation = "h"
))
fig.show() 