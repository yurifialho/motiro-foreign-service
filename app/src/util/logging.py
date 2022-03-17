import os
import yaml
import logging.config
import logging
import coloredlogs

class Logger:

    __loggerSetted = False

    @classmethod
    def setup_logging(self, default_path='src/config/logging.yaml', default_level=logging.INFO, env_key='LOG_CFG'):
        config = Logger.getConfigLogger(default_path=default_path, env_key=env_key)
        if config:
            logging.config.dictConfig(config)
            coloredlogs.install()
        else:
            logging.basicConfig(level=default_level)
            coloredlogs.install(level=default_level)
            print('Failed to load configuration file. Using default configs')

        self.__loggerSetted = True

    @classmethod
    def getLogger(self, cls=__name__, level=logging.INFO):
        if not self.__loggerSetted:
            Logger.setup_logging(default_level=level)
        return logging.getLogger(cls)

    @classmethod
    def getConfigLogger(self, default_path='src/config/logging.yaml', env_key='LOG_CFG'):
        path = default_path
        value = os.getenv(env_key, None)
        if value:
            path = value
        if os.path.exists(path):
            with open(path, 'rt') as f:
                try:
                    config = yaml.safe_load(f.read())
                    return config
                except Exception as e:
                    print(e)
                    print('Error in Logging Configuration. Using default configs')

        return None