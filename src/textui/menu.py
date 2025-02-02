
COMMANDS = {
    "1": "1 add tip",
    "2": "2 list tips",
    "3": "3 modify tip"
}

class Menu:
    def __init__(self, io, tip_service):
        self.io = io
        self.tip_service = tip_service

    def print_commands(self):
        for command in COMMANDS:
            self.io.write(COMMANDS[command])

    def run(self):
        self.io.write("Welcome dear reader")
        self.print_commands()

        while True:
            command = self.io.read("Command: ")
            if not command in COMMANDS:
                break
            if command == "1":
                name = self.io.read("name: ")
                url = self.io.read("url: ")
                try:
                    self.tip_service.create(name, url)
                except Exception as e:
                    self.io.write(e)

            if command == "2":
                tips = self.tip_service.get_all()
                for tip in tips:
                    id = tip[0]
                    name = tip[1].name
                    url = tip[1].url
                    self.io.write(f"id:{id} {name}, {url}")

            if command == "3":
                id = self.io.read("Tip id to edit: ")
                try:
                    old = self.tip_service.get_tip(id)
                    name = self.io.read("New name (leave blank to keep old): ")
                    if len(name) == 0:
                        name = old.name
                    url = self.io.read("New url (leave blank to keep old): ")
                    if len(url) == 0:
                        url = old.url
                    self.tip_service.edit(id, name, url)
                except Exception as e:
                    self.io.write(e)
                

