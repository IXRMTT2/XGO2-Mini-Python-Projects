# xgoedu Library

# Initialization:
XGOEDU(): Initializes the XGOEDU module.

# Methods (AI Vision):
XGO_edu.face_detect(): Detects a face using the XGOEDU module.

XGO_edu.yoloFast(): Yolo recognition

XGO_edu.gestureRecognition(): The Gesture recognition

XGO_edu.emotion(): Emotion recognition

XGO_edu.agesex(): Age recognition

XGO_edu.QRRecognition(): QR recognition

XGO_edu.CircleRecognition(): Ball recognition

XGO_edu.ColorRecognition("R"): Color recognition (R = red, B = blue, G = green, Y = yellow)

XGO_edu.SpeechSynthesis("hello"): Makes the robot speak

XGO_edu.SpeechRecognition(): Speech recognition

# Methods (Media):

XGO_edu.xgoCamera(True): Turns the camera on

XGO_edu.xgoCamera(False): Turns off the camera

XGO_edu.xgoTakePhoto("photo"): Captures a photo and saves it as "photo"

XGO_edu.xgoVideo(".mp4"): Plays a .mp4 video from the directory

XGO_edu.xgoVideoRecord("record",seconds=5): Records for 5 seconds and saves it as "record"

XGO_edu.xgoSpeaker("agitated.wav"): Plays an audio through the speaker

XGO_edu.xgoSpeaker(".wav"): Plays an audio file from directory

XGO_edu.xgoAudioRecord("record",seconds=5): Records any audio and saves it as "record"

# Buttons

XGO_edu.xgoButton("a"): Button A was pressed

XGO_edu.xgoButton("b"): Button b was pressed

# Screen (LCD Screen)

XGO_edu.lcd_arc(,,,,0,100,color=(255,255,255),width=2): Draw an arc 0,0,0, with angel 1 being 100 and color being 255 (rgb)

XGO_edu.lcd_circle(,,,color=(255,255,255),width=2): Draw a circle 0,0,0, with radius 0 being 100 and color being 255 (rgb) and width being 0

XGO_edu.lcd_rectangle(,,,,fill=None,outline=(255,255,255),width=2): Draw a rectangle 0,0,0, with the outline color of 255,255,255 and a width of 2

XGO_edu.lcd_line(,,,,color=(255,255,255),width=2): Draw a line 0,0,0 with color of 255,255,255, and a width of 2.

XGO_edu.lcd_picture("agitated.jpg"): displays the agitated jpg (change out with whatever facial thing you want)

XGO_edu.lcd_picture(".jpg"): Shows an image on the LCD screen

XGO_edu.lcd_text(,,,color=(255,255,255),fontsize=15): Shows LCD text

str(): string

XGO_edu.lcd_clear(): Clears the LCD screen































