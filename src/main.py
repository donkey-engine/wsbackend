"""Application run module."""
import uvicorn

from app import init


def run() -> None:
    """Run application."""
    app = init()
    uvicorn.run(app)


if __name__ == "__main__":
    run()
