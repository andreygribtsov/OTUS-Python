from loguru import logger
from time import sleep
import asyncio

async def foo():
    logger.info('Start foo acync')
    await asyncio.sleep(2)    
    logger.info('Finish foo acync')

async def bar():
    logger.info('Start bar acync')
    await asyncio.sleep(5)    
    logger.info('Frinish bar acync')

if __name__ == '__main__':
    logger.info('Starting main')
    func_list = [
            foo(),
            bar(),
            ]
    corut = asyncio.wait(func_list)
    asyncio.run(corut)
    logger.info('End main')
