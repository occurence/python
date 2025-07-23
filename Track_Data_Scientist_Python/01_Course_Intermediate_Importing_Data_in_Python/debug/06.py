# Import package
from urllib.request import urlopen, Request

# Specify the url: url
url = 'http://www.datacamp.com/teach/documentation'

# Packages the request, send the request and catch the response: r
r = urlopen(Request(url))

# Extract the response: text
# text = r.read().decode('utf-8')
text = r.read()
# text = r.text

# Print the html
print(text)