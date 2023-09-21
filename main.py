import csv

from travel import Travel

travel = Travel()


# Fetch csv file and get results
def fetch_csv_file(file):
    try:
        with open(file, "r", encoding="utf-8-sig") as read_file:
            lines = read_file.read().splitlines()
    except FileNotFoundError:
        raise FileNotFoundError("File doesn't exist")
    else:
        return show_results(lines)


# Read csv
def read_csv_file(file):
    travel_dict = travel.__dict__
    reader = csv.DictReader(file)  # get dict instead of a list
    records = []

    for row in reader:
        for column in row:
            travel_dict[column] = row[column]
        records.append(travel_dict)
    return records


# Get results
def show_results(file):
    for i, record in enumerate(read_csv_file(file)[:20]):
        print(f"position: {i+1}")
        print(Travel(**record).print())


fetch_csv_file("travelq.csv")
