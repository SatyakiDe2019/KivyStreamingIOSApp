# Real-time I-OS App displaying streaming data using Matplotlib & Python

## About this app

This app consuming streaming data from Ably channels & captured IoT events from the simulator & publish them inside a Dashboard of Kivy-build Python-app through measured KPIs.


## How to run this app

(The following instructions apply to Posix/bash. Windows users should check
[here](https://docs.python.org/3/library/venv.html).)

First, clone this repository and open a terminal inside the root folder.

Create and activate a new virtual environment (recommended) by running
the following:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Run the dummy event generation IoT-App:

```bash
python IoTDataGen.py
```

Run the Kivy-driven App:

```bash
python main.py
```

On a separate tab run this command:

```bash
source venv/bin/activate
```

## Screenshots

![demo.GIF](demo.GIF)

## Resources

- To learn more about Kivy, check out our [documentation](https://kivy.org/doc/stable/).
- To learn more about Matplotlib, check out our [documentation](https://matplotlib.org/stable/contents.html).
- To learn more about Ably, check out our [documentation](https://ably.com/case-studies).
