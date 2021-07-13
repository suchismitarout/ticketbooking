class User:
    def __init__(self, name, tickets):
        self.name = name
        self.tickets = tickets

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def set_tickets(self, tickets):
        self.tickets = tickets

    def get_tickets(self):
        return self.tickets



