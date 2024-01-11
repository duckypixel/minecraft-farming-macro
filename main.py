import asyncio
import pyautogui

# The async function for hitting the mobs
async def hitting():
    while True:
        for i in range(0,5):
            await asyncio.sleep(1) # * timed for a diamond sword, change if you plan on using other items i.e axes, you can use the equation 1/attack-speed to get the delay in seconds (which is the unit here)
            pyautogui.keyDown("space")
            pyautogui.click()
            pyautogui.keyUp("space")
        await asyncio.sleep(15) # * delays for how long to wait before hitting mobs, change if you want to wait for more mobs to pool up or less (unit is in seconds)

# Async function for eating food
async def eating():
    while True: 
        await asyncio.sleep(180) # * delays for how long you want to wait before eating food, change this if needed (unit is in seconds)
        pyautogui.press("2") # * binding for your food, you can change this to whatever bind you use for your food (refer to https://pyautogui.readthedocs.io/en/latest/keyboard.html for which binds are accepted)
        pyautogui.mouseDown(button='right')
        await asyncio.sleep(15) # * delays for how long the right button is held, change if needed (unit is also in seconds)
        pyautogui.mouseUp(button='right')
        pyautogui.press("1") # * binding for your sword, you can change this to whatever bind you use for your food 

async def main():
    hit = asyncio.create_task(hitting())
    eat = asyncio.create_task(eating()) 

    await hit
    await eat

asyncio.run(main()) 