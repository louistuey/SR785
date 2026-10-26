# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 18:30:34 2020

@author: mark.a.thomsen@spawar.navy.mil
"""

import pyvisa

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

import time
import threading

import tkinter as tk
from tkinter import messagebox
import tkinter.filedialog as writer 


class MainPage(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        
        tk.Tk.winfo_toplevel(self).title("Array Crosstalk Test")
        
        # Create spectrum analyzer object
        self.plotter = SR785()
        
        # Initialize variables that will hold entry values
        self.array_serial_number = tk.StringVar()
        self.array_voltage = tk.StringVar()
        self.array_current = tk.StringVar()
        self.sa_model_number = tk.StringVar()
        self.sa_serial_number = tk.StringVar()
        self.cal_due_date = tk.StringVar()
        self.number_channels = tk.StringVar()
        self.current_channel = tk.StringVar()
        self.source_channel = tk.StringVar()
        self.gpib_number = tk.StringVar()
        self.sa_frequency = tk.StringVar()
        
        # Set default value for curent & source channels
        self.current_channel.set("1")
        self.source_channel.set("1")
        
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
        
        self.source_channel_label = tk.Label(self.left_frame,
                                              text = "Source Channel: ",
                                              font = ("Arial", 20))
        
        self.source_channel_label.pack(expand = True,
                                        fill = "both")
        
        self.current_channel_label = tk.Label(self.left_frame,
                                              text = "Current Channel: ",
                                              font = ("Arial", 20))
        
        self.current_channel_label.pack(expand = True,
                                        fill = "both")
        
    
        self.gpib_number_label = tk.Label(self.left_frame,
                                          text = "GPIB #:",
                                          font = ("Arial", 20))
        self.gpib_number_label.pack(expand = True,
                                    fill = "both",
                                    pady = (5, 0))
        
        
        self.sa_frequency_label = tk.Label(self.left_frame,
                                           text = "Frequency: ",
                                           font = ("Arial", 20))
        
        self.sa_frequency_label.pack(expand = True,
                                     fill = "both",
                                     pady = 20)
    
    
        # Set Values to Right side of the screen
        self.array_serial_number_entry = tk.Entry(self.right_frame,
                                                  textvariable = self.array_serial_number,
                                                  font = ("Arial", 20))
        
        self.array_serial_number_entry.pack(expand = True,
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
        
        self.source_channel_entry = tk.Label(self.right_frame,
                                              textvariable = self.source_channel,
                                              font = ("Arial", 20))
        
        self.source_channel_entry.pack(expand = True,
                                        fill = "both",
                                        pady = (5, 0))
        
        self.current_channel_entry = tk.Label(self.right_frame,
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
        
        self.sa_frequency_value = tk.Label(self.right_frame,
                                           width = 12,
                                           textvariable = self.sa_frequency,
                                           font = ("Arial", 20))
        
        self.sa_frequency_value.pack(expand = True,
                                     fill = "both",
                                     pady = 20)
        
        
        # Start button underneath the two frames
        self.start_button = tk.Button(self.bottom_frame,
                                      text = "Start",
                                      command = self.start_press,
                                      font = ("Arial", 20))
        
        self.start_button.pack(expand = True,
                               pady = 15)
        
        
        # Start button underneath the two frames
        self.continue1_button = tk.Button(self.bottom_frame,
                                          text = "Continue",
                                          command = self.continue1_press,
                                          font = ("Arial", 20))
    
    
    
    # On start button press
    def start_press(self):
        
        
        # Store test set up information from inputs
        self.plotter.sa_model_number = str(self.sa_model_number.get())
        self.plotter.array_serial_number = str(self.array_serial_number.get())
        self.plotter.sa_serial_number = str(self.sa_serial_number.get())
        self.plotter.cal_due_date = str(self.cal_due_date.get())
        self.plotter.array_voltage = str(self.array_voltage.get())
        self.plotter.array_current = str(self.array_current.get())
        self.plotter.number_channels = str(self.number_channels.get())
        self.plotter.source_channel = str(self.source_channel.get())
        
        # Reset all variables when start is pressed
        self.plotter.clear_data()
        self.finished = False
        
         #Get directory to save all files to
        if(self.plotter.directory_selected == 0):
            self.plotter.directory = writer.askdirectory()
            self.plotter.directory_selected = 1
        
        
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
                self.plotter.sa_settings()
                
                # Query the SR785 to make sure comms are working
                self.plotter.instrument.query("*IDN ?")
                
                # Removes start button from window
                self.start_button.pack_forget()
                
                # Add continue button to window
                self.continue1_button.pack(expand = True,
                                   pady = 15)
                
                # Disable all entries during test
                self.array_serial_number_entry.config(state = "disabled")
                self.array_voltage_entry.config(state = "disabled")
                self.array_current_entry.config(state = "disabled")
                self.sa_model_number_entry.config(state = "disabled")
                self.sa_serial_number_entry.config(state = "disabled")
                self.cal_due_date_entry.config(state = "disabled")
                self.number_channels_entry.config(state = "disabled")
                self.current_channel_entry.config(state = "disabled")
                self.gpib_number_entry.config(state = "disabled")
                
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
        
        # Set finished thread state to false
        self.finished = False
        
        # thread the test function so it doesn't lock up the GUI
        thread = threading.Thread(target = self.run_test)
        thread.daemon = True
        thread.start()
        
        # Disable continue button while test is running
        self.continue1_button.config(state = "disabled")
        
        # Prevents function from continuing while threaded test function is
        # running
        self.check_status()
        
        
        # Once test is complete, incremenet channel to test on
        self.current_channel.set(str(int(self.current_channel.get()) + 1))

        # If current channel is greater than the number of channels, 
        # save data of current channel, increment to the next source channel 
        # & repeat
        if(int(self.current_channel.get()) > int(self.number_channels.get())):
            # Reset current channel to 1
            self.current_channel.set("1")
            
            # Set plotters source value to current source value on GUI
            self.plotter.source_channel = self.source_channel.get()
            
            # Save data
            self.plotter.save_data()
            
            # Clear data in arrays for next loop
            self.plotter.all_data.clear()
            self.plotter.channel_data.clear()
            
            # Increment source channel
            self.source_channel.set(str(int(self.source_channel.get()) + 1))
            
            
            
            # If the source channel is higher than the number of channels,
            # test is completed. Reset variables and close pdf
            if (self.source_channel.get() > self.number_channels.get()):
                
                # Test is completed, reset all values
                self.source_channel.set("1")
                self.running = False
                self.plotter.pdf.close()
                self.plotter.directory_selected = 0
                
                # Removes start button from window
                self.continue1_button.pack_forget()
                
                # Clear frequency after test
                self.sa_frequency.set("")

            
            
                # Add continue button to window
                self.start_button.pack(expand = True,
                                       pady = 15)
                
                
                self.plotter.clear_data()
                self.finished = False
                
                # Set default value fro curent & source channels
                self.current_channel.set("1")
                self.source_channel.set("1")
                
                # Pop up saying test was canceled when pressing
                messagebox.showinfo("Notification",
                                    "Test has been completed.")
                
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
                self.source_channel_entry.config(state = "normal")
            
                
                
                
                
            else:
                MsgBox = messagebox.askquestion("Alert",
                                                "Are you ready to proceed to \n" +
                                                "Source Channel: " +
                                                str(self.source_channel.get()) +
                                                " ?")
                
                if (MsgBox == "yes"):
                    self.continue1_press()
                
                else:
                    
                    self.plotter.clear_data()
                    self.finished = False
                    
                    # Set default value fro curent & source channels
                    self.current_channel.set("1")
                    self.source_channel.set("1")
                    
                    # Pop up saying test was canceled when pressing
                    messagebox.showinfo("Notification",
                                        "Test has been canceled.")
                
                    # Enable continue button & inputs once test is done
                    self.continue1_button.config(state = "normal")
                    self.array_serial_number_entry.config(state = "normal")
                    self.array_voltage_entry.config(state = "normal")
                    self.array_current_entry.config(state = "normal")
                    self.sa_model_number_entry.config(state = "normal")
                    self.sa_serial_number_entry.config(state = "normal")
                    self.cal_due_date_entry.config(state = "normal")
                    self.number_channels_entry.config(state = "normal")
                    self.current_channel_entry.config(state = "normal")
                    self.gpib_number_entry.config(state = "normal")
                    self.source_channel_entry.config(state = "normal")
        
                    # Clear frequency after test
                    self.sa_frequency.set("")
                    
                    
                    # Removes start button from window
                    self.continue1_button.pack_forget()
                    
                    # Add continue button to window
                    self.start_button.pack(expand = True,
                                           pady = 15)
                    
                    
            


        else:
            MsgBox = messagebox.askquestion("Alert",
                                            "Are you ready to proceed to \n" +
                                            "Current Channel: " +
                                            str(self.current_channel.get()) +
                                            " ?")
            if (MsgBox == "yes"):
                self.continue1_press()
            
            else:
                
                self.plotter.clear_data()
                self.finished = False
                
                # Set default value fro curent & source channels
                self.current_channel.set("1")
                self.source_channel.set("1")
                
                # Pop up saying test was canceled when pressing
                messagebox.showinfo("Notification",
                                    "Test has been canceled.")
                
                # Enable continue button & inputs once test is done
                self.continue1_button.config(state = "normal")
                self.array_serial_number_entry.config(state = "normal")
                self.array_voltage_entry.config(state = "normal")
                self.array_current_entry.config(state = "normal")
                self.sa_model_number_entry.config(state = "normal")
                self.sa_serial_number_entry.config(state = "normal")
                self.cal_due_date_entry.config(state = "normal")
                self.number_channels_entry.config(state = "normal")
                self.current_channel_entry.config(state = "normal")
                self.gpib_number_entry.config(state = "normal")
                self.source_channel_entry.config(state = "normal")
    
                # Clear frequency after test
                self.sa_frequency.set("")
                
                
                # Removes start button from window
                self.continue1_button.pack_forget()
                
                # Add continue button to window
                self.start_button.pack(expand = True,
                                       pady = 15)
                
                
                
            
                
        

        
    # Loops until run_test is complete. Prevents GUI from continuing
    # on while loop is running
    def check_status(self):
        while self.finished is False:
            self.update()
            
    # Crosstalk Test Function. Run test & save data to pdf
    def run_test(self):
        
#        # Cycle through the 10 frequencies to test
        for i in range (0, 10):
            # Set the spectrum analyzer's frequency
            self.plotter.set_freq()
            
            # Store SA's frequency to local gui variable
            self.sa_frequency.set(self.plotter.ch1_freq)
            
            # queries & stores data of 10 different frequencies from the
            # current channel
            self.plotter.get_data()
               
        
        # Store current channel data into list of all channels data
        self.plotter.all_data.append(self.plotter.channel_data)
        
        # Set thread to finished
        self.finished = True
        
        
# Spectrum analyzer class for SR785 SA
class SR785():
    
    
    def __init__(self):
        self.ch1_freq = 0
        self.freq_index = 0
        
        self.sa_model_number = 0
        self.array_serial_number = 0
        self.sa_serial_number = 0
        self.cal_due_date = 0
        self.array_voltage = 0
        self.array_current = 0
        self.number_channels = 0
        self.source_channel = 0
        self.running = False
        
        self.channel_data = []
        self.all_data = []
        self.directory_selected = 0
        
        
    # Connect computer to device via GPIB
    def gpib_connect(self, gpib):
        # Start Resource Manager & Open a connection with the SR785 via GPIB
        self.rm = pyvisa.ResourceManager()
        self.instrument = self.rm.open_resource('GPIB0::' + gpib + '::INSTR')

        # Set read & write terminations so host can communicate with SR785
        self.instrument.read_termination = '\n'
        self.instrument.write_termination = '\n'
    
    # Write test settings to the spectrum analyzer
    def sa_settings(self):
        # Set Output of Spectrum Analyzer to GPIB
        self.instrument.write("OUTX 0")

        # Set Print/Plot/Dump Destination to GPIB
        self.instrument.write("PDST 3")

        # Set Print/Plot/Dump GPIB Address to XX in GPIB0::XX::INSTR
        self.instrument.write("PLTA 10")

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

        # Set Average Number to 16
        self.instrument.write("FAVN 2, 16")

        # Set Peak Units to RMS
        self.instrument.write("UNPK 2, 2")

        # Set Channel 1 Max to -50 dBVrms
        self.instrument.write("YMAX 0, 0")

        # Set Channel 1 Min to -150 dBVrms
        self.instrument.write("YMIN 0, -100")

    

        # Set Channel 2 Max to 0 dBVrms
        self.instrument.write("YMAX 1, 0")

        # Set Channel 2 Min to -150 dBVrms
        self.instrument.write("YMIN 1, -100")


        # Set Print Screen Output to ASCII Dump
        self.instrument.write("POUT 2")

        # Set Disk File Start Number to 0
        self.instrument.write("PFIL 0")

        # Set Source 1 to Sine with Frequency 10Hz
        self.instrument.write("S1FR 10Hz")

        # Set Source 1 Amplitude to 1.6mVpk
        self.instrument.write("S1AM 2.2 mVpk")

        # Set Source 2 to Sine with Frequency 10Hz
        self.instrument.write("S2FR 10 Hz")

        # Set Source 2 Amplitude to 1.6mVpk
        self.instrument.write("S2AM 2.2 mVpk")
        
        # Set Channel 1 input range to auto
        self.instrument.write("A1RG 1")
        
        # Set Channel 2 input range to auto
        self.instrument.write("A2RG 1")
        
        # Set Source to On
        self.instrument.write("SRCO 1")
        

    # Sets frequency of spectrum analyzer
    def set_freq(self):
        if(self.freq_index == 0):
            # Set Source 1 to Sine with Frequency 10Hz
            self.instrument.write("S1FR 10.07Hz")
            
            # SetStart Frequency to 0Hz so drive signal is in the span
            self.instrument.write("FSTR 2, 0")
            
            # Set freq to display
            self.ch1_freq = 10.07
            
        elif(self.freq_index == 1):
            # Set Source 1 to Sine with Frequency 20Hz
            self.instrument.write("S1FR 20.14Hz")
            
            # Set freq to display
            self.ch1_freq = 20.14
        elif(self.freq_index == 2):
            # Set Source 1 to Sine with Frequency 40Hz
            self.instrument.write("S1FR 40.28Hz")
            
            # Set freq to display
            self.ch1_freq = 40.28
        elif(self.freq_index == 3):
            # Set Source 1 to Sine with Frequency 80Hz
            self.instrument.write("S1FR 80Hz")
            
            # Set freq to display
            self.ch1_freq = 80.00
        elif(self.freq_index == 4):
            # Set Source 1 to Sine with Frequency 160Hz
            self.instrument.write("S1FR 160Hz")
            
            # Set freq to display
            self.ch1_freq = 160.00
        elif(self.freq_index == 5):
            # Set Source 1 to Sine with Frequency 320Hz
            self.instrument.write("S1FR 319.80Hz")
            
            # Set freq to display
            self.ch1_freq = 319.80
        elif(self.freq_index == 6):
            # Set Source 1 to Sine with Frequency 640Hz
            self.instrument.write("S1FR 639.80Hz")
            
            # Set freq to display
            self.ch1_freq = 639.80
        elif(self.freq_index == 7):
            # Set Source 1 to Sine with Frequency 1280Hz
            self.instrument.write("S1FR 1280Hz")
            
            # Set freq to display
            self.ch1_freq = 1280.00
        elif(self.freq_index == 8):
            # Set Source 1 to Sine with Frequency 2560Hz
            self.instrument.write("S1FR 2560Hz")
            
            # SetStart Frequency to 2560Hz so drive signal is in the span
            self.instrument.write("FSTR 2, 1600")
            
            # Set freq to display
            self.ch1_freq = 2560.00
        elif(self.freq_index == 9):
            ########
            # Set Source 1 to Sine with Frequency 4000Hz
            self.instrument.write("S1FR 4000Hz")
            
            # SetStart Frequency to 4000Hz so drive signal is in the span
            self.instrument.write("FSTR 2, 3200")
            
            # Set freq to display
            self.ch1_freq = 4000.00
        
        self.freq_index = self.freq_index + 1
        
        if self.freq_index == 10:
            self.freq_index = 0
        
        
    # Get data of displays from spectrum analyzer
    def get_data(self):
        
        # Start measuring
        self.instrument.write("STRT")
            
        # After every frequency change, let analyzer average
        time.sleep(12)
                
        # After analyzer has averaged, appened received string to the
        # array of strings
        
        # Split data by comma delimiter, convert to float, put in list
        self.raw_data = self.instrument.query("DSPY ? 1")
        self.data_list = list(map(float, (self.raw_data.split(","))))
        self.channel_data.append(self.data_list)

        
    # Save received data to PDF
    def save_data(self):
        
        # Clear table vals and column vals every save
        self.col_labels = ["Frequency"]
        self.table_vals = []
               
        # If running for the first loop, create PDF and save
        # Otherwise, just write to PDF
        if (self.running is False):
            self.pdf = PdfPages(self.directory +
                                "/" +
                                "Crosstalk_Results" +
                                ".pdf")
            self.running = True

            # Create title page
            first_page = plt.figure(figsize = (11.69, 8.27))
            first_page.clf()
            first_page.text(0.1,
                            0.1,
                            "Array S/N: " +
                            str(self.array_serial_number) +
                            "\n" +
                            "Array Breakout Box Voltage: " +
                            str(self.array_voltage) +
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
                            str(self.cal_due_date) +
                            "\n",
                            transform = first_page.transFigure,
                            size = 20)
            self.pdf.savefig()
            plt.close()
        
        # Create a grid to store data points
        plt.figure()
        
        # Create 10 rows with labels for table
        self.row1_10Hz = [10]
        self.row2_20Hz = [20]
        self.row3_40Hz = [40]
        self.row4_80Hz = [80]
        self.row5_160Hz = [160]
        self.row6_320Hz = [320]
        self.row7_640Hz = [640]
        self.row8_1280Hz = [1280]
        self.row9_2560Hz = [2560]
        self.row10_4000Hz = [4000]
        
        # For every channel, append all frequency data of that channel to 
        # the rows that will be stored in the table
        for channel in range(int(self.number_channels)):
            
            self.col_labels.append("Channel " +
                                   str(channel + 1) +
                                   " dBVrms")
            
            self.row1_10Hz.append(self.all_data[channel][(channel) * 10 + 0][5])
            self.row2_20Hz.append(self.all_data[channel][(channel) * 10 + 1][10])
            self.row3_40Hz.append(self.all_data[channel][(channel) * 10 + 2][20])
            self.row4_80Hz.append(self.all_data[channel][(channel) * 10 + 3][40])
            self.row5_160Hz.append(self.all_data[channel][(channel) * 10 + 4][80])
            self.row6_320Hz.append(self.all_data[channel][(channel) * 10 + 5][160])
            self.row7_640Hz.append(self.all_data[channel][(channel) * 10 + 6][320])
            self.row8_1280Hz.append(self.all_data[channel][(channel) * 10 + 7][640])
            
            # Last two elements of a channel range from 1600-3200 and 3200-4800
            # Respectively. 1600 + (480 * 2) = 2560. 
            #               3200 + (400 * 2) = 4000
            self.row9_2560Hz.append(self.all_data[channel][(channel) * 10 + 8][480])
            self.row10_4000Hz.append(self.all_data[channel][(channel) * 10 + 9][400])

        
        # Save all row values in a list called table vals
        self.table_vals = [self.row1_10Hz,
                           self.row2_20Hz,
                           self.row3_40Hz,
                           self.row4_80Hz,
                           self.row5_160Hz,
                           self.row6_320Hz,
                           self.row7_640Hz,
                           self.row8_1280Hz,
                           self.row9_2560Hz,
                           self.row10_4000Hz]
        
        # Create table with values selected from above
        plt.table(cellText = self.table_vals,
                      colLabels = self.col_labels,
                      loc='center',
                      fontsize = 30)

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
            
            
        plt.title("Channel " + 
                  self.source_channel + 
                  " as Source", 
                  fontweight = "bold",
                  y = 0.95)
        
        # Plot the table
        plt.plot()
        
        # Automatically provide table layout
        plt.tight_layout()
        
        # Save table to pdf
        self.pdf.savefig()
        
        
    # Clears previous saved data for next test
    def clear_data(self):
        self.channel_data.clear()
        self.all_data.clear()
        self.directory_selected = 0
        
        
def main(): 

    MainPage().mainloop()


if __name__ == '__main__':
    main()