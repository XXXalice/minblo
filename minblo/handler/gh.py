import yaml
import inspect
import requests
import sys
import os

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
        config_path = os.path.join('/'.join(inspect.stack()[0][1].split('/')[:-1]), CONFIG_FILE_NAME) # handler/:CONFIG_FILE_NAME
        with open(config_path, 'r+') as f:
            self.config = yaml.load(f) # return type dict
        self.api_uri =  "https://api.github.com/repos/{}/{}/"

    def get_issues(self):
        self.api_uri = self.api_uri.format(
            self.config["github"]["id"],
            self.config["github"]["repo"]
        ) + "issues"
        try:
            raw_issues_data = requests.get(self.api_uri)
        except Exception as e:
            print(e)
            return

        return raw_issues_data




if __name__ == '__main__':
    # test mode.
    sys.stdout.write('this script is using github REST apis.')
    api = GithubApis()
    print(api.config)