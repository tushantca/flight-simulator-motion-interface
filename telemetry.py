import urllib.request
import json


class FlightGearTelemetry:
    def __init__(self, base_url="http://127.0.0.1:8080/json"):
        self.base_url = base_url

    async def connect(self):
        return

    async def get_prop(self, path):
        url = f"{self.base_url}{path}"
        with urllib.request.urlopen(url, timeout=2) as response:
            data = json.loads(response.read().decode())
        return float(data["value"])

    async def read(self):
        return {
            "pitch": await self.get_prop("/orientation/pitch-deg"),
            "roll": await self.get_prop("/orientation/roll-deg"),
            "yaw": await self.get_prop("/orientation/heading-deg"),
            "altitude": await self.get_prop("/position/altitude-ft"),
        }