print("N haneli bir sayının basamaklarının n'inci üstlerinin toplamı, sayının kendisine eşitse, böyle sayılara Armstrong sayı denir.")
n=input("Armstrong Sayısı Olup Olmadığını Kontol Etmek İstediğiniz Sayıyı Girin:\n")
u=len(n)
top=0

for i in range(0,u):
    top += int(n[i])**u
if top == int(n):
    print("\n{} bir Armstrong sayısıdır.\n".format(n))
else:
    print("\n{} bir Armstrong sayısı değidir.\n".format(n))
