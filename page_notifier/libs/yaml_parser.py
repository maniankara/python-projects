import yaml

class YamlParser:

    urls: list

    def parse(self, path: str):
        with open(path) as file:
            websites = yaml.safe_load(file)
            self.urls = [url['url'] for url in websites['websites']]
        print("*******", self.urls)