import json

def load_data():
    try:
        with open('data/user.json', 'r') as f:
            return json.load(f)
    except:
        return []
    
def save_data(data):
    with open('data/user.json', 'w') as f:
        return json.dump(data, f)
    
def load_history():
    try:
        with open('data/history.json', 'r') as f:
            return json.load(f)
    except:
        return[]
    
def save_history(history):
    with open('data/history.json', 'w') as f:
        return json.dump(history, f)