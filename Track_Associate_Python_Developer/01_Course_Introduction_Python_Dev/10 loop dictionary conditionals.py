courses = {'LLM Concepts': 'AI', 'Introduction to Data Pipelines': 'Data Engineering', 'AI Ethics': 'AI', 'Introduction to dbt': 'Data Engineering', 'Writing Efficient Python Code': 'Programming', 'Introduction to Docker': 'Programming'}

# Loop through the dictionary's keys and values
for key, value in courses.items():
  
  # Check if the value is "AI"
  if value == "AI":
    print(key, "is an AI course")
  
  # Check if the value is "Programming"
  elif value == "Programming":
    print(key, "is a Programming course")
  
  # Otherwise, print that it is a "Data Engineering" course
  else:
    print(key, "is a Data Engineering course")