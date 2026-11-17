# Phone Remote App 📱💻

This project is a local hosted app that will use phone as a remote to activate different presets for a monitor and tv setup (see presets below). This is a personal and learning project. I will use AI to plan in the beginning and help me with concepts, but not to write code.

---

## How it will work

```text
Smartphone in browser --> Home Server --> Windows PC --> System Actions (Displays, Audio, Apps)
```

---

## 🛠️ Tech Stack

* **Home server:** Python 3.10+, FastAPI, Uvicorn
* **PC Executor:** Python 3.10+, Native Windows APIs, `subprocess`, `pycaw`
* **Phone Interface:** HTML5, CSS3 (Dark Minimalist), Vanilla JavaScript (Fetch API)
* **IDE & Dev Tools:** VS Code, Git/GitHub, Python Virtual Environments (`venv`)

---

## 📁 Repository Structure (ai draft to help me subject to change)

```text
phone-remote-app/
├── README.md
├── .gitignore
├── server/                    # Home Server Coordinator (FastAPI)
│   ├── app/
│   │   ├── main.py
│   │   ├── config_loader.py
│   │   ├── routes/
│   │   │   └── api.py
│   │   └── services/
│   │       └── pc_client.py
│   ├── static/                # Mobile Web UI
│   │   ├── index.html
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── app.js
│   └── requirements.txt
│
└── pc_agent/                  # Windows PC Agent (Executor)
    ├── agent/
    │   ├── service_listener.py
    │   ├── dispatcher.py
    │   └── os_controller.py
    ├── config.json
    └── requirements.txt
```

---

## 🚀 Key Profiles & Features

### Base Features
* **Cinema Mode:** Sleep/disable primary monitor, switch audio output to TV/sound system, launch media center/streaming apps.
* **Game Mode:** Focus display output exclusively to TV screen, switch audio routing, launch Steam in Big Picture Mode.
* **Desktop / Work Mode:** Re-enable dual monitors, set standard desktop resolution, route audio back to desktop speakers/headphones.

### Planned additions I want to add
* Custom multi-step automation macro builder
* Direct media playback & volume control widgets
* Wake-on-LAN (WoL) system boot functionality
* Live PC resource usage monitoring dashboard (CPU/GPU/RAM)
* Smart home ambient light integration

---
