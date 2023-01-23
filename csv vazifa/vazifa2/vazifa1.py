import csv


def get_relase_year_2020_2021():
    res = ""
    try:
        with open("../csv/netflix_titles.csv", "r", encoding="utf-8") as f:
            data = [row for row in csv.reader(f)]
        for line in data[1:]:
            relase_year = line[7].strip()
            if relase_year == "2020" or relase_year == "2021":
                res += f"{line}\n"
        return res
    except Exception as e:
        print(e)


def write_relase_year_2020_2021():
    with open("relase_year_2020_2021.csv", "w", encoding="utf-8") as f:
        for relase_year in get_relase_year_2020_2021():
            f.write(f"{relase_year}")


def get_listed_in_comedies():
    res = ""
    try:
        with open("../csv/netflix_titles.csv", "r", encoding="utf-8") as f:
            data = [row for row in csv.reader(f)]
        for line in data[1:]:
            relase_year = line[10].strip()
            if relase_year == "Comedies":
                res += f"{line}\n"

    except Exception as e:
        print(e)
    return res


def write_listed_in_comedies():
    with open("rlisted_in_comedies.csv", "w", encoding="utf-8") as f:
        for relase_year in get_listed_in_comedies():
            f.write(f"{relase_year}")


def movie_United_States():
    res = ""
    with open("../csv/netflix_titles.csv", encoding="utf-8") as f:
        data = [row for row in csv.reader(f)]
    for line in data[1:]:
        type_ = line[1].strip()
        country = line[5].strip()
        if type_ == "Movie" and country == "United States":
            res += f"{line}\n"
    return res


def write_movie_UnitedS():
    with open("movie United Stetes.csv", "w", encoding="utf-8") as f:
        for line in movie_United_States():
            f.write(str(line))


            
# write_relase_year_2020_2021()
# # print(get_relase_year_2020_2021())
#
# print(write_listed_in_comedies())

#print(movie_United_States())
write_movie_UnitedS()