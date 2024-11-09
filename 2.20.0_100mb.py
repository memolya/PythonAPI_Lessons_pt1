new_dict = {'file1.txt': 10, 'file2.txt': 100, 'file3.txt': 101, 'file4.txt': 200, 'file5.txt': 5, 'file6.txt': 305}
for key, value in new_dict.items(): # This method analyzes a dictionary and returns keys and values stored as tuples.
    if value > 100:
        print(key)