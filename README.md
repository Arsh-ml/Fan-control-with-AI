# Fan-control-with-AI
Control your fan based on the fact if someone is present in a room or not. If someone is present, the fan goes on and vice versa.

### CONNECTIONS FOR ARDUINO ###
1) VIN of Arduino -> 5V of Relay.
2) GND of Arduino -> GND of Relay.
3) Pin 8 of Arduin0 -> IN4 of Relay (or any other input according to your relay module channels, mine was at channel 4).

***NOTE: THIS WILL ONLY TURN THE RELAY ON AND OFF BASED ON THE DETECTION OF FACE. FOR SAFETY PURPOSE I AM NOT TELLING HOW TO CONNECT RELAY TO LIVE WIRES IF YOU WANT TO DO CHECK OUT SOME ONLINE ARTICLES/VIDEOS***

### HOW TO RUN ###
1) Firstly make the connections and upload 'fan_control.ino' to arduino
2) Run the 'fan_control_detection.py' (Dependencies can be found below...)
3) Press 'q' to exit the program in python.

### PYTHON FILE REQUIREMENTS ###
python version: 3.6.6
opencv-python==4.5.3.56

Rest can be found in the requirements.txt file and can be installed via:   pip install -r requirements.txt
(make sure to run the pip command in the same folder where the file is stored)
