#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('file_input.txt', 'w', encoding='utf_8') as file:
    file.write('fffffffhhhhAAAAhhjkkkff')

with open('file_input.txt', 'r', encoding='utf_8') as file:
    data = file.read()
print(data)
compress=''
decompress=''
count = 1
i=0
k=0
while i<=len(data):
    for j in range(i+1, len(data)):
        if data[i]==data[j] and data[i+1]!=None:
            count+=1
        else:
            compress = compress + str(count)+data[i]
            k=count-1
            count=1
            break
    i+=1+k
    if i >= len(data)-1:
        compress = compress + str(count) + data[i-k]

m=0
while m <=len(compress)-1:
    decompress = decompress + str(int(compress[m])*compress[m+1])
    m+=2

with open('file_output.txt', 'w', encoding='utf_8') as file:
    file.write(f'data: {data}\ncompress: {compress}\ndecompress: {decompress}')