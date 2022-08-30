import time
import tkinter as tk
import serial.tools.list_ports
from tkinter import ttk, Label
from PIL import ImageTk, Image
from core.threading_function import Thread_with_trace
from core.modbus_communication import Module
from pymodbus.client.sync import ModbusSerialClient
from datetime import datetime
from core.plot_chart import Plot


class Frames:
    """
    Class responsible for creating the GUI
    """

    def __init__(self, directory_path: str):
        label_style = ttk.Style()
        label_style.configure('Blue.TLabelframe.Label', foreground='blue')

        self.width = 20
        self.show_flag = False
        self.my_plot = Plot()
        self.directory_path = directory_path

    @staticmethod
    def main_frame(win):

        # Main Frame
        main = ttk.LabelFrame(win, text="", style="Blue.TLabelframe")
        main.grid(column=0, row=0, sticky="WENS", padx=10, pady=10)
        return main

    def configuration_frame(self, win):

        # Configuration Frame
        config_frame = ttk.LabelFrame(win, text="Config", style="Blue.TLabelframe")
        config_frame.grid(column=0, row=0, sticky='NWS', padx=20, pady=10)

        # Port COM
        ports = serial.tools.list_ports.comports()
        com_ports = [ports[i][0] for i in range(len(ports))]

        ttk.Label(config_frame, text="Port COM:").grid(column=0, row=0)
        device = tk.StringVar
        self.port_com = ttk.Combobox(config_frame, width=self.width, textvariable=device, state='readonly')
        self.port_com['values'] = com_ports
        self.port_com.grid(column=0, row=1, sticky=tk.EW, padx=10)
        self.port_com.current(0)

        # Modbus ID
        ttk.Label(config_frame, text="Modbus ID").grid(column=0, row=3)
        self.modbus_id = tk.StringVar()
        ttk.Entry(config_frame, width=20, textvariable=self.modbus_id).grid(column=0, row=4, sticky=tk.EW, padx=10)
        self.modbus_id.set(1)

        # Baudrate
        ttk.Label(config_frame, text="Baudrate").grid(column=0, row=5)
        self.baudrate = tk.StringVar()
        baudrate_box = ttk.Entry(config_frame, width=self.width, textvariable=self.baudrate)
        baudrate_box.grid(column=0, row=6, sticky=tk.EW, padx=10)
        self.baudrate.set(115200)

        # Parity Bits
        ttk.Label(config_frame, text="Parity Bits").grid(column=1, row=0)
        parity_bits = tk.StringVar
        self.parity_bits = ttk.Combobox(config_frame, width=self.width, textvariable=parity_bits, state='readonly')
        self.parity_bits['values'] = ["N", "O", "E"]
        self.parity_bits.grid(column=1, row=1, sticky=tk.EW, padx=10)
        self.parity_bits.current(0)

        # Stop Bits
        ttk.Label(config_frame, text="Stop Bits").grid(column=1, row=3)
        stop_bits = tk.StringVar
        self.stop_bits = ttk.Combobox(config_frame, width=self.width, textvariable=stop_bits, state='readonly')
        self.stop_bits['values'] = [1, 2]
        self.stop_bits.grid(column=1, row=4, sticky=tk.EW, padx=10)
        self.stop_bits.current(0)

        # Data Bits
        ttk.Label(config_frame, text="Data Bits").grid(column=1, row=5)
        data_bits = tk.StringVar
        self.data_bits = ttk.Combobox(config_frame, width=self.width, textvariable=data_bits, state='readonly')
        self.data_bits['values'] = [7, 8]
        self.data_bits.grid(column=1, row=6, sticky=tk.EW, padx=10)
        self.data_bits.current(1)

        # Timeout
        ttk.Label(config_frame, text="Timeout").grid(column=2, row=0)
        self.timeout = tk.StringVar()
        ttk.Entry(config_frame, width=self.width, textvariable=self.timeout).grid(column=2, row=1, sticky=tk.EW,
                                                                                  padx=10)
        self.timeout.set(1000)

        # Read time
        ttk.Label(config_frame, text="Read time").grid(column=2, row=3)
        self.read_time = tk.StringVar()
        ttk.Entry(config_frame, width=self.width, textvariable=self.read_time).grid(column=2, row=4, sticky=tk.EW,
                                                                                    padx=10)
        self.read_time.set(0)

    def registers_frame(self, win):

        # Registers Frame
        reg_frame = ttk.LabelFrame(win, text="Registers", style="Blue.TLabelframe")
        reg_frame.grid(column=1, row=0, sticky='NWS', padx=20, pady=10)

        # Register 1
        ttk.Label(reg_frame, text="1.").grid(column=0, row=1)
        ttk.Label(reg_frame, text="Register Name:").grid(column=1, row=0)
        self.reg_1_name = tk.StringVar()
        ttk.Entry(reg_frame, width=20, textvariable=self.reg_1_name).grid(column=1, row=1, sticky=tk.EW, padx=10)

        ttk.Label(reg_frame, text="Register Address:").grid(column=2, row=0)
        self.reg_1_address = tk.StringVar()
        ttk.Entry(reg_frame, width=20, textvariable=self.reg_1_address).grid(column=2, row=1, sticky=tk.EW, padx=10)

        ttk.Label(reg_frame, text="Register Value:").grid(column=3, row=0)
        self.reg_1_value = tk.StringVar()
        ttk.Entry(reg_frame, width=20, textvariable=self.reg_1_value, state="disabled").grid(column=3, row=1,
                                                                                             sticky=tk.EW, padx=10)

        # Register 2
        ttk.Label(reg_frame, text="2.").grid(column=0, row=4)
        ttk.Label(reg_frame, text="Register Name:").grid(column=1, row=3)
        self.reg_2_name = tk.StringVar()
        ttk.Entry(reg_frame, width=20, textvariable=self.reg_2_name).grid(column=1, row=4, sticky=tk.EW, padx=10)

        ttk.Label(reg_frame, text="Register Address:").grid(column=2, row=3)
        self.reg_2_address = tk.StringVar()
        ttk.Entry(reg_frame, width=20, textvariable=self.reg_2_address).grid(column=2, row=4, sticky=tk.EW, padx=10)

        ttk.Label(reg_frame, text="Register Value:").grid(column=3, row=3)
        self.reg_2_value = tk.StringVar()
        ttk.Entry(reg_frame, width=20, textvariable=self.reg_2_value, state="disabled").grid(column=3, row=4,
                                                                                             sticky=tk.EW, padx=10)

        # Register 3
        ttk.Label(reg_frame, text="3.").grid(column=0, row=7)
        ttk.Label(reg_frame, text="Register Name:").grid(column=1, row=6)
        self.reg_3_name = tk.StringVar()
        ttk.Entry(reg_frame, width=20, textvariable=self.reg_3_name).grid(column=1, row=7, sticky=tk.EW, padx=10)

        ttk.Label(reg_frame, text="Register Address:").grid(column=2, row=6)
        self.reg_3_address = tk.StringVar()
        ttk.Entry(reg_frame, width=20, textvariable=self.reg_3_address).grid(column=2, row=7, sticky=tk.EW, padx=10)

        ttk.Label(reg_frame, text="Register Value:").grid(column=3, row=6)
        self.reg_3_value = tk.StringVar()
        ttk.Entry(reg_frame, width=20, textvariable=self.reg_3_value, state="disabled").grid(column=3, row=7,
                                                                                             sticky=tk.EW, padx=10)

    def buttons_frame(self, win):

        # Buttons Frame
        but_frame = ttk.LabelFrame(win, text="Run", style="Blue.TLabelframe")
        but_frame.grid(column=2, row=0, sticky='NWS', padx=20, pady=10)

        # Start button
        def start():
            def run_communication():
                # global reg_values
                self.client_rs485 = ModbusSerialClient(port=self.port_com.get(),
                                                       method="RTU",
                                                       baudrate=int(self.baudrate.get()),
                                                       parity=self.parity_bits.get(),
                                                       stopbits=int(self.stop_bits.get()),
                                                       bytesize=int(self.data_bits.get()),
                                                       timeout=int(self.timeout.get()))

                self.client_rs485.connect()

                device = Module()
                device.modbus_init(self.client_rs485, int(self.modbus_id.get()))
                if device.check_connection() is None:
                    self.client_rs485.close()
                    return False

                registers = ["reg_" + str(register + 1) for register in range(3)]

                registers_info = {}
                for reg in registers:
                    reg_info = {}
                    try:
                        reg_name = getattr(self, str(reg) + "_name")
                        reg_addr = getattr(self, str(reg) + "_address")
                        reg_info["name"] = reg_name.get()
                        reg_info["address"] = int(reg_addr.get())
                    except:
                        reg_info["name"] = None
                        reg_info["address"] = None
                    registers_info[reg] = reg_info

                time_delay = float(self.read_time.get())

                reg_1_values = []
                reg_2_values = []
                reg_3_values = []

                while True:
                    read_time = datetime.now().time()
                    for reg in registers_info:
                        address = registers_info[reg]['address']
                        if address is not None:
                            read_value = device.read_reg(address)

                            # set value in GUI slot
                            reg_value = getattr(self, str(reg) + "_value")
                            reg_value.set(read_value)

                            # set value in values list
                            reg_values = eval(reg + '_values')
                            reg_values.append((read_time, read_value))
                            registers_info[reg]['values'] = reg_values

                    self.my_plot.plot_chart(registers_info, self.directory_path)
                    self.chart_frame()

                    time.sleep(time_delay)

            start_button.configure(state="disabled")
            stop_button.configure(state="enabled")
            show_button.configure(state="enabled")

            self.main_script = Thread_with_trace(target=run_communication)
            self.main_script.start()

        start_button = ttk.Button(but_frame, text="Start", command=start, width=20)
        start_button.grid(column=0, row=0, sticky=tk.N, pady=10)

        # Stop button
        def stop():
            start_button.configure(state="enabled")
            stop_button.configure(state="disabled")
            show_button.configure(state="disabled")
            self.client_rs485.close()

            self.main_script.kill()
            self.main_script.join()

        stop_button = ttk.Button(but_frame, text="Stop", command=stop, width=20)
        stop_button.grid(column=0, row=1, sticky=tk.N, pady=10)
        stop_button.configure(state="disabled")

        # Show plot button
        def show():
            self.my_plot.show_plot = True

        show_button = ttk.Button(but_frame, text="Show Plot", command=show, width=20)
        show_button.grid(column=0, row=2, sticky=tk.N, pady=10)
        show_button.configure(state="disabled")

    def chart_frame(self):
        try:
            self.pil_image = Image.open(self.directory_path + "history.jpeg")

            width = 1150
            height = 500

            self.pil_image_resized = self.pil_image.resize((width, height), Image.ANTIALIAS)

            self.img = ImageTk.PhotoImage(self.pil_image_resized)
            self.in_frame = Label(image=self.img)
            self.in_frame.image = self.img

            self.in_frame.place(x=20, y=220)
        except:
            pass
