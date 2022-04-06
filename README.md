# Fan-control-with-AI
Control your fan based on the fact if someone is present in a room or not. If someone is present, the fan goes on and vice versa.

### CONNECTIONS FOR ARDUINO ###
VIN of Arduino -> 5V of Relay
GND of Arduino -> GND of Relay
Pin 8 of Arduin0 -> IN4 of Relay (or any other input according to your relay module channels, mine was at channel 4).

### HOW TO RUN ###
1) Firstly make the connections and upload 'fan_control.ino' to arduino
2) Run the 'fan_control_detection.py' (Dependencies can be found below...

### PYTHON FILE REQUIREMENTS ###
python version: 3.6.6
opencv-python==4.5.3.56

Rest can be found in the requirements.txt file and can be installed via:   pip install -r requirements.txt
(make sure to run the pip command in the same folder where the file is stored)
