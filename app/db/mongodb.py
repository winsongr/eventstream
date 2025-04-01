from motor.motor_asyncio import AsyncIOMotorClient
from ..config import settings


class MongoDB:
    client: AsyncIOMotorClient = None

    async def connect_to_database(self):
        self.client = AsyncIOMotorClient(settings.mongodb_url)
        self.db = self.client[settings.database_name]

    async def close_database_connection(self):
        if self.client:
            self.client.close()


db = MongoDB()
