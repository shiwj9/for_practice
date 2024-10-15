magicians_name = ["Lily", "Tom", "Sam"]


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


show_magicians(magicians_name)


def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "the Great " + magicians[i]
    # for magician in magicians:
    #     magician = "the Great "+magician#形参magician改变，实际列表未改变


make_great(magicians_name)

show_magicians(magicians_name)
