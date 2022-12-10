from PyQt5.QtWidgets import *
from autoservice import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps,True)

class Controller(QMainWindow, Ui_MainWindow):
    '''
    A class representing details for a controller object. Contains all functions for GUI
    '''
    def __init__(self, *args, **kwargs):
        '''
        Contstructor to create initial state of a controller object.
        '''
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.submit_button.clicked.connect(lambda: self.submit())
        self.clear_button.clicked.connect(lambda: self.clear())

    def service1(self) -> int:
        '''
        Method to get total of service 1 that the user enters
        :return: Total of service 1.
        '''
        service1_total = 0
        service1 = int(self.input_service1.text())
        if service1 == 1:
            service1_total += 35
        elif service1 == 2:
            service1_total += 19
        elif service1 == 3:
            service1_total += 7
        elif service1 == 4:
            service1_total += 12
        else:
            self.text_output.setText(f'Please enter a number for a service. (1/2/3/4)')
        return service1_total

    def service2(self) -> int:
        '''
        Method to get total of service 2 that the user enters
        :return: Total of service 2
        '''
        service2_total = 0
        service2 = int(self.input_service2.text())
        if service2 == 1:
            service2_total+= 35
        elif service2 == 2:
            service2_total += 19
        elif service2 == 3:
            service2_total += 7
        elif service2 == 4:
            service2_total += 12
        return service2_total

    def submit(self):
        '''
        Method to display totals when user hits submit
        :return: Totals
        '''
        try:
            overall_total = self.service1() + self.service2()
            option_1 = self.service1()
            option_2 = self.service2()
            self.text_output.setText(f'Service 1 Total: ${option_1}\n'
                             f'Service 2 Total: ${option_2}\n'
                             f'Bill Total: ${overall_total}')
        except ValueError:
            self.text_output.setText(f'Please enter the numerical value for service. E.g. If you would like an oil'
                                     f'change enter 1')

    def clear(self):
        '''
        Method to clear display so new information can be entered and submitted ahain.
        '''
        self.input_service1.setText('')
        self.input_service2.setText('')
        self.text_output.setText('')


