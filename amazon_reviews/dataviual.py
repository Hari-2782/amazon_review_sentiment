import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("sentiment_analysis.csv")
sns.histplot(df["sentiment"], bins=20, kde=True)
plt.title("Sentiment Distribution of Amazon Reviews")
plt.show()
