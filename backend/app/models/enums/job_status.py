from enum import Enum


class JobStatus(Enum):
    DONE = "DONE"
    RUNNING = "RUNNING"
    WAITING = "WAITING"
    STOPPED = "STOPPED"
    PAUSED = "PAUSED"
    DELETED = "DELETED"
    ERROR = "ERROR"
