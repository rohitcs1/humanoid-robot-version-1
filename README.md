# 🤖 Humanoid Robot Version 1

An AI-powered humanoid robot built using **Raspberry Pi 4**, **Pi Camera**, and Python.

This project is being developed in modules so that every feature can be tested independently and expanded in future versions.

---

# 🚀 Current Features

- ✅ Camera Setup
- ✅ Face Detection

---

# 📅 Upcoming Features

- ⏳ Face Tracking (Servo)
- ⏳ Face Recognition
- ⏳ Emotion Detection
- ⏳ Display Facial Expressions
- ⏳ Human Detection
- ⏳ Object Detection
- ⏳ AI Assistant
- ⏳ Voice Assistant
- ⏳ Autonomous Navigation

---

# 🛠 Hardware

- Raspberry Pi 4
- Raspberry Pi Camera Module
- Servo Motor
- LCD Display (Future)
- Motor Driver
- DC Gear Motors
- Ultrasonic Sensors
- IR Sensors
- PIR Sensor
- Relay Module
- GSM Module
- Li-ion Battery

---

# 📁 Project Structure

```text
humanoid-robot-version-1/
│
├── README.md
├── requirements.txt
├── setup.sh
│
├── models/
│   └── haarcascade_frontalface_default.xml
│
└── src/
    ├── main.py
    ├── camera.py
    └── face_detection.py
```

---

# 📥 Installation

Clone the repository

```bash
git clone git@github.com:rohitcs1/humanoid-robot-version-1.git
```

Go to the project folder

```bash
cd humanoid-robot-version-1
```

Give setup script permission

```bash
chmod +x setup.sh
```

Run setup

```bash
./setup.sh
```

---

# ▶️ Run Project

If your `main.py` is inside the **src** folder:

```bash
python3 src/main.py
```

If your `main.py` is in the project root:

```bash
python3 main.py
```

Press **Q** to exit.

---

# 🗺 Development Roadmap

## Phase 1 - Vision
- [x] Camera Setup
- [x] Face Detection
- [ ] Face Tracking

## Phase 2 - AI Vision
- [ ] Face Recognition
- [ ] Emotion Detection
- [ ] Human Detection
- [ ] Object Detection

## Phase 3 - Robot Face
- [ ] LCD Face Animation
- [ ] Eye Blink Animation
- [ ] Mouth Animation

## Phase 4 - Motion
- [ ] Servo Head Movement
- [ ] Autonomous Navigation
- [ ] Obstacle Avoidance

## Phase 5 - AI
- [ ] AI Chat Assistant
- [ ] Voice Assistant
- [ ] Memory System

---

# 👨‍💻 Author

**Rohit Kumar**

GitHub: https://github.com/rohitcs1

---

# 📜 License

This project is open-source and released under the MIT License.
