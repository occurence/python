from textanalysis.textanalysis import count_words

# Count the number of positive words
nb_positive_words = count_words(r'D:\STUDY\python\Track_Data_Scientist_Python\03_Track_Developing_Python_Packages\01 script package\hotel-reviews.txt', ['good', 'great'])

# Count the number of negative words
nb_negative_words = count_words(r'D:\STUDY\python\Track_Data_Scientist_Python\03_Track_Developing_Python_Packages\01 script package\hotel-reviews.txt', ['bad','awful'])

print("{} positive words.".format(nb_positive_words))
print("{} negative words.".format(nb_negative_words))