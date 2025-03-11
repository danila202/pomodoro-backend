import asyncio
import uvicorn
import uvloop

from src.pomodoro.settings import settings

def main() -> None:
    """Entrypoint of the application."""
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    uvicorn.run(
        "src.pomodoro.main:make_app",
        host=settings.host,
        port=settings.port,
        factory=True,
    )


if __name__ == "__main__":
    main()
