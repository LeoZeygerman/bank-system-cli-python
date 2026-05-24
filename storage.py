import json

def load_data():
    try:
        with open('data/user.json', 'r') as f:
            return json.load()
    except:
        return []
    
def save_data(data):
    with open('data/user.json', 'w') as f:
        return json.dump(data, f)