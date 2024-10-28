import json

headers = {
    'Content-type': 'text/',
}
data = {
    'name': 'Messi',
    'age': '18'
}

e = json.dumps(data)
with open('my_data.json', 'w') as f:
    f.write(json.dumps(data, indent=2))

with open('my_data.json', 'r') as f:
    read_data = json.loads(f.read())
    print(data == read_data)

