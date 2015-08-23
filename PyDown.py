from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import  urllib.request
class Downloader(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout=QVBoxLayout()
        self.url= QLineEdit()
        self.savelocation=QLineEdit()
        self.progress=QProgressBar()
        download=QPushButton("Download")
        saveas=QPushButton("Browse")

        self.url.setPlaceholderText("URL")
        self.savelocation.setPlaceholderText("File save location")

        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.url)
        layout.addWidget(self.savelocation)
        layout.addWidget(saveas)
        layout.addWidget(self.progress)
        layout.addWidget(download)

        self.setLayout(layout)
        self.setWindowTitle("Python Downloader")
        self.setFocus()

        download.clicked.connect(self.download)
        saveas.clicked.connect(self.save_as)

    def save_as(self):
        save_file=QFileDialog.getSaveFileName(self, caption="Save as", directory=".", filter="All Files (*.*)")
        self.savelocation.setText(QDir.toNativeSeparators(save_file))

    def download(self):
        url = self.url.text()
        savelocation = self.savelocation.text()
        try :
             urllib.request.urlretrieve(url,savelocation,self.report)
        except Exception:
            QMessageBox.warning(self, "Warning", "Download Failed")
            return
        QMessageBox.information(self, "Information" , "The File has been Downloaded")
        self.url.setText("")
        self.progress.setValue(0)
        self.savelocation.setText("")

    def report(self,blocknum, blocksize , totalsize):
        readsofar = blocknum*blocksize
        if totalsize > 0 :
            percent=readsofar*100/totalsize
            self.progress.setValue(int(percent))


app = QApplication(sys.argv)
dl=Downloader()
dl.show()
app.exec_()