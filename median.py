import csv
with open('SOCR-HeightWeight.csv', newline ='') as f: 
    reader = csv.reader(f)
    file_data = list(reader)

    file_data.pop(0)

    #sorting data to get the heights of people
    new_data = []
    for i in range(len(file_data)):
        n_num = file_data[i][1]
        new_data.append(float(n_num))

    #getting the median
    n = len(new_data)
    new_data.sort()

    #floor division
    if n % 2 == 0:
        median1 = float(new_data[n//2])
        median2 = float(new_data[n//2-1])
        median = (median1 + median2)/2
    else:
        median = new_data[n//2]
        print(n)
    print("median is:" + str(median))