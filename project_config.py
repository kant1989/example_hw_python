from typing import Literal

from pydantic_settings import BaseSettings
from hw_python.utils import path

BrowserType = Literal['chrome', 'firefox', 'edge']


class Config(BaseSettings):
    env: Literal['example', 'stage', 'local'] = 'local'

    base_url: str = "https://demoqa.com"
    window_height: int = 1080
    window_width: int = 1920
    driver_name: BrowserType = 'chrome'
    timeout: float = 4.0
    headless: bool = False


config = Config(_env_file=path.relative_from_root(f'.env.{Config().env}'))
