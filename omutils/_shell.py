import asyncio


async def async_run(cmd, semaphore):
    with await semaphore:
        proc = await asyncio.create_subprocess_shell(
            cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await proc.communicate()
    return stdout, stderr
