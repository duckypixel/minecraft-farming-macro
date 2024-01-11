import asyncio
import pyautogui

# The async function for hitting the mobs
async def hitting():
    while True:
        for i in range(0,5):
            await asyncio.sleep(1)
            pyautogui.keyDown("space")
            pyautogui.click()
            pyautogui.keyUp("space")
        await asyncio.sleep(15)

# Async function for eating food
async def eating():
    while True: 
        await asyncio.sleep(180)
        pyautogui.press("2") # * binding for your food, you can change this to whatever bind you use for your food (refer to https://pyautogui.readthedocs.io/en/latest/keyboard.html for which binds are accepted)
        pyautogui.mouseDown(button='right')
        await asyncio.sleep(15)
        pyautogui.mouseUp(button='right')
        pyautogui.press("1") # * binding for your sword, you can change this to whatever bind you use for your food 

async def main():
    hitting = asyncio.create_task(hitting())
    eating = asyncio.create_task(eating())

    await hitting
    await eating

asyncio.run(main())