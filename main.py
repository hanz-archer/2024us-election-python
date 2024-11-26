import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

data = pd.read_csv("pres_polls.csv")

# Reshape data to have 'Party' and 'Votes' columns
data_long = pd.melt(data, id_vars=["State", "EV"], 
                    value_vars=["Dem", "GOP", "Ind"],
                    var_name="Party", value_name="Votes")

data_long["Votes"] = pd.to_numeric(data_long["Votes"], errors="coerce").fillna(0)

data_long = data_long.groupby(["State", "Party"], as_index=False).sum()

statewise = data_long.pivot(index="State", columns="Party", values="Votes")

# plotly create bar
fig = px.bar(data_long, x="State", y="Votes", color="Party", barmode="group",
             title="2024 U.S. Election Results by State")

# Matplot
statewise.plot(kind="bar", figsize=(10, 6), stacked=True)

# Customize graph
plt.title("2024 U.S. Election Results by State", fontsize=16)
plt.xlabel("State", fontsize=12)
plt.ylabel("Votes (in millions)", fontsize=12)
plt.legend(title="Party")
plt.xticks(rotation=45)
plt.tight_layout()

# Display
plt.savefig("election_results_graph.png")
plt.show()
fig.show()
