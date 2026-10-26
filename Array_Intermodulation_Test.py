# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 17:36:27 2020

@author: mark.a.thomsen@spawar.navy.mil
"""

import pyvisa

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

import time
import threading
import os

import tkinter as tk
import tkinter.ttk as ttk

from tkinter import messagebox

import tkinter.filedialog as writer 

class MainPage(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        
        tk.Tk.winfo_toplevel(self).title("Array Intermodulation Test")
        
        # Create spectrum analyzer object
        self.plotter = SR785()
                
        # Initialize variables that will hold entry values
        self.array_serial_number = tk.StringVar()
        self.source_level = tk.StringVar()
        self.array_voltage = tk.StringVar()
        self.array_current = tk.StringVar()
        self.sa_model_number = tk.StringVar()
        self.sa_serial_number = tk.StringVar()
        self.cal_due_date = tk.StringVar()
        self.number_channels = tk.StringVar()
        self.current_channel = tk.StringVar()
        self.gpib_number = tk.StringVar()
        
        # Create Left, Right, and Bottom frame for organizing window
        self.left_frame = tk.Frame(self)
        self.right_frame = tk.Frame(self)
        self.bottom_frame = tk.Frame(self)
        
        self.left_frame.grid(row = 0,
                             column = 0,
                             sticky = "nsew",
                             pady = 10)
        
        self.right_frame.grid(row = 0,
                              column = 1,
                              sticky = "nsew",
                              pady = 10)
        
        self.bottom_frame.grid(row = 1,
                               column = 0,
                               columnspan = 2,
                               sticky = "nsew",)
        
        
        
        # Set Labels to Left side of screen
        self.array_sn_label = tk.Label(self.left_frame,
                                       text = "Array Serial #: ",
                                       font = ("Arial", 20))
        
        self.array_sn_label.pack(expand = True,
                                 fill = "both")
        
        self.source_level_label = tk.Label(self.left_frame,
                                           text = "Source Level(mV): ",
                                           font = ("Arial", 20))
        
        self.source_level_label.pack(expand = True,
                                     fill = "both")
        
        
        self.array_voltage_label = tk.Label(self.left_frame,
                                            text = "Array Voltage: ",
                                            font = ("Arial", 20))
        
        self.array_voltage_label.pack(expand = True,
                                      fill = "both")
        
        self.array_current_label = tk.Label(self.left_frame,
                                            text = "Array Current: ",
                                            font = ("Arial", 20))
        
        self.array_current_label.pack(expand = True,
                                      fill = "both")
        
        self.sa_model_number_label = tk.Label(self.left_frame,
                                              text = "SA Model #: ",
                                              font = ("Arial", 20))
        
        self.sa_model_number_label.pack(expand = True,
                                        fill = "both")
        
        self.sa_serial_number_label = tk.Label(self.left_frame,
                                               text = "SA Serial #: ",
                                               font = ("Arial", 20))
        
        self.sa_serial_number_label.pack(expand = True,
                                         fill = "both")
        
        self.cal_due_date_label = tk.Label(self.left_frame,
                                           text = "Cal Due Date: ",
                                           font = ("Arial", 20))
        
        self.cal_due_date_label.pack(expand = True,
                                     fill = "both")
        
        self.number_channels_label = tk.Label(self.left_frame,
                                              text = "# of Channels: ",
                                              font = ("Arial", 20))
        
        self.number_channels_label.pack(expand = True,
                                        fill = "both")
        
        self.current_channel_label = tk.Label(self.left_frame,
                                              text = "Current Channel: ",
                                              font = ("Arial", 20))
        
        self.current_channel_label.pack(expand = True,
                                        fill = "both")
        
        self.gpib_number_label = tk.Label(self.left_frame,
                                          text = "GPIB #: ",
                                          font = ("Arial", 20))
        
        self.gpib_number_label.pack(expand = True,
                                     fill = "both")
    
        
        # Set Values to Right side of the screen
        self.array_serial_number_entry = tk.Entry(self.right_frame,
                                                  textvariable = self.array_serial_number,
                                                  font = ("Arial", 20))
        
        self.array_serial_number_entry.pack(expand = True,
                                            fill = "both",
                                            pady = (5, 0))
        
        self.source_level_entry = tk.Entry(self.right_frame,
                                           textvariable = self.source_level,
                                           font = ("Arial", 20))
        
        self.source_level_entry.pack(expand = True,
                                     fill = "both",
                                     pady = (5, 0))
        
        self.array_voltage_entry = tk.Entry(self.right_frame,
                                            textvariable = self.array_voltage,
                                            font = ("Arial", 20))
        
        self.array_voltage_entry.pack(expand = True,
                                      fill = "both",
                                      pady = (5, 0))
        
        self.array_current_entry = tk.Entry(self.right_frame,
                                            textvariable = self.array_current,
                                            font = ("Arial", 20))
        
        self.array_current_entry.pack(expand = True,
                                      fill = "both",
                                      pady = (5, 0))
        
        self.sa_model_number_entry = tk.Entry(self.right_frame,
                                              textvariable = self.sa_model_number,
                                              font = ("Arial", 20))
        
        self.sa_model_number_entry.pack(expand = True,
                                        fill = "both",
                                        pady = (5, 0))
        
        self.sa_serial_number_entry = tk.Entry(self.right_frame,
                                               textvariable = self.sa_serial_number,
                                               font = ("Arial", 20))
        
        self.sa_serial_number_entry.pack(expand = True,
                                         fill = "both",
                                         pady = (5, 0))
        
        self.cal_due_date_entry = tk.Entry(self.right_frame,
                                           textvariable = self.cal_due_date,
                                           font = ("Arial", 20))
        
        self.cal_due_date_entry.pack(expand = True,
                                     fill = "both",
                                     pady = (5, 0))
        
        self.number_channels_entry = tk.Entry(self.right_frame,
                                              textvariable = self.number_channels,
                                              font = ("Arial", 20))
        
        self.number_channels_entry.pack(expand = True,
                                        fill = "both",
                                        pady = (5, 0))
        
        self.current_channel_entry = tk.Entry(self.right_frame,
                                              textvariable = self.current_channel,
                                              font = ("Arial", 20))
        
        self.current_channel_entry.pack(expand = True,
                                        fill = "both",
                                        pady = (5, 0))
        
        self.gpib_number_entry = tk.Entry(self.right_frame,
                                          textvariable = self.gpib_number,
                                          font = ("Arial", 20))
        
        self.gpib_number_entry.pack(expand = True,
                                    fill = "both",
                                    pady = (5, 0))
        
        
        # Start button underneath the two frames
        self.start_button = tk.Button(self.bottom_frame,
                                      text = "Start",
                                      command = self.start_press,
                                      font = ("Arial", 20))
        
        self.start_button.pack(expand = True,
                               pady = 15)
        
        
        # Continue button, will only be visible after pressing start button
        self.continue1_button = tk.Button(self.bottom_frame,
                                          text = "Continue",
                                          command = self.continue1_press,
                                          font = ("Arial", 20))
        
        # Progress bar to track progress of test. Only visible after
        # pressing start
        self.progress_bar = ttk.Progressbar(self.bottom_frame,
                                            length = 550,
                                            mode = 'determinate')
        
        
    
    
    
    # On start button press
    def start_press(self):
        
        # gpib set to -1 so if the try block below fails, the if statement 
        # won't error out
        gpib = -1
        
        # Convert user input of GPIB to int to use in comm parameters
        try:
            gpib = int(self.gpib_number.get())
                
        except:
            messagebox.showerror("Error",
                                 "Not a valid input.")
            
        # If the GPIB was successfully set, start comms & show next button
        if (gpib >=0):
            
            try:
                # Connect to spectrum analyzer & set the test settings
                self.plotter.gpib_connect(self.gpib_number.get())
                self.plotter.sa_settings(self.source_level.get())
                
                # Query the SR785 to make sure comms are working
                self.plotter.instrument.query("*IDN ?")
                
                # Removes start button from window
                self.start_button.pack_forget()
                
                # Add continue button to window
                self.continue1_button.pack(expand = True,
                                           pady = 15)
                
                # Add Progress bar to window
                self.progress_bar.pack()
                

                
                # Disable all entries during test
                self.array_serial_number_entry.config(state = "disabled")
                self.source_level_entry.config(state = "disabled")
                self.array_voltage_entry.config(state = "disabled")
                self.array_current_entry.config(state = "disabled")
                self.sa_model_number_entry.config(state = "disabled")
                self.sa_serial_number_entry.config(state = "disabled")
                self.cal_due_date_entry.config(state = "disabled")
                self.gpib_number_entry.config(state = "disabled")
                self.number_channels_entry.config(state = "disabled")
                self.current_channel_entry.config(state = "disabled")
                
                # Store test set up information from inputs
                self.plotter.source_level = str(self.source_level.get())
                self.plotter.array_serial_number = str(self.array_serial_number.get())
                self.plotter.array_battery_voltage = str(self.array_voltage.get())
                self.plotter.array_current = str(self.array_current.get())
                self.plotter.sa_model_number = str(self.sa_model_number.get())
                self.plotter.sa_serial_number = str(self.sa_serial_number.get())
                self.plotter.sa_cal_due_date = str(self.cal_due_date.get())
                
                # Get directory to save all files to
                if(self.plotter.directory_selected == 0):
                    self.plotter.directory = writer.askdirectory()
                    self.plotter.directory_selected = 1
        
                messagebox.showinfo("Notification",
                                    "The Signal Analyzer settings have been set.\n" +
                                    "When ready, press continue to begin the test.")
                
            except:
                # When the query times out, give error
                messagebox.showerror("Error",
                                     "No response from the signal analyzer.\n" +
                                     "Please make sure that the GPIB # is correct.")
                
            
    # On continue button press
    def continue1_press(self):

        # Disable button while test is running
        self.continue1_button.config(state = "disabled")
        
        # Reset progress bar back to 0
        self.plotter.progress_value = 0
        
        # Set finished thread state to false
        self.finished = False
        
        # thread the test function so it doesn't lock up the GUI
        thread = threading.Thread(target = self.test)
        thread.daemon = True
        thread.start()
        
        # Checks status of the progress bar and updates the display 
        self.check_status()
            
        # Once test is complete, incremenet channel to test on
        self.current_channel.set(str(int(self.current_channel.get()) + 1))

        # If finished testing all channels, reset for next test
        if(int(self.current_channel.get()) > int(self.number_channels.get())):
            self.current_channel.set("1")
            
            # Enable all entries after test
            self.array_serial_number_entry.config(state = "normal")
            self.array_voltage_entry.config(state = "normal")
            self.array_current_entry.config(state = "normal")
            self.sa_model_number_entry.config(state = "normal")
            self.sa_serial_number_entry.config(state = "normal")
            self.cal_due_date_entry.config(state = "normal")
            self.gpib_number_entry.config(state = "normal")
            self.number_channels_entry.config(state = "normal")
            self.current_channel_entry.config(state = "normal")
            self.continue1_button.config(state = "normal")
                
            self.plotter.file_number = 1
            self.plotter.progress_value = 0
            self.directory_selected = 0
            self.index_number = 0
                


            # Removes start button from window
            self.continue1_button.pack_forget()
            
            # Add continue button to window
            self.start_button.pack(expand = True,
                                   pady = 15)
            
            # Remove progress bar from the screen
            self.progress_bar.pack_forget()
                
                
                
            messagebox.showinfo("Notification",
                                "Array intermodulation test procedure has finished")
        else:
            MsgBox = messagebox.askquestion("Alert",
                                            "Are you ready to move on to channel " + 
                                            self.current_channel.get() + 
                                            "?")
            if (MsgBox == "yes"):
                self.continue1_press()
            else:
                # Enable all entries after test
                self.source_level_entry.config(state = "normal")
                self.array_serial_number_entry.config(state = "normal")
                self.array_voltage_entry.config(state = "normal")
                self.array_current_entry.config(state = "normal")
                self.sa_model_number_entry.config(state = "normal")
                self.sa_serial_number_entry.config(state = "normal")
                self.cal_due_date_entry.config(state = "normal")
                self.gpib_number_entry.config(state = "normal")
                self.number_channels_entry.config(state = "normal")
                self.current_channel_entry.config(state = "normal")
                self.continue1_button.config(state = "normal")
                
                self.plotter.file_number = 1
                self.plotter.progress_value = 0
                self.directory_selected = 0
                self.index_number = 0
                
                # Removes start button from window
                self.continue1_button.pack_forget()
                
                # Add continue button to window
                self.start_button.pack(expand = True,
                                       pady = 15)
                
                # Remove progress bar from the screen
                self.progress_bar.pack_forget()
                
                
                
                messagebox.showinfo("Notification",
                                    "Array intermodulation test procedure has finished")
                
        
    # Updates display with new progress bar value
    def check_status(self):
        while self.finished is False:
            self.progress_bar['value'] = self.plotter.progress_value
            self.update()
            
    # Intermodulation Test Function. Run test & save data to pdf
    def test(self):
        
        # Set first file as file 0
        self.plotter.file_number = 0
        
        # First test 620 Hz, source off
        self.plotter.ch1_freq = 620
        self.plotter.source = "Off"
        self.plotter.get_data()
        self.plotter.plot_data(int(self.current_channel.get()))
        
        # Second test 620Hz, source on
        self.plotter.ch1_freq = 620
        self.plotter.source = "On"
        self.plotter.get_data()
        self.plotter.plot_data(int(self.current_channel.get()))

        # Third test 1140Hz, source on
        self.plotter.ch1_freq = 1140
        self.plotter.source = "On"
        self.plotter.get_data()
        self.plotter.plot_data(int(self.current_channel.get()))
        
        
        self.finished = True
        

# Spectrum analyzer class for SR785 SA
class SR785():
    
    
    def __init__(self):
        self.ch1_freq = 0
        self.ch2_freq = 0
        self.freq_start = 0
        self.source = ""
        self.ch_plot = 0
        self.figure = 0
        self.sa_model_number = 0
        self.source_level = 0
        self.array_serial_number = 0
        self.sa_serial_number = 0
        self.sa_cal_due_date = 0
        self.array_battery_voltage = 0
        self.array_current = 0
        self.previous_channel = 0
        self.progress_value = 0
        
        self.file_number = 0
        self.directory_selected = 0
        self.index_number = 0
        
    
    # Connect computer to device via GPIB
    def gpib_connect(self, gpib):
        # Start Resource Manager & Open a connection with the SR785 via GPIB
        self.rm = pyvisa.ResourceManager()
        self.instrument = self.rm.open_resource('GPIB0::' + gpib + '::INSTR')

        # Set timeout value
        self.instrument.timeout = 20000
        
        # Set read & write terminations so host can communicate with SR785
        self.instrument.read_termination = '\n'
        self.instrument.write_termination = '\n'
    
    # Write test settings to the spectrum analyzer
    def sa_settings(self, source_level):
        # Set Output of Spectrum Analyzer to GPIB
        self.instrument.write("OUTX 0")

        # Set GPIB Control mode to Host
        self.instrument.write("PCIC 0")
        
        # Set Channel 1 & 2 Frequency Span from 0Hz to 1600Hz
        self.instrument.write("FSPN 2, 1.6E3")

        # Set Channel 1 & 2 Start Frequency to 0Hz so that it spans 0Hz to 1600Hz
        self.instrument.write("FSTR 2, 0")

        # Set Channel 1 & 2 FFT Line to 800
        self.instrument.write("FLIN 2, 3")


        ######## SET INPUT MODE OF CHANNEL 1 & 2 TO A. OTHERWISE CAN'T SET TO FLOATING
        self.instrument.write("I1MD 0")

        self.instrument.write("I2MD 0")


        # Set Channel 1 & 2 Grounding to Floating
        self.instrument.write("I1GD 0")
        
        self.instrument.write("I2GD 0")

        # Set Channel 1 & 2 Input Coupling to AC
        self.instrument.write("I1CP 1")
        
        self.instrument.write("I2CP 1")

        # Set Channel 1 & 2 FFT Window to BMH
        self.instrument.write("FWIN 2, 3")

        # Set Average Type to Linear
        self.instrument.write("FAVT 2, 0")
        
        # Set Display Average to RMS
        self.instrument.write("FAVM 2, 2")

        # Set Average Number to 16
        self.instrument.write("FAVN 2, 16")

        # Set Peak Units to RMS
        self.instrument.write("UNPK 2, 2")

        # Set Channel 1 Max to -50 dBVrms
        self.instrument.write("YMAX 0, -50")

        # Set Channel 1 Min to -175 dBVrms
        self.instrument.write("YMIN 0, -175")

        # Set Channel 2 Max to 0 dBVrms
        self.instrument.write("YMAX 1, 0")

        # Set Channel 2 Min to -100 dBVrms
        self.instrument.write("YMIN 1, -100")

        # Set Print Screen Output to ASCII Dump
        self.instrument.write("POUT 2")

        # Set Disk File Start Number to 0
        self.instrument.write("PFIL 0")

        # Set Source 1 to Sine with Frequency 620Hz
        self.instrument.write("S1FR 620 Hz")

        # Set Source 1 Amplitude
        self.instrument.write("S1AM " + source_level + " mVpk")

        # Set Source 2 to Sine with Frequency 600Hz
        self.instrument.write("S2FR 600 Hz")

        # Set Source 2 Amplitude
        self.instrument.write("S2AM " + source_level + " mVpk")

        # Set Channel 1 input range to auto
        self.instrument.write("A1RG 1")
        
        # Set Channel 2 input range to auto
        self.instrument.write("A2RG 1")
        
    # Plot the received data
    def plot_data(self, current_channel):
        
        # Create PDF
        pdf = PdfPages(self.directory +
                       "/" +
                       "Array_Channel_" +
                       str(current_channel) +
                       "_" +
                       str(self.ch1_freq) +
                       "Hz_" +
                       "Source " +
                       str(self.source) +
                       "_" +
                       "Results"".pdf")
        
        # Create title page
        first_page = plt.figure(figsize = (11.69, 8.27))
        first_page.clf()
        first_page.text(0.1,
                        0.1,
                        "Array S/N: " +
                        str(self.array_serial_number) +
                        "\n" +
                        "Source Level(mV): " +
                        str(self.source_level) +
                        "\n" +
                        "Array Breakout Box Voltage: " +
                        str(self.array_battery_voltage) +
                        "\n" +
                        "Array Current: " +
                        str(self.array_current) +
                        "\n" +
                        "Spectrum Analyzer Model #: " +
                        str(self.sa_model_number) +
                        "\n" +
                        "Spectrum Analyzer S/N: " +
                        str(self.sa_serial_number) +
                        "\n" + 
                        "Spectrum Analyzer Cal Due Date: " +
                        str(self.sa_cal_due_date) +
                        "\n",
                        transform = first_page.transFigure,
                        size = 20)
        pdf.savefig()
        plt.close()
        
        plt.figure(self.figure, figsize =(8,8))
        
        # Loop 6 times (1 for each plot)
        for i in range(0, 6):
            # On the 1st loop, 3rd loop, and 5th loop set the channel to plot to
            # 1
            if i % 2 == 0:
                self.ch_plot = 0
                
                # The 1st two plots start at 0, next 2 at 1600, and final 2 at 3200
                if i == 0:
                    self.freq_start = 0
                elif i == 2:
                    self.freq_start = 1600
                elif i == 4:
                    self.freq_start = 3200
            # On the 2nd, 4th, and 6th loop set the channel to plot to 2
            else:
                self.ch_plot = 1
                
                
            # Split data by comma delimiter, convert to float, put in list
            self.data_list = list(map(float, (self.data[i].split(","))))
                    
            # Create x -axis (0 to 800 in step size of 2)
            self.x_axis = list(range(self.freq_start, self.freq_start + 1602, 2))
            
            # Increment figure counter so the plot will open a new window each loop
            self.figure = self.figure + 1
            
            self.save_data(current_channel)
            
            # Increment file counter so a new file with data will be saved each loop
            self.file_number = self.file_number + 1

            self.index_number = self.index_number + 1
            
            if (self.index_number > 5):
                self.index_number = 0
        
        # Save all 6 plots to pdf
        pdf.savefig()
        #plt.close()
        
        # Loop for both ch1 and ch2 data
        for i in range (0, 2):
            # index 0, 2, 4  of data are ch1           1,3,5 are ch 2   
            # Split data by comma delimiter, convert to float, put in list
            self.data_list = list(map(float, (self.data[i].split(",")))) + \
                        list(map(float, (self.data[i + 2].split(",")))) + \
                        list(map(float, (self.data[i + 4].split(","))))
            
            #data[i] & data[i+2] both test 1600Hz. Del data[i] val for it
            del self.data_list[800]
            #data[i+2] & data[i+4] both test 3200Hz. Del data[i+2] val for it
            del self.data_list[1600]
            
            # Create list for 0-4800Hz in steps of 2
            self.x_axis = list(range(0, 4802, 2))
            
            
            # Plot list
            plt.plot(self.x_axis, self.data_list)
            
            plt.xlabel("Frequency (Hz)")
            plt.ylabel("dBVrms")
        
            # Channel 1 and 2 have different y axis, set depending on which one
            # is being plotted
            if (i == 0):
                plt.ylim([-175, -50])
            else:
                plt.ylim([-100, 0])
            
            # Title plot based on parameters
            plt.title("Channel " + str(i + 1))
            
            plt.tight_layout()
            

            
            # Save current plot to pdf
            pdf.savefig()
            plt.close()
            
            # Increment figure counter so the plot will open a new window each loop
            self.figure = self.figure + 1
        
        # If the source is on, store specific data points for table
        if (self.source == "On"):
            
            # Create a grid to store data points
            plt.figure(self.figure, figsize = (8,8))
            plt.subplot2grid((4,3), (0,0), colspan = 2, rowspan = 2)
        
        
            # If the current channel frequency is 620, grab data from
            # the corresponding frequencies
            if(self.ch1_freq == 620):
                self.data_list = list(map(float, (self.data[1].split(","))))
                self.dBVrms20 = self.data_list[10]
                self.dBVrms600 = self.data_list[300]
                self.dBVrms620 = self.data_list[310]
                self.dBVrms1220 = self.data_list[610]
        
        
                self.col_labels = ["Frequency", "dBVrms"]
                self.table_vals = [[20, self.dBVrms20],
                                   [600, self.dBVrms600],
                                   [620, self.dBVrms620],
                                   [1220, self.dBVrms1220]]
            # If the current channel frequency is 1140, grab data from
            # the corresponding frequencies
            elif(self.ch1_freq == 1140):
                self.data_list = list(map(float, (self.data[1].split(","))))
                self.dBVrms540 = self.data_list[270]
                self.dBVrms600 = self.data_list[300]
                self.dBVrms1140 = self.data_list[570]
                
                self.data_list = list(map(float, (self.data[3].split(","))))
                self.dBVrms1740 = self.data_list[70]
        
        
                self.col_labels = ["Frequency", "dBVrms"]
                self.table_vals = [[540, self.dBVrms540],
                                   [600, self.dBVrms600],
                                   [1140, self.dBVrms1140],
                                   [1740, self.dBVrms1740]]
                
                
        
            # Create table with values selected from above
            plt.table(cellText = self.table_vals,
                          colLabels = self.col_labels)
            
        
            # Remove empty plot from above the table
            plt.tick_params(axis = 'x',
                            which = 'both',
                            bottom = False,
                            top = False,
                            labelbottom = False)
            plt.tick_params(axis = 'y',
                            which = 'both',
                            right = False,
                            left = False,
                            labelleft = False)
            
            for pos in ['right','top','bottom','left']:
                plt.gca().spines[pos].set_visible(False)
                
                
            
            plt.plot()
            plt.title("Array Channel " +
                      str(current_channel) +
                      " 600 Hz / " + 
                      str(self.ch1_freq) +
                      " Hz",
                      fontweight="bold",
                      y = 0.02)
            
            # Save current table to pdf
            pdf.savefig()
            plt.close()
                
            
            # Increment figure counter so the plot will open a new window each loop
            self.figure = self.figure + 1
            
        pdf.close()
        
    # Get data of displays from spectrum analyzer
    def get_data(self):
        
        self.data = []
    
        # Send ch_1 freq to signal analyzer based on user input   
        if (self.ch1_freq == 620):
            # Set Source 1 to Sine with Frequency 620Hz
            self.instrument.write("S1FR 620 Hz")
        elif (self.ch1_freq == 1140):
            # Set Source 1 to Sine with Frequency 1140Hz
            self.instrument.write("S1FR 1140 Hz")
        
        # Send source value to signal analyzer based on user input
        if (self.source == "On"):
            # Set Source to On
            self.instrument.write("SRCO 1")
        elif (self.source == "Off"):
            # Set Source to Off
            self.instrument.write("SRCO 0")
        
        
        # Loop for 6 times, every other loop changing the channel to query
        # At the 1st, 3rd, and 5th loop change the starting frequency so that
        # a different span is seen. 0-1600, 1600-3200, 3200-4800
        for i in range(0, 6):
            
            if i % 2 == 0:
    
                if i == 0:
                    self.instrument.write("FSTR 2, 0")
                    self.instrument.write("STRT")
                    
                elif i == 2:
                    self.instrument.write("FSTR 2, 1600")
                    self.instrument.write("STRT")
                    
                elif i == 4:
                    self.instrument.write("FSTR 2, 3200")
                    self.instrument.write("STRT")
                                    
                # After every frequency start change, let analyzer average
                time.sleep(12)
                
                # After analyzer has averaged, appened received string to the
                # array of strings
                self.data.append(self.instrument.query("DSPY ? 0"))
            else:
                time.sleep(0.5)
                # After analyzer has averaged, appened received string to the
                # array of strings
                self.data.append(self.instrument.query("DSPY ? 1"))
                
            self.progress_value = self.progress_value + 5.56

    # Save received data to text files
    def save_data(self, current_channel):
    
            
        try:
            if(self.previous_channel != current_channel):
                os.mkdir(self.directory +
                         "/" + 
                         "Channel_" +
                         str(current_channel))
        except:
            pass
        
        self.previous_channel = current_channel
        
        self.data_writer = open(self.directory + 
                                "/" + 
                                "Channel_" +
                                str(current_channel) +
                                "/" +
                                "SCRN" + 
                                "{:04d}".format(self.file_number) + 
                                ".txt", 
                                mode = 'w')
        
        for i in range (0, 801):
            self.data_writer.write(str("{:.7e}".format(self.x_axis[i])) + 
                                   "    " +
                                   str("{:.7e}".format(self.data_list[i])) +
                                   "\n")
            

        # Close opened file
        self.data_writer.close()
            
def main(): 

    MainPage().mainloop()


if __name__ == '__main__':
    main()