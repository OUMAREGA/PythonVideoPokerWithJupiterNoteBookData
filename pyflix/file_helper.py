def load_shows(file_path):
    with open(file_path) as shows_file:

        shows_file.readline()

        for line in shows_file:
            show, season, number, title, duration, year = line.split(";")

            yield show, int(season), int(number), title, int(duration), int(year)
