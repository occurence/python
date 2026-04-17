import os
import glob
extract_path = r"D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\extract"
imdb_path = os.path.join(extract_path, "aclImdb")
train_pos_path = os.path.join(imdb_path, "train", "pos")
train_neg_path = os.path.join(imdb_path, "train", "neg")












# Check the first file in the positive and negative review folders
first_pos_file = os.path.join(train_pos_path, os.listdir(train_pos_path)[0])
first_neg_file = os.path.join(train_neg_path, os.listdir(train_neg_path)[0])

with open(first_pos_file, 'r', encoding="utf-8") as f:
    print(f"First positive review:\n{f.read()}")

with open(first_neg_file, 'r', encoding="utf-8") as f:
    print(f"First negative review:\n{f.read()}")

# Verify review counts
print("Positive reviews count:", len(os.listdir(train_pos_path)))
print("Negative reviews count:", len(os.listdir(train_neg_path)))

def load_reviews_from_folder(folder, label):
    """Read all .txt files in a folder and assign a sentiment label."""
    reviews = []
    files = glob.glob(os.path.join(folder, "*.txt"))  # Corrected path
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            text = f.read().strip()
            if len(text) > 0:  # Only add non-empty reviews
                reviews.append((text, label))
            else:
                print(f"Empty review found in: {file}")  # Debug empty reviews
    return reviews
