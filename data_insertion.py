from finger_trees import *
import csv

# Create an empty dictionary to store the finger trees
finger_trees = {}

# Open the CSV file and read the data
with open('Temperature_data_set.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    # Skip the header row
    next(reader)
    # Loop through each row in the CSV file
    for row in reader:
        if str(row[0]) == '':
            print('The data got inconsistent, hence the loop stopped')
            break
        else:
            # Extract the date and temperature values from the row
            date = row[0].split()[0]
            time = row[0].split()[1]
            temperature = row[1]
            # Loop through each greenhouse column and create a finger tree for each day and greenhouse
            for i in range(1, len(row)):
                greenhouse = "greenhouse" + str(i)
                value = time + "_" + date + "_" + row[i]
                # Create a new finger tree for each day and greenhouse
                if (date, greenhouse) not in finger_trees:
                    finger_trees[(date, greenhouse)] = FingerTree.empty()
                # Insert the temperature reading into the finger tree
                finger_trees[(date, greenhouse)].append(value)
# finger_trees[('2/10/2012', 'greenhouse1')].treeHead()
# finger_trees[('2/10/2012', 'greenhouse1')].treeTail()
finger_trees[('2/10/2012', 'greenhouse1')].treeLast()
finger_trees[('2/10/2012', 'greenhouse1')].treeInit()