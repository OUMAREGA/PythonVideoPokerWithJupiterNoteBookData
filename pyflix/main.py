import pyflix.file_helper as file

print('Traitement de fichiers pour PyFlix')

for data in file.load_shows(r'/Users/dad3zero/Workshop/python/python4students-work/assets/showslist.csv'):
    print("->", data, "<-")
