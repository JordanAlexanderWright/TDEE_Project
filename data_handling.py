import pickle


def save_food(date, new_data):

    with(open("food_log.pickle", 'ab+')) as openfile:

        openfile.seek(0, 0)

        try:
            data = pickle.load(openfile)

            if data[date]:
                data[date] = new_data[date]

            else:
                data.update(new_data)

            openfile.seek(0, 0)
            pickle.dump(data, openfile, pickle.HIGHEST_PROTOCOL)

        except EOFError:
            pickle.dump(new_data, openfile, pickle.HIGHEST_PROTOCOL)


def load_info(date):

    with(open("food_log.pickle", 'rb')) as openfile:

        data = pickle.load(openfile)

        return data[date]

