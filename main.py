from src.app import App
from src.config import config

if __name__ == '__main__':
    app = App((config.WIDTH, config.HEIGHT))
    app.run()
