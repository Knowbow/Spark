import asyncio
import logging
#missing imports
import os 
import datetime 

logger = logging.getLogger(__name__)
SLEEP_DURATION = os.getenv("SLEEP_DURATION")


class Pipeline:
    #self needs to be added as a first argument to be able to reference the instance.
    # async not used with magic methods
    def __init__(self, *args, **kwargs):  
        self.default_sleep_duration = kwargs["default_sleep_duration"] # self to reference to the instance since we're in a constructor

    #self needs to be added as first argument 
    async def sleep_for(self,coro, sleep_duration, *args, **kwargs):
        #sleep_duration should be capitalized
        #tabs needed to be fixed
        asyncio.sleep(SLEEP_DURATION)
        logger.info("Slept for %s seconds", SLEEP_DURATION)
        start = datetime.now()
        #kwargs mispelled
        await coro(*args, **kwargs)
        #fixed tabbing for last 3 lines
        end = datetime.now()
        time_elapsed = (start - end).total_seconds()
        logger.debug(f"Executed the coroutine for {time_elapsed} seconds")
