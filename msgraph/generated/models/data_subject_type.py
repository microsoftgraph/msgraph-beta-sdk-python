from enum import Enum

class DataSubjectType(str, Enum):
    Customer = "customer",
    CurrentEmployee = "currentEmployee",
    FormerEmployee = "formerEmployee",
    ProspectiveEmployee = "prospectiveEmployee",
    Student = "student",
    Teacher = "teacher",
    Faculty = "faculty",
    Other = "other",
    UnknownFutureValue = "unknownFutureValue",

