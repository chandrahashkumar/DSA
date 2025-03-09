heros = ['spider man','thor','hulk','iron man','captain america']
print ("Length of the list:", len(heros))
heros.append("black panther")
print("Adding black panther to the list:", heros)
heros.remove("black panther")
print("Removing black panther from the list:", heros)
heros.insert(3,"black panther")
print(heros)
heros[1:3] = ["doctor strange"]
print(heros)
heros.sort()
print("Sorting the list in ascending order:", heros)