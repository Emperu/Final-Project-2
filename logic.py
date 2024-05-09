from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets
from PyQt5 import QtCore
import csv
import os

class Logic(object):
    def __init__(self, MainWindow):
        self.ui = MainWindow

    def submit(self):
        import csv
        import os

        try:
            student_name = self.ui.lineEdit_student_name.text()
            if not student_name:
                QMessageBox.critical(self.ui.centralwidget, "Invalid Input", "Student Name cannot be empty.")
                return

            attempts = int(self.ui.lineEdit_attempts.text())
            scores = []
            for i, lineEdit in enumerate(self.ui.scoreLineEdits):
                try:
                    score = int(lineEdit.text())
                    if not (0 <= score <= 100):
                        raise ValueError()
                    scores.append(score)
                except ValueError:
                    QMessageBox.critical(self.ui.centralwidget, "Invalid Input",
                                         "Scores should be numbers between 0 and 100.")
                    return

            best_score = max(scores)

            filename = 'students.csv'
            fieldnames = ['Name', 'Score 1', 'Score 2', 'Score 3', 'Score 4', 'Final Score']
            data = {'Name': student_name, 'Score 1': 0, 'Score 2': 0, 'Score 3': 0, 'Score 4': 0, }

            for i, score in enumerate(scores):
                data[f'Score {i + 1}'] = score
            data['Final Score'] = best_score

            with open(filename, 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                # check size to write headers: if the file is new, it will have size 0
                if os.path.getsize(filename) == 0:
                    writer.writeheader()
                # Write the row for the current student
                writer.writerow(data)

        except Exception as e:
            print(f"An error occurred: {e}")

        self.ui.submit_status_label.setText("Submitted")
        self.ui.submit_status_label.setStyleSheet("QLabel { color : green; }")
        self.ui.submit_status_label.show()

    def attemptCountChange(self):
        input_text = self.ui.lineEdit_attempts.text().strip()
        if input_text == "":
            if input_text == "":
                for lineEdit, label in zip(self.ui.scoreLineEdits, self.ui.scoreLabels):
                    lineEdit.deleteLater()
                    label.deleteLater()

                self.ui.scoreLineEdits.clear()
                self.ui.scoreLabels.clear()
                return
        try:
            count = int(self.ui.lineEdit_attempts.text())
        except ValueError:
            print('Invalid input')
            QMessageBox.critical(self.ui.centralwidget, "Invalid Input",
                                 "Invalid input! Please enter a number.")  # Add these lines
            return

        if not 1 <= count <= 4:
            print('Invalid input')
            QMessageBox.critical(self.ui.centralwidget, "Invalid Input",
                                 "Invalid input. Please enter a number between 1 and 4.")  # Add these lines
            return

        for lineEdit, label in zip(self.ui.scoreLineEdits, self.ui.scoreLabels):
            lineEdit.deleteLater()
            label.deleteLater()

        self.ui.scoreLineEdits.clear()
        self.ui.scoreLabels.clear()

        for i in range(count):
            label = QtWidgets.QLabel(self.ui.centralwidget)
            label.setGeometry(QtCore.QRect(10, 70 + i * 30, 111, 16))
            label.setText(f'Score {i + 1}:')
            label.show()

            lineEdit = QtWidgets.QLineEdit(self.ui.centralwidget)
            lineEdit.setGeometry(QtCore.QRect(110, 70 + i * 30, 113, 21))
            lineEdit.show()

            self.ui.scoreLineEdits.append(lineEdit)
            self.ui.scoreLabels.append(label)