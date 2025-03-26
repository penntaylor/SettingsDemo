# This Python file uses the following encoding: utf-8


# README:
# This sample application demonstrates how to use QSettings to save and restore the UI
# state of a Qt Application.


import sys
from time import sleep
import concurrent.futures

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QSettings, QSize, QPoint

from PyQt5.QtCore import pyqtRemoveInputHook, pyqtRestoreInputHook

# Here's how to insert a temporary pdb trace line that turns off Qt's event loop while the debugger is active:
# pyqtRemoveInputHook(); import pdb;  pdb.set_trace(); pyqtRestoreInputHook()

# Important:
# If you change anything in the .ui file,
# you need to run the following command to generate the ui_form.py file
#     pyuic5 form.ui -o ui_form.py
from ui_form import Ui_SettingsDemoWindow


# Utility function to deal with booleans-as-strings in QSettings
def _strBool(s):
    if "false" in s.lower():
        return False
    else:
        return True


class SettingsDemoWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SettingsDemoWindow()
        self.ui.setupUi(self)

        # Read settings from the ini file
        self.readSettings()


    # Qt calls this when SettingsDemoWindow is closed.
    # We use this event as an opportunity to automatically write out
    # the current window settings. You don't have to do this kind of automatic saving, of course.
    # This could instead be attached to a menu option or a button or something.
    def closeEvent(self, event):
        self.writeSettings()
        event.accept()


    def writeSettings(self):
        """Write all saveable settings to a .ini file.
        Dumps out the location of the ini file to stdout after writing.
        """
        settings = QSettings(QSettings.IniFormat, QSettings.UserScope, "MyCompany", "SettingsDemo")
        settings.setValue("MainWindow/size", self.size())
        settings.setValue("MainWindow/pos", self.pos())

        ui = self.ui

        # Data Checkboxes
        settings.setValue("Data/A", ui.checkBox_A.isChecked())
        settings.setValue("Data/B", ui.checkBox_B.isChecked())
        settings.setValue("Data/C", ui.checkBox_C.isChecked())
        settings.setValue("Data/D", ui.checkBox_D.isChecked())
        settings.setValue("Data/E", ui.checkBox_E.isChecked())

        # RMSE radio group
        settings.setValue("RMSE/n", ui.radioButton_nrmse.isChecked())
        settings.setValue("RMSE/rw", ui.radioButton_rwnrmse.isChecked())
        settings.setValue("RMSE/rank", ui.radioButton_ranknrmse.isChecked())

        # veryImportantNumber
        settings.setValue("Spinner/veryImportantNumber", ui.spinBox_veryImportantNumber.value())

        # Those two unlabeled toolbuttons
        settings.setValue("Tools/paintbrush", ui.toolButton_paintbrush.isChecked())
        settings.setValue("Tools/eraser", ui.toolButton_eraser.isChecked())

        print(f"Saved settings to {QSettings.fileName(settings)}")



    def readSettings(self):
        """Read in the .ini settings file and restore everything to the previously-saved state
        """
        settings = QSettings(QSettings.IniFormat, QSettings.UserScope, "MyCompany", "SettingsDemo")
        self.resize(QSize(settings.value("MainWindow/size", QSize(400, 400))))
        self.move(QPoint(settings.value("MainWindow/pos", QPoint(200, 200))))

        ui = self.ui

        # Restore Data checkboxes
        ui.checkBox_A.setChecked(_strBool(settings.value("Data/A", "false")))
        ui.checkBox_B.setChecked(_strBool(settings.value("Data/B", "false")))
        ui.checkBox_C.setChecked(_strBool(settings.value("Data/C", "false")))
        ui.checkBox_D.setChecked(_strBool(settings.value("Data/D", "false")))
        ui.checkBox_E.setChecked(_strBool(settings.value("Data/E", "false")))

        # Restore RMSE radio group
        ui.radioButton_nrmse.setChecked(_strBool(settings.value("RMSE/n", "false")))
        ui.radioButton_rwnrmse.setChecked(_strBool(settings.value("RMSE/rw", "false")))
        ui.radioButton_ranknrmse.setChecked(_strBool(settings.value("RMSE/rank", "false")))

        # Restore veryImportantNumber
        ui.spinBox_veryImportantNumber.setValue(int(settings.value("Spinner/veryImportantNumber", 0)))

        # Restore those two unlabeled toolbuttons
        ui.toolButton_paintbrush.setChecked(_strBool(settings.value("Tools/paintbrush", "false")))
        ui.toolButton_eraser.setChecked(_strBool(settings.value("Tools/eraser", "false")))



if __name__ == "__main__":
    try:
        app
    except:
        app = QApplication(sys.argv)
    widget = SettingsDemoWindow()
    widget.show()
    sys.exit(app.exec())
