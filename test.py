from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QComboBox, QListWidget, QListWidgetItem, QMessageBox,
    QFileDialog, QCheckBox, QInputDialog
)
import sys
import json

class HotkeyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hotkey 功能設定工具")
        self.resize(600, 400)

        self.hotkey_list = []

        self.init_ui()

    def init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout()
        central.setLayout(layout)

        # 輸入區
        input_layout = QHBoxLayout()
        self.hotkey_input = QLineEdit()
        self.action_combo = QComboBox()
        self.action_combo.addItems(["文字輸入", "開啟檔案"])

        self.action_content_btn = QPushButton("設定內容")
        self.action_content_btn.clicked.connect(self.set_action_detail)

        self.add_button = QPushButton("加入")
        self.add_button.clicked.connect(self.add_hotkey)

        input_layout.addWidget(self.hotkey_input)
        input_layout.addWidget(self.action_combo)
        input_layout.addWidget(self.action_content_btn)
        input_layout.addWidget(self.add_button)

        layout.addLayout(input_layout)

        # 清單區
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        # 控制區
        control_layout = QHBoxLayout()
        self.enable_check = QCheckBox("啟用監聽")
        self.save_btn = QPushButton("儲存設定")
        self.load_btn = QPushButton("載入設定")
        self.exit_btn = QPushButton("結束程式")

        self.save_btn.clicked.connect(self.save_config)
        self.load_btn.clicked.connect(self.load_config)
        self.exit_btn.clicked.connect(self.close)

        control_layout.addWidget(self.enable_check)
        control_layout.addWidget(self.save_btn)
        control_layout.addWidget(self.load_btn)
        control_layout.addWidget(self.exit_btn)

        layout.addLayout(control_layout)

        self.current_action_detail = ""

    def set_action_detail(self):
        action = self.action_combo.currentText()
        if action == "文字輸入":
            text, ok = QInputDialog.getText(self, "輸入文字", "請輸入要輸出的文字：")
            if ok:
                self.current_action_detail = text
        elif action == "開啟檔案":
            file, _ = QFileDialog.getOpenFileName(self, "選擇檔案")
            if file:
                self.current_action_detail = file

    def add_hotkey(self):
        key = self.hotkey_input.text()
        action = self.action_combo.currentText()
        detail = self.current_action_detail

        if not key or not detail:
            QMessageBox.warning(self, "錯誤", "請完整輸入 Hotkey 與功能內容")
            return

        item = f"{key} → {action}: {detail}"
        self.list_widget.addItem(item)

        self.hotkey_list.append({
            "hotkey": key,
            "action": action,
            "detail": detail
        })

        # reset
        self.hotkey_input.clear()
        self.current_action_detail = ""

    def save_config(self):
        path, _ = QFileDialog.getSaveFileName(self, "儲存設定", filter="JSON Files (*.json)")
        if path:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(self.hotkey_list, f, indent=2, ensure_ascii=False)

    def load_config(self):
        path, _ = QFileDialog.getOpenFileName(self, "載入設定", filter="JSON Files (*.json)")
        if path:
            with open(path, "r", encoding="utf-8") as f:
                self.hotkey_list = json.load(f)

            self.list_widget.clear()
            for entry in self.hotkey_list:
                item = f"{entry['hotkey']} → {entry['action']}: {entry['detail']}"
                self.list_widget.addItem(item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = HotkeyApp()
    win.show()
    sys.exit(app.exec())
