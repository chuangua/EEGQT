# © MNELAB developers
#
# License: BSD (3-clause)

from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QGridLayout,
    QLabel,
    QLineEdit,
    QVBoxLayout,
)


class SampleDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Filter data")
        vbox = QVBoxLayout(self)
        grid = QGridLayout()
        grid.addWidget(QLabel("Resampling frequency (Hz):"), 0, 0)
        self.fs = QLineEdit()
        grid.addWidget(self.fs, 0, 1)

        vbox.addLayout(grid)
        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        vbox.addWidget(buttonbox)
        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)
        vbox.setSizeConstraint(QVBoxLayout.SetFixedSize)

    @property
    def sampling(self):
        fs = self.fs.text()
        return int(fs) if fs else None
