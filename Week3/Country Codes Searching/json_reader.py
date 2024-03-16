from json import JSONDecodeError, load


class JsonReader:
    @staticmethod
    def read_json_file(path):
        try:
            with open(path, "r", encoding="utf-8") as json_file:
                data = load(json_file)
            return data
        except FileNotFoundError:
            print("File not found.")
        except JSONDecodeError:
            print("JSON format is not correct.")
