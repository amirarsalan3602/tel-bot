import requests


class Connections:
    def __init__(self):
        self.server = "103.216.61.88"

    def free_account(self, path: str = "Free_acc", uuid: str = None, token: str = None, EXP: str = None):
        response = requests.post(url=f"http://{self.server}/{path}/{uuid}/{EXP}")
        return response.json()[-1]


connections = Connections()
# a = Connection()
# print(a.free_account(uuid="3243234", EXP="3d"))
