from enum import Enum


class UserScenario(str, Enum):
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"
    GET_BY_ID = "get_by_id"
