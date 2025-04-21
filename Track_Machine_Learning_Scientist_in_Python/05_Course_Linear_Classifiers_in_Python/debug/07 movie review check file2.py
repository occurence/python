import os

extract_path = r"D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\extract"
train_pos = os.path.join(extract_path, "aclImdb", "train", "pos")
train_neg = os.path.join(extract_path, "aclImdb", "train", "neg")

print("Train positive path:", train_pos)
print("Train negative path:", train_neg)
print("Sample positive files:", os.listdir(train_pos)[:5])  # List first 5 files
print("Sample negative files:", os.listdir(train_neg)[:5])  # List first 5 files


import glob

def load_reviews_from_folder(folder, label):
    """Read all .txt files in a folder and assign a sentiment label."""
    reviews = []
    files = glob.glob(os.path.join(folder, "*.txt"))  # Get all .txt files
    print(f"Loading {len(files)} reviews from {folder}")  # Print how many files

    for i, file in enumerate(files[:5]):  # Show first 5 files only for debugging
        with open(file, "r", encoding="utf-8") as f:
            text = f.read().strip()
            if not text:
                print(f"⚠ Empty review found: {file}")  # Warn about empty files
            else:
                print(f"📄 Review {i+1} from {folder}:\n{text[:100]}...\n")  # Print first 100 chars
            reviews.append((text, label))

    return reviews

pos_reviews = load_reviews_from_folder(train_pos, 1)
neg_reviews = load_reviews_from_folder(train_neg, 0)

import pandas as pd

# Convert to DataFrame
df_train = pd.DataFrame(pos_reviews + neg_reviews, columns=["review", "label"])

print("Total reviews loaded:", len(df_train))
print(df_train.head())  # Print sample reviews

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words='english', min_df=1, max_df=1.0)
X_train = vectorizer.fit_transform(df_train["review"])
print("Vocabulary size:", len(vectorizer.get_feature_names_out()))
