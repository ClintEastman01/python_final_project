import tkinter


class UniversityGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()
        self.main_window.geometry("425x150")
        self.main_window.title('University Information System')

        # Create frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create variable to use with the Radio buttons
        self.rb_var = tkinter.IntVar()

        # Set the variable to 0
        self.rb_var.set(0)

        # Create the Radio buttons in top_frame
        self.rb1 = tkinter.Radiobutton(self.top_frame,
                                       text='Check Instructor Info',
                                       variable=self.rb_var, value=1,
                                       command=self.radio_button_selected)
        self.rb2 = tkinter.Radiobutton(self.top_frame,
                                       text='Get Department Info',
                                       variable=self.rb_var, value=2,
                                       command=self.radio_button_selected)
        self.rb3 = tkinter.Radiobutton(self.top_frame,
                                       text='Clear',
                                       variable=self.rb_var, value=3,
                                       command=self.clear)
        self.rb4 = tkinter.Radiobutton(self.top_frame,
                                       text='Quit',
                                       variable=self.rb_var, value=4,
                                       command=self.main_window.destroy)

        # Pack the Radio buttons and align them to the left by default
        self.rb1.pack(side='left')
        self.rb2.pack(side='left')
        self.rb3.pack(side='left')
        self.rb4.pack(side='left')

        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    # Define the clear function
    def clear(self):
        self.mid_frame.destroy()
        self.bottom_frame.destroy()

    def create_instructor_frame(self):

        self.value = tkinter.StringVar()
        self.submit_button = tkinter.Button(self.mid_frame,
                                            text='Submit', command=self.search_instructor)
        self.instructor_label = tkinter.Label(self.mid_frame,
                                              text='Enter instructor ID:')
        self.instructor_entry = tkinter.Entry(self.mid_frame, width=10)

        self.instructor_info = tkinter.Label(self.bottom_frame,
                                             textvariable=self.value, justify="left", anchor='w')

        self.instructor_label.pack(side='left')
        self.instructor_entry.pack(side='left')
        self.submit_button.pack(side='left')
        self.instructor_info.pack(side='left')

        self.mid_frame.pack(anchor='w')
        self.bottom_frame.pack(anchor='w')

        self.instructor_entry.bind('<Return>', self.search_instructor)

    def create_dept_frame(self):
        self.value = tkinter.StringVar()
        self.submit_button = tkinter.Button(self.mid_frame,
                                            text='Submit', command=self.search_dept)
        self.dept_label = tkinter.Label(self.mid_frame,
                                        text='Enter department name:')
        self.dept_entry = tkinter.Entry(self.mid_frame, width=10)

        self.dept_info = tkinter.Label(self.bottom_frame,
                                       textvariable=self.value, anchor='w')

        self.dept_label.pack(side='left')
        self.dept_entry.pack(side='left')
        self.submit_button.pack(side='left')
        self.dept_info.pack(side='left')

        self.mid_frame.pack(anchor='w')
        self.bottom_frame.pack(anchor='w')

        self.dept_entry.bind('<Return>', self.search_dept)

    def radio_button_selected(self):
        # Get the value of the selected radio button.
        if self.rb_var.get() == 1:
            self.mid_frame.destroy()
            self.bottom_frame.destroy()
            self.mid_frame = tkinter.Frame(self.main_window)
            self.bottom_frame = tkinter.Frame(self.main_window)
            self.create_instructor_frame()
        if self.rb_var.get() == 2:
            self.mid_frame.destroy()
            self.bottom_frame.destroy()
            self.mid_frame = tkinter.Frame(self.main_window)
            self.bottom_frame = tkinter.Frame(self.main_window)
            self.create_dept_frame()
        if self.rb_var.get() == 3:
            self.clear()


    def search_instructor(self, event=None):
        #
        id = int(self.instructor_entry.get())
        found = False
        with open('instructor.txt', 'r') as int_file, open('department.txt', 'r') as dept_file:
            int_line = int_file.readline()
            dept_line = dept_file.readline()
            while int_line != '':
                int_line = int_line.rstrip().split(",")
                key = int(int_line[0])
                if id == key:
                    name = int_line[1]
                    dept = int_line[2]
                    found = True
                int_line = int_file.readline()

            if not found:
                self.value.set('Information not found')
                return

            while dept_line != '':
                dept_line = dept_line.rstrip().split(",")
                key = dept_line[0]
                if dept == key:
                    building = dept_line[1]
                dept_line = dept_file.readline()
        self.value.set(f'Name: {name}\nDepartment: {dept}\nBuilding: {building}')

    def search_dept(self, event=None):

        dept = self.dept_entry.get()
        dept = dept.upper()
        found = False
        with open('department.txt', 'r') as dept_file:
            dept_line = dept_file.readline()
            while dept_line != '':
                dept_line = dept_line.rstrip().split(",")
                key = dept_line[0]
                if dept == key:
                    building = dept_line[1]
                    budget = dept_line[2]
                    found = True
                dept_line = dept_file.readline()
            if not found:
                self.value.set('Information not found')
                return
            else:
                self.value.set(f'Building: {building}\nBudget: {budget}')


# Create an instance of AutoGUI
if __name__ == '__main__':
    auto = UniversityGUI()
