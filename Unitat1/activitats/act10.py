llista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

llista_imp = list(filter(lambda i: i%2 != 0, llista))
llista_par = list(filter(lambda i: i%2 == 0, llista))

print(llista_par)
print(llista_imp)