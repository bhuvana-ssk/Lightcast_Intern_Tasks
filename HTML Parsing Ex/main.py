from bs4 import BeautifulSoup
import json

def html_to_json(input_html):
    soup = BeautifulSoup(input_html, 'html.parser')

    body_content = []
    if soup.body:
        body_content = [element.text for element in soup.body.find_all(recursive=False)]

    json_data = {
        'title': soup.title.text if soup.title else None,
        'body_content': body_content
    }
    return json_data

html_input_file = './input.html'
json_output_file = './output.json'

with open(html_input_file, 'r', encoding='utf-8') as file:
    html_content = file.read()

json_output = html_to_json(html_content)

print(json.dumps(json_output, indent=2))
with open(json_output_file, 'w', encoding='utf-8') as json_file:
    json.dump(json_output, json_file, indent=2)
