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

    def get_issues(self, direct_return_response=False):
        """
        GitHub APIより指定した指定したリポジトリのissuesを取得
        :return: list（リポジトリ内部の全issues）
        """
        self.api_uri = self.api_uri.format(
            self.config["github"]["id"],
            self.config["github"]["repo"]
        ) + "issues"
        try:
            resp = requests.get(self.api_uri)
            if direct_return_response:
                return resp
        except Exception as e:
            print(e)
            return

        issues = resp.json()

        return issues

    def fetch_issues(self, raw_issues, origin_rules=None):
        """
        全issues内部から必要な物を抽出する
        :param raw_datas: tuple 全issues
        :param origin_rules: str 独自正規表現（基本使わない？）
        :return: list 抽出済みissues
        """
        import re
        correct_items = []
        pattern = r"\d{4}/\d{2}/\d{2}" if origin_rules == None else origin_rules
        for data in raw_issues:
            print(data)
            judge = re.search(pattern, data["title"])
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
    issues = api.get_issues()
    items = api.fetch_issues(issues)
    pprint.pprint(items)
