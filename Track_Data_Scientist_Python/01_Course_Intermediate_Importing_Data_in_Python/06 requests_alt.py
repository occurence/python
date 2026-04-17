# Import package
import requests

# Specify the url: url
url = 'http://www.datacamp.com/teach/documentation'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# Packages the request, send the request and catch the response: r
# r = requests.get(url)
r = requests.get(url, headers=headers)

# Extract the response: text
text = r.text
# text = r.read().decode('utf-8')

# Print the html
print(text)