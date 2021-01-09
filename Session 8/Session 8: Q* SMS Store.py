class SMSStore:
    def __init__(self):
        self.inbox = []
    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        self.inbox.append(((False, from_number, time_arrived, text_of_SMS)))
    def message_count(self):
        return len(self.inbox)
    def get_unread_indexes(self):
        return list(filter(lambda x: x[0] is False, self.inbox))
    def get_message(self, i):
        if len(self.inbox) > i:
            self.inbox[i] = (True, self.inbox[i][1], self.inbox[i][2], self.inbox[i][3])
            return self.inbox[i][1:]
        return None
    def delete(self, i):
        del self.inbox[i]
    def clear(self):
        self.inbox = []
