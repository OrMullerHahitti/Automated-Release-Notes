# app/services/base_service.py
from abc import ABC, abstractmethod
from typing import List

class BaseReop(ABC):
    @abstractmethod
    async def fetch_commits(self, start_date: str, end_date: str) -> List[Commit]:
        pass

    @abstractmethod
    async def fetch_repositories(self) -> List[dict]:
        pass