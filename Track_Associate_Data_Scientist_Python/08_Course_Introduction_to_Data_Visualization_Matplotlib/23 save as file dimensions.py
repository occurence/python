import pandas as pd
import matplotlib.pyplot as plt

medals = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\08_Course_Introduction_to_Data_Visualization_Matplotlib\datasets\medals_by_country_2016.csv')

fig, ax = plt.subplots()
ax.bar(medals.index, medals['Gold'])
ax.set_xticklabels(medals.index, rotation=90)
ax.set_ylabel('Number of medals')
# plt.show()

# Set figure dimensions and save as a PNG
fig.set_size_inches([3, 5])
fig.savefig(r'generated_files\figure_3_5.png')

# Set figure dimensions and save as a PNG
fig.set_size_inches([5, 3])
fig.savefig(r'generated_files\figure_5_3.png')

plt.show()