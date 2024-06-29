import matplotlib.pyplot as plt

# Bar Graph Plotting with fig.add_Axes
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])     # [left,bottom,width,height]
languages = ['English', 'French', 'Spanish', 'German', 'Hindi', 'Chinese']      # X-axis
num_of_people = [100, 30, 60, 20, 140, 80]              # Y-axis

ax.bar(languages, num_of_people)        # Plotting
plt.xlabel('Languages')                 # X label
plt.ylabel('Number of People')          # Y label
plt.title('Number of People by Language')       # Title

plt.show()          # shows the graph

# Bar Graph Plotting with plt.subplots()
fig, ax = plt.subplots()

languages = ['English', 'French', 'Spanish', 'German', 'Hindi', 'Chinese']      # X-axis
num_of_people = [100, 30, 60, 20, 140, 80]              # Y-axis

ax.bar(languages, num_of_people)        # Plotting
plt.xlabel('Languages')                 # X label
plt.ylabel('Number of People')          # Y label
plt.title('Number of People by Language')       # Title

plt.show()          # shows the graph