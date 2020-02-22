import yaml
import inspect
import sys

CONFIG_FILE_NAME = 'config.yml'

class GithubApis:
    """
    Github REST API利用クラス
    """
    def __init__(self):
        """
        イニシャライザ
        configをロード
        """
        config_path = '/'.join(inspect.stack()[0][1].split('/')[:-1], CONFIG_FILE_NAME) # handler/:CONFIG_FILE_NAME
        self.config = yaml.load(config_path) # return type: dict



if __name__ == '__main__':
    # test mode.
    sys.stdout.write('this script is using github REST apis.')
