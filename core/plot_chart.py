import matplotlib.pyplot as plt
import numpy as np


class Plot:

    def __init__(self):
        self.show_plot = False

    def plot_chart(self, registers_info: dict, directory_path: str):
        plt.figure(figsize=(17, 6))

        # add colors for registers
        colors = ['dodgerblue', 'red', 'green']
        count = 0
        for reg in registers_info:
            registers_info[reg]['color'] = colors[count]
            count += 1

        # add values to axis
        for reg in registers_info:
            register_name = registers_info[reg]['name']
            if register_name is not None:
                x_axis = []
                y_axis = []
                for time, value in registers_info[reg]['values']:
                    y_axis.append(value)
                    x_axis.append(str(time))
                if len(x_axis) >= 5:
                    plt.xticks(np.arange(0, len(x_axis), step=len(x_axis) // 5))
                plt.plot(x_axis, y_axis, registers_info[reg]['color'], label=register_name, linewidth=1)

        # plot config
        plt.xlabel("Time", fontsize=16)
        plt.ylabel("Register values", fontsize=16)

        plt.title("Modbus History Chart", fontsize=16)
        plt.legend()
        plt.grid(False)
        plt.savefig(directory_path + 'history.jpeg', dpi=400, quality=100)

        # show plot for user in different window
        if self.show_plot is True:
            plt.show()
            self.show_plot = False

        plt.clf()
        plt.close('all')
