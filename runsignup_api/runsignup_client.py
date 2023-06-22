# Runsignup API runnable example client using Gracy - https://github.com/guilatrova/gracy
import asyncio
import typing as t
from os import environ

import httpx
from gracy import BaseEndpoint, Gracy, GracyConfig, LogEvent, LogLevel
from rich import print

# https://runsignup.com/API/club/:club_id/members/GET
# leaving current_members_only to the default of True


# 1. Define your endpoints
class RunSignupApiEndpoint(BaseEndpoint):
    GET_MEMBERS = "/members"


# 2. Define your Graceful API
class RunsignupAPI(Gracy[str]):
    class Config:
        # TrailHawks club ID = 2198
        BASE_URL = "https://runsignup.com/rest/club/2198"
        SETTINGS = GracyConfig(
            log_request=LogEvent(LogLevel.DEBUG),
            log_response=LogEvent(LogLevel.INFO, "{URL} took {ELAPSED}"),
            parser={"default": lambda r: r.json()},
        )

    def _create_client(self) -> httpx.AsyncClient:
        client = super()._create_client()
        client.headers = {"X-RSU-API-SECRET": environ.get("RSU_SECRET")}
        return client

    async def get_members(self) -> t.Awaitable[dict]:
        return await self.get(
            RunSignupApiEndpoint.GET_MEMBERS,
            params=[("rsu_api_key", environ.get("RSU_KEY")), ("format", "json"), ("results_per_page", "2500")],
        )


rsu = RunsignupAPI()


async def main():
    try:
        members = await rsu.get_members()
        print(f"Printing the 0 index member of {len(members['club_members'])} total currently active members.")
        print(members["club_members"][0])

    finally:
        rsu.report_status("rich")


asyncio.run(main())
