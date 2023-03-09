# Python
import requests
from typing import Union, TypeAlias
import time
import asyncio

# Django
from django.core.management.base import BaseCommand
from django.db import transaction

# Apps
from asynics.models import Station


dtype: TypeAlias = list[dict[str, Union[str, int]]]

class Command(BaseCommand):
    """Class to create data."""
    
    help = 'Custom command for filling up database.'

    
    def generate_data(self, *args: tuple, **kwargs: dict) -> None:
        
        async def create_100_objs(objs: list[dict]):
            stations: list[Station] = []
            
            obj: dict
            for obj in objs:
                station = Station(**obj)
                stations.append(station)
            try:
                with transaction.atomic() as tr:
                    Station.objects.bulk_create(stations)
            except Exception as e:
                print("ERROR TASK:", e)

            return time.localtime()
        
        def finish(
            future: asyncio.Future[list], 
            *args: tuple, 
            **kwargs: dict
        ) -> None:
            print("FINISH")

        async def main(objs: list[dict]):
            tasks: list[asyncio.Task] = []

            i: int
            for i in range(0, len(objs) - 100, 100):
                task: asyncio.Task = asyncio.create_task(
                    create_100_objs(objs[i:i+100])
                )
                tasks.append(task)

            fut: asyncio.Future = asyncio.gather(*tasks)
            fut.add_done_callback(finish)
        
        
        url: str = (
            "https://radio-world-75-000-worldw"
            "ide-fm-radio-stations.p.rapidapi.com/api.php"
        )
        querystring: requests.sessions._Params = {
            "count": "5000",
            "page": "1",
            "radios": ""
        }
        headers: requests.sessions._HeadersUpdateMapping = {
            "X-RapidAPI-Key": "d16d7c4e93msh3ca9ddc5ef24a17p16f35bjsn73c95e2203fa",
            "X-RapidAPI-Host": "radio-world-75-000-worldwide-fm-radio-stations.p.rapidapi.com"
        }
        response: requests.Response = \
            requests.request(
                "GET", 
                url, 
                headers=headers, 
                params=querystring
            )
        data: dtype = response.json()
        asyncio.run(
            main(
                data.get('stations')
            )
        )


    def handle(self, *args: tuple, **options: dict) -> None:
        """Handles data filling."""

        start = time.perf_counter()
        self.generate_data()
        print(
            f"Finished by {(start - time.perf_counter()):.2f}sec"
        )