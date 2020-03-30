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
        """
        GitHub APIより指定した指定したリポジトリのissuesを取得
        :return: list（リポジトリ内部の全issues）
        """
        self.api_uri = self.api_uri.format(
            self.config["github"]["id"],
            self.config["github"]["repo"]
        ) + "issues"
        try:
            raw_issues_datas = requests.get(self.api_uri).text
        except Exception as e:
            print(e)
            return

        return raw_issues_datas

    def fetch_issues(self, raw_datas, origin_rules=None):
        """
        全issues内部から必要な物を抽出する
        :param raw_datas: tuple 全issues
        :param origin_rules: str 独自正規表現（基本使わない？）
        :return: list 抽出済みissues
        """
        import re
        correct_items = []
        pattern = r"$\d{4}/d{2}/d{2}" if origin_rules == None else origin_rules
        for data in raw_datas:
            judge = re.match(pattern , data["title"])
            if judge:
                item = { "title": data["title"],
                         "date": data["created_at"],
                         "body": data["body"]}
                correct_items.append(item)

        return correct_items


if __name__ == '__main__':
    # test mode.
    import pprint
    sys.stdout.write('this script is using github REST apis.')
    api = GithubApis()
    print(api.config)
    raw_data = api.get_issues()
    data = api.fetch_issues(raw_datas=raw_data)
    pprint.pprint(data)