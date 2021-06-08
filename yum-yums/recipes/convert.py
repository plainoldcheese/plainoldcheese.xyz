import markdown
import os

print(os.getcwd())

with open('recipes/mayo.md', 'r') as f:
    text = f.read()
    html = markdown.markdown(text)

with open('recipes/mayo.html', 'w') as f:
    f.write(html)