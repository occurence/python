import numpy as np

def create_sequences(df, seq_length):
    xs, ys = [], []
    # Iterate over data indices
    for i in range(len(df) - seq_length):
      	# Define inputs
        x = df.iloc[i:(i+seq_length), 1]
        # Define target
        y = df.iloc[i+seq_length, 1]
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)

print("You can now use create_sequences() to create a set of training or testing examples for the model, where each example consists of an input of seq_length consecutive data points, and the single target, the following data point. You'll put this into action in the next exercise!")