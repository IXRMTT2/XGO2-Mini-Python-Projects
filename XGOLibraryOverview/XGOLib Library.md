# xgolib Library

# Initialization:
XGO('xgomini'): Initializes the XGO Mini robot.

# Methods:
dog.action(action_id): Performs a specific action based on the action ID.

XGO_mini.gait_type("trot"): Makes the set gain trot

XGO_mini.gait_type("walk"): Makes the set gain walk

XGO_mini.gait_type("high_walk"): makes the set gain high walk

XGO_mini.motor_speed(255): Makes the servo speed fast

XGO_mini.motor_speed(128): Makes the server speed normal

XGO_mini.motor_speed(1): Makes the servo speed slow

XGO_mini.pace("high"): Makes the step frequency fast

XGO_mini.pace("normal"): Makes the step frequency normal

XGO_mini.pace("slow"): Makes the step frequency slow

XGO_mini.motor(13,0): Makes the left front leg at [-31,31] with a servo degree of 0 (The 0 can be changed to a different degree)

XGO_mini.motor(23,0): Makes the right front leg at [-31,31] with a servo degree of 0 (The 0 can be changed to a different degree)

XGO_mini.motor(33,0): Makes the right rear leg at [-31,31] with a servo degree of 0 (The 0 can be changed to a different degree)

XGO_mini.motor(43,0): Makes the left rear leg at [-31,31] with a servo degree of 0 (The 0 can be changed to a different degree)

XGO_mini.motor(51,0): Makes the arm (claw arm) go [-65,65], with a servo degree of 0 (The servo degree can be changed from 0 to a different degree)

XGO_mini.motor(52,0): Makes the arm (claw arm) go [-85,50], with a servo degree of 0 (The servo degree can be changed from 0 to a different degree)

XGO_mini.motor(53,0): Makes the arm (claw arm) go [-75,90], with a servo degree of 0 (The servo degree can be changed from 0 to a different degree)

XGO_mini.leg(1,[0,0,105]): Controls the left front foot

XGO_mini.leg(2,[0,0,105]): Controls right front foot

XGO_mini.leg(3,[0,0,105]): Controls right rear foot

XGO_mini.leg(4,[0,0,105]): Controls left rear foot

XGO_mini.arm(90,90): Sets the arm (claw arm) position X axis to 90 degrees, and the Z axis to 90 degrees (these degrees can be changed)

XGO_mini.arm_mode(0): Sets the arm reference farm as body

XGO_mini.arm_mode(1): Sets the arm reference farm as ground

XGO_mini.claw(128): Sets the claw grip to 128 (0~255)

XGO_mini.move_x(15): Sets Forward[0mm~25mm] translation motion with a stride of 15 step

time.sleep(0): Sets how long the robot should just stay in its position for (the 0 can be changed and its in seconds)

XGO_mini.read_motor(): Gets the current servo angle

XGO_mini.read_roll(): Get gyro X axis's angle

XGO_mini.read_pitch(): Get gyro Y axis's angle

XGO_mini.read_yaw(): Get gyro Z axis's angle

XGO_mini.read_battery(): Gets current power of the robot

XGO_mini.unload_allmotor(): Sets all servos to be unloaded (cut power)

XGO_mini.load_allmotor(): Sets all servos to be loaded (puts power back)

XGO_mini.perform(1): Turns on performance mode

XGO_mini.perform(0): Turns off performance mode

XGO_mini.imu(1): Turns on gyroscope

XGO_mini.imu(0): Turns off gyroscope

XGO_mini.periodic_rot("r",0): Stop body rotation along X axis

XGO_mini.periodic_rot("p",0): Stop body rotation along Y axis

XGO_mini.periodic_rot("y",0): Stop body rotation along Z axis

XGO_mini.periodic_rot("r",3): Set body cycle rotation per 3  (1.5~8)s along x axis

XGO_mini.periodic_rot("p",3): Sets the body cycle rotation per 3 (1.5~8)s along Y axis

XGO_mini.periodic_rot("y",3):  Sets the body cycle rotation per 3 (1.5~8)s along Z axis

XGO_mini.turn(-100): Makes the robot turn clockwise at 100 degrees 

XGO_mini.turn(100): Makes the robot turn counter clockwise at 100 degrees
