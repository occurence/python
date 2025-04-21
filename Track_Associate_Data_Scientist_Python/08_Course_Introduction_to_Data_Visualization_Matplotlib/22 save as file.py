import pandas as pd
import matplotlib.pyplot as plt

medals = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\08_Course_Introduction_to_Data_Visualization_Matplotlib\datasets\medals_by_country_2016.csv')

fig, ax = plt.subplots()
ax.bar(medals.index, medals['Gold'])
ax.set_xticklabels(medals.index, rotation=90)
ax.set_ylabel('Number of medals')
plt.show()

# Save as a PNG file
fig.savefig(r'generated_files\medals.png')

# Save as a PNG file with 300 dpi
fig.savefig(r'generated_files\medals_300dpi.png', dpi=300)