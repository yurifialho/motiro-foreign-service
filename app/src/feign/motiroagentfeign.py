from typing import Dict
from src.config.config import Config
from src.util.logging import Logger

logger = Logger.getLogger(cls=__name__)

class MotiroAgentFeign:

    def __init__(self) -> None:

        motiroUrl = Config.getEnvVariables(Config.MOTIRO_AGENT_URL)
        

    