import os
import shutil
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QPushButton


class ListboxWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.resize(600, 600)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
            global links
            links = []
            for url in event.mimeData().urls():
                if url.isLocalFile():
                    links.append(str(url.toLocalFile()))
                else:
                    links.append(str(url.tostring()))
            self.addItems(links)
        else:
            event.ignore()

    def removeItem(self, x):
        self.removeItem(x)

    def getSelecteditem(self):
        item = QListWidgetItem(self.lstbox_View.currentItem())
        return item.text()


class AppDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1200, 600)
        self.lstbox_View = ListboxWidget(self)
        '''
        self.btn = QPushButton(' Get Value ', self)
        self.btn.setGeometry(850, 400, 200, 50)
        self.btn.clicked.connect(lambda: print(self.getSelecteditem()))
        '''
        self.btn2 = QPushButton(' Organized ', self)
        # x-axis , y-axis , width , height
        self.btn2.setGeometry(850, 300, 200, 50)
        self.btn2.clicked.connect(lambda: self.sortbyext())

    def createFolder(self, folder):
        try:
            print(' Checking folder ')
            if not os.path.exists(folder):
                os.makedirs(folder)
                return True
        except OSError:
            print(f"Error while Creating Folder {folder}")
            return False

    def sortbyext(self):
        # os.chdir('C:\\Users\\Shreyas\\Desktop\\test')
        # if not os.path.exists(folder):
        # os.makedirs(folder)
        current_dir = os.getcwd()
        # print("CWD " + current_dir)
        for f_loc in links:
            filename, file_ext = os.path.splitext(f_loc)
            filename = os.path.basename(f_loc)
            print(f"filename : {filename} \n file Extension : {file_ext}")
            try:
                if not file_ext:
                    print(f"Directory Found ! Skiped ...")
                    pass

                # video
                elif file_ext in ('.mp4'):
                    folder = ".\Video File"
                    try:
                        print(' Checking folder exits ')
                        if not os.path.exists(folder):
                            os.makedirs(folder)
                            print(f"Creating folder {folder}")
                        shutil.move(
                            # source
                            f_loc,
                            # destination
                            os.path.join(current_dir, 'Video File', f'{filename}'))
                    except (FileNotFoundError, PermissionError, FileExistsError) as e:
                        print(e)

                # text
                elif file_ext in ('.txt'):
                    folder = ".\Text File"
                    try:
                        print(' Checking folder exits ')
                        if not os.path.exists(folder):
                            os.makedirs(folder)
                            print(f"Creating folder {folder}")
                        shutil.move(
                            # source
                            f_loc,
                            # destination
                            os.path.join(current_dir, 'Text File', f'{filename}'))
                    except (FileNotFoundError, PermissionError, FileExistsError) as e:
                        print(e)
                # music
                elif file_ext in ('.mp3', '.wav'):
                    folder = ".\Songs File"
                    try:
                        print(' Checking folder exits ')
                        if not os.path.exists(folder):
                            os.makedirs(folder)
                            print(f"Creating folder {folder}")
                        shutil.move(
                            # source
                            f_loc,
                            # destination
                            os.path.join(current_dir, 'Songs File', f'{filename}'))
                    except (FileNotFoundError, PermissionError, FileExistsError) as e:
                        print(e)

                else:
                    pass

            except Exception as e:
                print("Error : " + e)


app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec_())
