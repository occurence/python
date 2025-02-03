import tarfile
import os

# Paths
tar_path = r"D:\STUDY\python\Track_Macine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\aclImdb_v1.tar.gz"  # Replace with actual path
extract_path = r"D:\STUDY\python\Track_Macine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\extract"  # Where to extract
os.makedirs(extract_path, exist_ok=True)

# # Extract .tar file
# with tarfile.open(tar_path, 'r') as tar:
#     tar.extractall(path=extract_path)

# print("Extraction complete. Files are in:", extract_path)

# with tarfile.open(tar_path, 'r:gz') as tar:
#     tar.extractall(path=extract_path)

import os

extracted_files = os.listdir(extract_path)
print(extracted_files)

['train', 'test', 'imdb.vocab', 'imdbEr.txt']

import pandas as pd
import glob

def load_reviews_from_folder(folder, label):
    """Read all .txt files in a folder and assign a sentiment label."""
    reviews = []
    files = glob.glob(folder + "/*.txt")  # Get all .txt files
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            reviews.append((f.read(), label))
    return reviews

# Paths
train_pos = os.path.join(extract_path, "train", "pos")
train_neg = os.path.join(extract_path, "train", "neg")

# Load train data
pos_reviews = load_reviews_from_folder(train_pos, 1)
neg_reviews = load_reviews_from_folder(train_neg, 0)

# Convert to DataFrame
df_train = pd.DataFrame(pos_reviews + neg_reviews, columns=["review", "label"])
print(df_train.head())  # Preview data


from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(df_train["review"])  # Fit on training data

def get_features(review):
    return vectorizer.transform([review])  # Now works!


from sklearn.linear_model import LogisticRegression

y_train = df_train["label"].values  # Convert labels to NumPy array

lr = LogisticRegression(max_iter=500)
lr.fit(X_train, y_train)

# Predict sentiment for a review
review1 = "LOVED IT! This movie was amazing. Top 10 this year."
review1_features = get_features(review1)
print("Probability of positive review:", lr.predict_proba(review1_features)[0,1])








import os

extract_path = r"D:\STUDY\python\Track_Macine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\extract"

# List main folder contents
print(os.listdir(extract_path))  

imdb_path = os.path.join(extract_path, "aclImdb")
print(os.listdir(imdb_path))  

['train', 'test', 'imdb.vocab', 'imdbEr.txt']

train_pos_path = os.path.join(imdb_path, "train", "pos")
train_neg_path = os.path.join(imdb_path, "train", "neg")

print("Positive reviews count:", len(os.listdir(train_pos_path)))
print("Negative reviews count:", len(os.listdir(train_neg_path)))

import pandas as pd
import glob

def load_reviews_from_folder(folder, label):
    """Read all .txt files in a folder and assign a sentiment label."""
    reviews = []
    files = glob.glob(os.path.join(folder, "*.txt"))  # Corrected path
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            text = f.read().strip()
            if text:  # Only add non-empty reviews
                reviews.append((text, label))
    return reviews

# Load data
pos_reviews = load_reviews_from_folder(train_pos_path, 1)
neg_reviews = load_reviews_from_folder(train_neg_path, 0)

# Convert to DataFrame
df_train = pd.DataFrame(pos_reviews + neg_reviews, columns=["review", "label"])

print("Total reviews loaded:", len(df_train))
print(df_train.head())  # Should show some data

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(df_train["review"])  # Should work now!

print(df_train["review"].head(10))





