# Electrimake

---
Electrimake allows you to easily build native desktop apps with 1 script!

# Usage
Dependencies: Node.js, NPM, & Python.

- ```npm install -g electron electron-builder```

- ```python Electrimake.py```

  then go into the ```dist``` folder

  finally, open ```electron-url-app Setup 1.0.0.exe```

  ---
  # Configuration

  Edit

  ```
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
```
