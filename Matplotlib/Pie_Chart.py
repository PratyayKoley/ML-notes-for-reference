import matplotlib.pyplot as plt

# Pie Chart Plotting
fig, ax = plt.subplots()

languages = ['English', 'French', 'Spanish', 'German', 'Hindi', 'Chinese']      # X-axis
num_of_people = [100, 30, 60, 20, 140, 80]              # Y-axis

# first argument takes the number by which pie slices must occur, second argument are the labels to the pie slices and third argument is the precision by which the pie slices must cut and can be seen to the viewer % % indicates to use character % sign with number 1.1f. It is used to format a string literal.

ax.pie(num_of_people, labels=languages, autopct="%1.1f%%")    
plt.show()