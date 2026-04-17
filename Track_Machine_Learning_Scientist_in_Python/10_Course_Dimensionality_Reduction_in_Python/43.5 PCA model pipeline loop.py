import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier

# Load dataset
poke_df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\10_Course_Dimensionality_Reduction_in_Python\datasets\pokemon.csv')
poke_df = poke_df.drop(['#', 'Name', 'Type 1', 'Type 2', 'Total', 'Generation'], axis=1)
X = poke_df.iloc[:, :-1]
y = poke_df.iloc[:, -1]

# Loop through different random states
best_acc = 0
best_state = None

for random_state in range(0, 100):  # Adjust the range if needed
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=random_state)

    # Build the pipeline
    pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('reducer', PCA(n_components=2)),
        ('classifier', RandomForestClassifier(random_state=0))
    ])

    # Fit the pipeline
    pipe.fit(X_train, y_train)

    # Evaluate
    accuracy = pipe.score(X_test, y_test)
    print(f'Random state {random_state}: {accuracy:.1%} test set accuracy')
print(X_train.iloc[0])

# 12,27,30,34,40,48,53,64,65,84