import pandas as pd

def load_and_plot_data(filename):
  """Load a data frame and plot each column.
  
  Args:
    filename (str): Path to a CSV file of data.
  
  Returns:
    pandas.DataFrame
  """
  df = pd.load_csv(filename, index_col=0)
  df.hist()
  return df

def has_docstring(func):
  """Check to see if the function 
  `func` has a docstring.

  Args:
    func (callable): A function.

  Returns:
    bool
  """
  return func.__doc__ is not None


# Call has_docstring() on the load_and_plot_data() function
ok = has_docstring(load_and_plot_data)

if not ok:
  print("load_and_plot_data() doesn't have a docstring!")
else:
  print("load_and_plot_data() looks ok")