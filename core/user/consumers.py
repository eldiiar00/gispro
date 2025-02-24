# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import UserLocation

class LocationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("locations", self.channel_name)
      
        locations = await self.get_locations_from_db()
        for location in locations:
            await self.send(text_data=json.dumps({
        "user_id": location.user_id,
        "user_nickname": location.user_nickname,
        "latitude": location.latitude,
        "longitude": location.longitude,
        }))

    async def receive(self, text_data):
        data = json.loads(text_data)
        user_id = data['user_id']
        user_nickname = data['user_nickname']
        latitude = data['latitude']
        longitude = data['longitude']
        # Сохраняем или обновляем данные в базе данных
        await self.save_or_update_location(user_id, user_nickname, latitude, longitude)

        # Отправляем данные всем в группе
        await self.channel_layer.group_send(
            "locations",
                {
                "type": "location_update",
                "user_id": user_id,
                "user_nickname": user_nickname,
                "latitude": latitude,
                "longitude": longitude,
                }
            )
    @database_sync_to_async
    def get_locations_from_db(self):
        # Получаем все текущие местоположения из базы данных
        return list(UserLocation.objects.all())

    @database_sync_to_async
    def save_or_update_location(self, user_id, user_nickname, latitude, longitude):
        # Обновляем или создаем запись
        UserLocation.objects.update_or_create(
            user_id=user_id,
            defaults={
                'user_nickname': user_nickname,
                'latitude': latitude,
                'longitude': longitude,
            }
        )

    async def location_update(self, event):
        await self.send(text_data=json.dumps({
            "user_id": event["user_id"],
            "user_nickname": event["user_nickname"],
            "latitude": event["latitude"],
            "longitude": event["longitude"],
    }))