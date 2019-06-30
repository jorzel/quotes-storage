import os

from src.app import create_app


config_prefix = os.environ.get('CONFIG_ENV', 'test').capitalize()
app = create_app(f'src.config.{config_prefix}Config')


if __name__ == '__main__':
    app.run()
