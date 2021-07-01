"""Application run module."""
import uvicorn

from app import init


def run() -> None:
    """Run application."""
    app = init()
    uvicorn.run(
        app,
        host='0.0.0.0',
        port=8888,
    )


if __name__ == "__main__":
    run()
