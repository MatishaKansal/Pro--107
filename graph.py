import csv
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv("data.csv")

mean = df.groupby("level")["attempt"].mean()


fig = px.scatter(df, x = "level", y= "attempt", color="attempt", size="student_id")

fig.show()
