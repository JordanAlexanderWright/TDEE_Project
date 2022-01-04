import pickle


def save_food(date, new_data):

    with(open("food_log.pickle", 'ab+')) as openfile:

        openfile.seek(0, 0)
        print(new_data)
        new_date = date
        save_stuff = {new_date: new_data}

        try:
            data = pickle.load(openfile)

            if data[date]:
                print('yes')
                data[date] = new_data
                print(data[date])

            else:
                print(save_stuff)
                print('hello')
                data.update(save_stuff)

            openfile.seek(0, 0)
            pickle.dump(data, openfile, pickle.HIGHEST_PROTOCOL)

        except EOFError:
            print("uh oh")
            pickle.dump(save_stuff, openfile, pickle.HIGHEST_PROTOCOL)


def load_info(date):

    with(open("food_log.pickle", 'rb')) as openfile:

        data = pickle.load(openfile)

        if data[date]:

            return data[date]
        else:
            return None
