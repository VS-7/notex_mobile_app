import http.client
import json

API_URL = "apinotex-production.up.railway.app"

class APIClient:
    def __init__(self):
        self.conn = http.client.HTTPSConnection(API_URL)

    def login(self, email, password):
        login_data = json.dumps({"email": email, "password": password})
        headers = {'Content-type': 'application/json'}
        self.conn.request('POST', '/login', body=login_data, headers=headers)
        response = self.conn.getresponse()

        response_data = response.read().decode()

        print(f"Response status: {response.status}")  # Log do status
        print(f"Response data: {response_data}")      # Log do conteúdo da resposta

        if response.status == 200 and response.getheader('Content-Type') == 'application/json':
            return json.loads(response_data)
        else:
            return {"status": response.status, "message": response_data}

    def register(self, name, email, password):
        register_data = json.dumps({"name": name, "email": email, "password": password})
        headers = {'Content-type': 'application/json'}
        self.conn.request('POST', '/register', body=register_data, headers=headers)
        return self.conn.getresponse()

    def get_notes(self, user_id):
        self.conn.request('GET', f'/notes/{user_id}')
        response = self.conn.getresponse()
        return json.loads(response.read().decode())

    def create_note(self, note):
        headers = {'Content-type': 'application/json'}
        self.conn.request('POST', '/notes', body=json.dumps(note), headers=headers)
        return self.conn.getresponse()

    def update_note(self, note_id, note):
        headers = {'Content-type': 'application/json'}
        self.conn.request('PUT', f'/notes/{note_id}', body=json.dumps(note), headers=headers)
        return self.conn.getresponse()

    def delete_note(self, note_id):
        self.conn.request('DELETE', f'/notes/{note_id}')
        return self.conn.getresponse()