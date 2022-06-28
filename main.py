from utils import loadfile, relations, coincidence

if __name__ == '__main__':
    data = loadfile("files/schedule.txt")
    lista = relations(data)
    L = coincidence(lista, [], 0)
    print(*L, sep="\n")
