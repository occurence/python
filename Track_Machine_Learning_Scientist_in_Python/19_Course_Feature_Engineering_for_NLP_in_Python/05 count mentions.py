import pandas as pd
import matplotlib.pyplot as plt

tweets = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\19_Course_Feature_Engineering_for_NLP_in_Python\datasets\russian_tweets.csv')

# Function that returns number of mentions in a string
def count_mentions(string):
	# Split the string into words
    words = string.split()
    
    # Create a list of words that are mentions
    mentions = [word for word in words if word.startswith('@')]
    
    # Return number of mentions
    return(len(mentions))

# Create a feature mention_count and display distribution
tweets['mention_count'] = tweets['content'].apply(count_mentions)
tweets['mention_count'].hist()
plt.title('Mention count distribution')
plt.show()

print("You now have a good grasp of how to compute various types of summary features. In the next lesson, we will learn about more advanced features that are capable of capturing more nuanced information beyond simple word and character counts.")