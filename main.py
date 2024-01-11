import asyncio
import pyautogui

async def hitting():
    while True:
        for i in range(0,5):
            await asyncio.sleep(1)
            pyautogui.keyDown("space")
            pyautogui.click()
            pyautogui.keyUp("space")
        await asyncio.sleep(15)

async def eating():
    while True: 
        await asyncio.sleep(180)
        pyautogui.press("2")
        pyautogui.mouseDown(button='right')
        await asyncio.sleep(15)
        pyautogui.mouseUp(button='right')
        pyautogui.press("1")

# Run both tasks concurrently
async def main():
    task1 = asyncio.create_task(hitting())
    task2 = asyncio.create_task(eating())

    await task1
    await task2

asyncio.run(main())