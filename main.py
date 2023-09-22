import csv

from travel import Travel

travel = Travel()


# Fetch csv file and get results
def fetch_csv_file(file):
    try:
        # open/close file management
        with open(file, "r", encoding="utf-8-sig") as read_file:
            lines = read_file.read().splitlines()
    except FileNotFoundError:
        raise FileNotFoundError("File doesn't exist")
    else:
        return read_csv_file(lines)


# Read csv by travel module
def read_csv_file(file):
    travel_dict = travel.__dict__
    reader = csv.DictReader(file)  # get dict of list of data
    records = []

    for i, row in enumerate(reader):
        for column in row:
            travel_dict[column] = row[column]
        records.append(travel_dict)
        if i > 20:
            break
        print(Travel(**records[i]).print())


fetch_csv_file("travelq.csv")
