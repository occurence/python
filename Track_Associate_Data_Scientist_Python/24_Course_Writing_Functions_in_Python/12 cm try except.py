import os
import contextlib

@contextlib.contextmanager
def in_dir(directory):
  """Change current working directory to `directory`,
  allow the user to run some code, and change back.

  Args:
    directory (str): The path to a directory to work in.
  """
  current_dir = os.getcwd()
  os.chdir(directory)

  # Add code that lets you handle errors
  try:
    yield
  # Ensure the directory is reset,
  # whether there was an error or not
  finally:
    os.chdir(current_dir)

with in_dir('.'):
    # This code will run in the current directory
    print("Now in the current directory")
    # Add any code here that you want to run inside the current directory

    
# Once the block ends, the directory returns to the previous working directory
