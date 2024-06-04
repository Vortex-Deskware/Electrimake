import os

def create_electron_app(url):
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
  "description": "Your app description goes here",
  "author": "Your Name",
  "devDependencies": {{
    "electron": "^16.0.0"
  }}
}}
        ''')

    # Create main.js file
    with open("main.js", "w") as main_file:
        main_file.write('''
const { app, BrowserWindow } = require('electron');

function createWindow() {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true
    }
  });

  win.loadURL("''' + url + '''");
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});
        ''')

    # Install Electron
    os.system("npm install --save-dev electron")

    print("Electron app created successfully!")
    print("Run 'npm start' to launch the Electron app.")
    print("Run 'npm run dist' to build the Electron app.")

def build_executable():
    os.system("npm run dist")

if __name__ == "__main__":
    url = input("Enter the URL for your Electron app: ")
    create_electron_app(url)
    build_executable()
