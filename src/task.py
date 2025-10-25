""" Module presenting a single task"""

from enum import Enum
import datetime

class Task:
    """ Class representing single task

    Attributes:
        _id - A unique identifier for the task
        _description - A short description of the task
        _status - The status of the task (todo, in-progress, done)
        _createdAt - The date and time when the task was created
        _updatedAt - The date and time when the task was last updated
    """
    def __init__(self, id: int, description: str, status: str = 'todo') -> None:
        self._id: int = id
        self._description:str = description
        self._status: str = status
        self._createdAt: datetime.datetime = datetime.datetime.now()
        self._updatedAt: datetime.datetime  = self._createdAt

    """Setters"""

    def setDescription(self, description: str) -> None:
        self._description = description

    def setStatus(self, status: str) -> None:
        self._status = status

    def setUpdateDateAndTime(self, updatedAt: datetime.datetime ) -> None:
        self._updatedAt = updatedAt
    
    """Getters"""

    def getId(self) -> int:
        return self._id
    
    def getDescription(self) -> str:
        return self._description
    
    def getStatus(self) -> str:
        return self._status
    
    def getCreationDateAndTime(self) -> datetime.datetime :
        return self._createdAt
    
    def getUpdateDateAndTime(self) -> datetime.datetime :
        return self._updatedAt
    
    """Methods"""

    def print(self) -> None:
        print(f"[{self._id}]  {self._description}\t{self._status}")
    
        