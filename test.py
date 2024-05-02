import codecs
from bs4 import BeautifulSoup

# Open the file using codecs
path = 'index.html'
html = codecs.open(path)

# Detect all HTML tags
soup = BeautifulSoup(html)
for script in soup(["script", "style"]):
    script.decompose()