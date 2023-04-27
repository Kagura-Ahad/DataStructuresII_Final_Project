from finger_trees import *
import csv
from typing import List, Tuple, Dict

def insert_from_CSV() -> Dict[Tuple[str, str], FingerTree]:
    # Create an empty dictionary to store the finger trees
    finger_trees = {}

    # Open the CSV file and read the data
    with open('Temperature_data_set.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        greenhouse_values = []
        time_values = []
        date_values = []
        value_lst = []
        # Skip the header row
        next(reader)
        count = 0
        lst1 = []
        lst2 = []
        # Loop through each row in the CSV file
        for row in reader:
            if str(row[0]) == '':
                # print('The data got inconsistent, hence the loop stopped')
                break
            else:
                # Extract the date and temperature values from the row
                date = row[0].split()[0]
                time = row[0].split()[1]
                temperature = row[1] 
                # Loop through each greenhouse column and create a finger tree for each day and greenhouse
                for i in range(1, len(row)):
                    greenhouse = "greenhouse" + str(i)
                    value = time + "_" + date + "_" + temperature
                    if greenhouse not in greenhouse_values:
                        greenhouse_values.append(greenhouse)
                    if time not in time_values:
                        time_values.append(time)
                    if date not in date_values:
                        date_values.append(date)
                    # Create a new finger tree for each day and greenhouse
                    if (date, greenhouse) not in finger_trees:
                        finger_trees[(date, greenhouse)] = FingerTree.empty()
                    # Insert the temperature reading into the finger tree
                    if count <= 12:
                        print("prepend", value)
                        finger_trees[(date, greenhouse)].prepend(value)
                    else:
                        print("append", value)
                        finger_trees[(date, greenhouse)].append(value)
                count += 1
                if count == 24:
                    count = 0
    returnlist = []
    returnlist.append(finger_trees)
    returnlist.append(greenhouse_values)
    returnlist.append(time_values)
    returnlist.append(date_values)
    return returnlist

finger_trees = insert_from_CSV()


# print(finger_trees[('2/10/2012', 'greenhouse1')].treeLast())
# print(finger_trees[('2/10/2012', 'greenhouse1')].treeHead())
print(finger_trees[('2/10/2012', 'greenhouse1')])