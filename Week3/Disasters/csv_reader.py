import csv


class CsvReader:
    @staticmethod
    def read_csv_file(path):
        disasters = []
        try:
            with open(path, encoding="utf-8", newline='') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=",")
                for row in reader:
                    disasters.append(row)
            return disasters
        except FileNotFoundError:
            print("File not found.")
        except UnicodeDecodeError:
            print("File encoding error.")
