class Calendar:
    def __init__(self):
        self.events = []

    def add_event(self, date, name):
        self.events.append([date, name])

    def remove_event(self, name):
        for event in self.events:
            if event[1] == name:
                self.events.remove(event)
                break

    def show_events_in_month(self, month):
        for event in self.events:
            event_month = event[0].split("-")[1]
            if event_month == month:
                print(event[0] + ": " + event[1])

calendar = Calendar()
calendar.add_event("2025-10-08", "День народження")
calendar.add_event("2025-10-15", "Зустріч")
calendar.add_event("2025-11-01", "Відпустка")

calendar.remove_event("Зустріч")

print("Події у жовтні:")
calendar.show_events_in_month("10")
