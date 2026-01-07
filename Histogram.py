import math
import matplotlib.pyplot as plt

def calculate_freq(num1, num2) -> tuple:
    frequency = 0
    for element in dataset:
        if(element < num2 and element >= num1):
            frequency += 1
    return frequency, round(frequency/sample_size, precision)

def print_basic_data():
    print(f'Minimum is\t\t\t\t{mn}', end='\n')
    print(f'Maximum is\t\t\t\t{mx}', end='\n')
    print(f'Range is\t\t\t\t{rng}', end='\n')
    print(f'Subintervals number is\t{subintervals_number}', end='\n')
    print(f'Sample Size is\t\t\t{sample_size}', end='\n')
    print(f'Precision Size is\t\t{precision}', end='\n')
    print(f'Dataset is\t\t\t\t{dataset}', end='\n')
    print(f'Cell Width is\t\t\t{cell_width}', end='\n')
    print(f'Intervals is\t\t\t{intervals}', end='\n')
    print(f'Frequencies is\t\t\t{frequencies}', end='\n')


file = open("dataset_1.csv", "rt")
str_list = file.read().split(',')
dataset = []
for i in range(0,len(str_list)):
    dataset.append(float(str_list[i]))

sample_size = len(dataset)
mn = min(dataset)
mx = max(dataset)
rng = mx - mn
dataset.sort()
subintervals_number = math.ceil(math.sqrt(sample_size))

# Detecting Precision
# Edited After Video (Realized that I made the inverse)
precision = 0
for element in dataset:
    if element != int(element):
        precision = len(str(dataset[0]).split('.')[1])
        break

cell_width = round(rng/subintervals_number,precision)
print(str(dataset[0]).split('.'))

intervals = []
for i in range(0, subintervals_number):
    intervals.append((round(mn + i*cell_width, precision), round(mn + (i+1)*cell_width, precision)))

frequencies = []
for i in range(0, subintervals_number):
    frequencies.append(calculate_freq(intervals[i][0], intervals[i][1]))

print_basic_data()


# Matplotlib code

# table code
fig, (tablo, histo) = plt.subplots(1, 2, sharey=True, tight_layout=True)
columns = ['Intervals','Frequency', 'Relative Frequency']
rows = []
for i in range(0,subintervals_number):
    row = []
    row.append(f'{intervals[i][0]} - {intervals[i][1]}')
    row.append(f'{frequencies[i][0]}')
    row.append(f'{frequencies[i][1]}')
    rows.append(row)

tablo.axis('off')
table = tablo.table(cellText = rows, colLabels = columns, colLoc='center', loc='center', cellLoc='center', rowLoc='left')
table.scale(1.5, 2.5)
table.auto_set_font_size(False)
table.set_fontsize(15)

# Histogram code

histo.hist(dataset, bins = subintervals_number, color='skyblue', edgecolor='black')
plt.xlabel("Interval")
plt.ylabel("Frequency")
histo.grid(axis='x', linestyle=':', alpha=0.7)

plt.title("R.F. Table and Histogram")
plt.show()

# Forgot to close it at the video
file.close()