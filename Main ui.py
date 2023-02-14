import subprocess
from tkinter import Tk, Label, Button
import nltk
import sklearn
class MyFirstGUI:
    def __init__(self,master):
        self.master = master
        master.title("A simple GUI")


        self.label = Label(master, text="Resumex!")
        self.label.pack()

        self.greet_button = Button(master, text="Candidate", command=self.greet)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Recruiter", command=self.greet1)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        subprocess.Popen("candidateui1.py 1", shell=True)

    def greet1(self):
        subprocess.Popen("jobpostui1.py 1", shell=True)

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()


##job_reqs = ["java", "python"]
with open('jobpost.pkl', 'rb') as f:
   job_reqs = pickle.load(f)

#job_reqs_c = len(job_reqs)+1
count = 0
new_filtered_list = list(set(filtered_sentence))

for i in range(len(new_filtered_list)):
    if new_filtered_list[i] in job_reqs:
        #print new_filtered_list[i]
        count += 1

suit_per = count / len(job_reqs)
print ((count, job_reqs))

print ("Candidate is suitable: "+str(suit_per*100)+"%")

# x-coordinates of left sides of bars
##left = [1, 2, 3, 4, 5]
left = range(1,len(job_reqs)+1)

# heights of bars
##height = [10, 24, 36, 40, 5]
height = []
for i in range(len(job_reqs)):
    if i >= count:
        height.append(0)
    else:
        height.append(1)
print (height)

# labels for bars
##tick_label = ['one', 'two', 'three', 'four', 'five']
tick_label = job_reqs


# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 0.8, color = ['red', 'green'])

# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('Similarity chart')

# function to show the plot
plt.show()
