"""
Tut
"""
import time
from pathlib import Path
from typing import Callable

import httpx

POP20_CC = {"CN", "IN", "US", "ID", "BR", "PK", "NG", "BD", "RU", "JP"}

BASE_URL