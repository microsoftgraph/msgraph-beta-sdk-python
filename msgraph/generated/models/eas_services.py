from enum import Enum

class EasServices(Enum):
    None_escaped = "none",
    # Enables synchronization of calendars.
    Calendars = "calendars",
    # Enables synchronization of contacts.
    Contacts = "contacts",
    # Enables synchronization of email.
    Email = "email",
    # Enables synchronization of notes.
    Notes = "notes",
    # Enables synchronization of reminders.
    Reminders = "reminders",

