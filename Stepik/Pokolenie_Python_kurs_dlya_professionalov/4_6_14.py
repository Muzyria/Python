import pickle


def filter_dump(filename, objects, typename):
    with open(filename, 'wb') as file:
        pickle.dump([i for i in objects if type(i) == typename], file)
