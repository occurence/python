# Import packages
import matplotlib.pyplot as plt
import seaborn as sns
import re
import pandas as pd
import json
from matplotlib.cm import get_cmap
from matplotlib.colors import to_hex

tweets_data_path = r'D:\STUDY\python\Track_Data_Scientist_Python\01_Course_Intermediate_Importing_Data_in_Python\datasets\tweets3.txt'
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweets_data, columns=['text','lang'])

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)

    if match:
        return True
    return False

# Initialize list to store tweet counts
[clinton, trump, sanders, cruz] = [0, 0, 0, 0]

# Iterate through df, counting the number of tweets in which
# each candidate is mentioned
for index, row in df.iterrows():
    clinton += word_in_text('clinton', row['text'])
    trump += word_in_text('trump', row['text'])
    sanders += word_in_text('sanders', row['text'])
    cruz += word_in_text('cruz', row['text'])

# Create DataFrame for plotting
data = {
    'candidate': ['clinton', 'trump', 'sanders', 'cruz'],
    'mentions': [clinton, trump, sanders, cruz]
}
plot_df = pd.DataFrame(data)

# Set seaborn style and custom purple palette
sns.set_style("whitegrid")
purple_shades = ['#B19CD9', '#9B59B6', '#8E44AD', '#6C3483']
sns.set_palette(purple_shades)

# Plot
ax = sns.barplot(data=plot_df, x='candidate', y='mentions')
ax.set(ylabel="Count", title="Mentions of Candidates in Tweets")
plt.show()
