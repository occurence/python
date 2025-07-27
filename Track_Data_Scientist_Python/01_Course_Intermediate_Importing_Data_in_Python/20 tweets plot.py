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

# # Set seaborn style
# # sns.set(color_codes=True)
# # sns.set_theme(style="dark")
# # sns.set_palette('RdBu')
# # sns.set_palette(['#39A7D0', '#36ADA4'])
# sns.set_style("whitegrid")
# # sns.set_palette('Purples')
# sns.set_palette(['#B19CD9', '#9B59B6', '#8E44AD', '#6C3483'])
# # purple_shades = [to_hex(get_cmap('Purples')(i)) for i in [0.4, 0.55, 0.7, 0.85]]
# # sns.set_palette(purple_shades)

# # Create a list of labels:cd
# cd = ['clinton', 'trump', 'sanders', 'cruz']

# # Plot the bar chart
# ax = sns.barplot(x=cd, y=[clinton, trump, sanders, cruz])
# # ax = sns.catplot(x=cd, y=[clinton, trump, sanders, cruz], palette='Purples')
# ax.set(ylabel="count")
# plt.show()


data = {
    'candidate': ['clinton', 'trump', 'sanders', 'cruz'],
    'mentions': [clinton, trump, sanders, cruz]
}
plot_df = pd.DataFrame(data)

# Plot using Matplotlib instead to fully control color per bar
# plt.style.use('seaborn-whitegrid')

# Colors (different purple shades)
colors = ['#B19CD9', "#CC95E2", "#9E5FB9", '#6C3483']

# Plot
plt.bar(plot_df['candidate'], plot_df['mentions'], color=colors)
plt.ylabel("Count")
plt.title("Mentions of Candidates in Tweets")
plt.show()
