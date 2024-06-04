import os
import tkinter as tk
from tkinter import ttk, messagebox

class ElectronAppCreator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Electrimake GUI")
        self.geometry("400x350")
        self.configure(bg="#1E1E1E")
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TLabel", foreground="#FFFFFF", background="#1E1E1E", font=("Segoe UI", 10))
        self.style.configure("TEntry", foreground="#000000", background="#333333", font=("Segoe UI", 10))
        self.style.map("TButton", background=[("active", "#005f9b")])

        self.url_label = ttk.Label(self, text="URL:")
        self.url_label.grid(row=0, column=0, padx=20, pady=(30, 5), sticky="w")

        self.url_entry = ttk.Entry(self)
        self.url_entry.grid(row=0, column=1, padx=10, pady=(30, 5), sticky="we")

        self.title_label = ttk.Label(self, text="App Title:")
        self.title_label.grid(row=1, column=0, padx=20, pady=5, sticky="w")

        self.title_entry = ttk.Entry(self)
        self.title_entry.grid(row=1, column=1, padx=10, pady=5, sticky="we")

        self.description_label = ttk.Label(self, text="Description:")
        self.description_label.grid(row=2, column=0, padx=20, pady=5, sticky="nw")

        self.description_entry = tk.Text(self, width=30, height=5, bg="#333333", fg="#FFFFFF", font=("Segoe UI", 10))
        self.description_entry.grid(row=2, column=1, padx=10, pady=5, sticky="we")

        self.icon_label = ttk.Label(self, text="Icon Path (optional):")
        self.icon_label.grid(row=3, column=0, padx=20, pady=5, sticky="w")

        self.icon_entry = ttk.Entry(self)
        self.icon_entry.grid(row=3, column=1, padx=10, pady=5, sticky="we")

        self.create_button = ttk.Button(self, text="Create Electron App", command=self.create_electron_app)
        self.create_button.grid(row=4, column=0, columnspan=2, padx=20, pady=20, sticky="we")

        self.build_button = ttk.Button(self, text="Build Executable", command=self.build_executable)
        self.build_button.grid(row=5, column=0, columnspan=2, padx=20, pady=5, sticky="we")

    def create_electron_app(self):
        url = self.url_entry.get()
        title = self.title_entry.get()
        description = self.description_entry.get("1.0", "end-1c")
        icon_path = self.icon_entry.get()

        if url and title:
            try:
                # Create a directory for the Electron app
                os.makedirs("electron_app")
                os.chdir("electron_app")

                # Create package.json file
                with open("package.json", "w") as package_file:
                    package_file.write(f'''
{{
  "name": "electron-url-app",
  "version": "1.0.0",
  "main": "main.js",
  "scripts": {{
    "start": "electron .",
    "pack": "electron-builder --dir",
    "dist": "electron-builder"
  }},
  "description": "{description}",
  "author": "Your Name",
  "build": {{
    "productName": "{title}",
    "appId": "com.example.electronapp",
    "directories": {{
      "output": "dist"
    }},
    "win": {{
      "icon": "{icon_path if icon_path else ''}"
    }}
  }},
  "devDependencies": {{
    "electron": "^16.0.0"
  }}
}}
                    ''')

                # Create main.js file
                with open("main.js", "w") as main_file:
                    main_file.write(f'''
const {{ app, BrowserWindow }} = require('electron');

function createWindow() {{
  const win = new BrowserWindow({{
    width: 800,
    height: 600,
    webPreferences: {{
      nodeIntegration: true
    }}
  }});

  win.loadURL("{url}");
}}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {{
  if (process.platform !== 'darwin') {{
    app.quit();
  }}
}});

app.on('activate', () => {{
  if (BrowserWindow.getAllWindows().length === 0) {{
    createWindow();
  }}
}});
                    ''')

                # Install Electron
                os.system("npm install --save-dev electron")

                messagebox.showinfo("Success", "Electron app created successfully!\nRun 'npm start' to launch the Electron app.\nRun 'npm run dist' to build the Electron app.")

            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please enter a valid URL and app title.")

    def build_executable(self):
        try:
            os.system("npm run dist")
            messagebox.showinfo("Success", "Executable built successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = ElectronAppCreator()
    app.mainloop()
