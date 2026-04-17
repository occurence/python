def read_files():
  file_contents = None
  
  def save_contents(filename):
    # Add a keyword that lets us modify file_contents
    nonlocal file_contents
    if file_contents is None:
      file_contents = []
    with open(filename) as fin:
      file_contents.append(fin.read())
      
  for filename in [r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\24_Course_Writing_Functions_in_Python\datasets\1984.txt', 
                   r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\24_Course_Writing_Functions_in_Python\datasets\MobyDick.txt', 
                   r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\24_Course_Writing_Functions_in_Python\datasets\CatsEye.txt']:
    save_contents(filename)
    
  return file_contents

print('\n'.join(read_files()))