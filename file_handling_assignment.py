# File creation
def create_file():
    with open("my_file.txt", "w") as file:
        file.write("Bonjour, c'est mon premier fichier !\n")
        file.write("Je suis créé le {}.\n".format("aujourd'hui"))
        file.write("J'ai {} ans.\n".format(25))

# Reading and print of the file
def read_file():
    with open("my_file.txt", "r") as file:
        contenu = file.read()
        print("Contenu du fichier :")
        print(contenu)

# Content add to the file
def append_file():
    with open("my_file.txt", "a") as file:
        file.write("Je vais ajouter quelques lignes supplémentaires.\n")
        file.write("C'est facile de modifier un fichier existant.\n")
        file.write("J'espère que cela fonctionne !\n")

# Functions execution
create_file()
read_file()
append_file()
read_file()
