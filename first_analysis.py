import pandas as pd
import matplotlib.pyplot as plt
data = {
"City": ["Dublin", "Cork", "Galway", "Limerick"],
"Value": [42, 31, 27, 22]
}
df = pd.DataFrame(data)
print(df)
df.plot(
x="City",
y="Value",
kind="bar",
legend=False,
title="My First PAI Visualisation"
)
plt.ylabel("Value")
plt.tight_layout()
plt.show()