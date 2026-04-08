import asyncio
from telemetry import FlightGearTelemetry


def map_motion(data):
    pitch_cmd = data["pitch"] * 2
    roll_cmd = data["roll"] * 3
    yaw_cmd = data["yaw"] * 0.1

    return {
        "pitch_cmd": round(pitch_cmd, 2),
        "roll_cmd": round(roll_cmd, 2),
        "yaw_cmd": round(yaw_cmd, 2),
    }


async def main():
    fg = FlightGearTelemetry()
    await fg.connect()

    while True:
        data = await fg.read()
        motion = map_motion(data)

        print("INPUT:", data)
        print("OUTPUT:", motion)
        print("------")

        await asyncio.sleep(0.1)


asyncio.run(main())