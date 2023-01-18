def get_countries_xith_c():
    result = []
    with open('../csv/countries of the world.csv') as f:
        lines = f.readlines()

    for line in lines[1:]:
        name = line.split(",")[0].strip()
        if name[1] == "C":
            result.append(name)
    return result


print(get_countries_xith_c())
