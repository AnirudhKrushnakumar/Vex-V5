#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

# Brain should be defined by default
brain=Brain()

# Robot configuration code
left_drive_smart = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_drive_smart = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.19, 295, 40, MM, 1)
claw_motor = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
arm_motor = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

# ----------------------------------------------------------------------------
#                                                                            
#    Project:        
#    Description:    
#    Configuration:  V5 Clawbot or Advanced TrainingBot (Drivetrain 2-motor, No Gyro)
#                    Claw Motor in Port 3
#                    Arm Motor in Port 8          
#                                                                            
# ----------------------------------------------------------------------------

# Library imports
from vex import *

def open_claw():
    claw_motor.spin(REVERSE)
    wait(2, SECONDS)
    claw_motor.stop()

def close_claw():
    claw_motor.spin(FORWARD)

def raise_arm_max():
    arm_motor.spin_for(FORWARD, 600, DEGREES)

def lower_arm_max():
    arm_motor.spin_for(REVERSE, 600, DEGREES)

def raise_arm(amount):
    arm_motor.spin_for(FORWARD, amount, DEGREES)

def lower_arm(amount):
    arm_motor.spin_for(REVERSE, amount, DEGREES)

# Begin project code

# Checkpoint 4.1
# claw_motor.set_velocity(15, PERCENT)
# arm_motor.set_velocity(30,PERCENT)
# raise_arm(230)
# open_claw()
# drivetrain.drive_for(FORWARD, 43, INCHES)
# wait(0.75, SECONDS)
# drivetrain.turn_for(LEFT, 90, DEGREES)
# wait(1,SECONDS)
# drivetrain.set_drive_velocity(15, PERCENT)
# drivetrain.drive_for(FORWARD, 3.55, INCHES)
# wait(0.5, SECONDS)
# drivetrain.drive_for(FORWARD, 2,INCHES)
# close_claw()
# wait(0.75,SECONDS)
# drivetrain.drive_for(REVERSE, 3.05, INCHES)
# drivetrain.turn_for(RIGHT, 90, DEGREES)
# wait(1,SECONDS)
# drivetrain.set_drive_velocity(15, PERCENT)
# drivetrain.drive_for(FORWARD, 52, INCHES)
# drivetrain.turn_for(LEFT, 90,DEGREES)
# raise_arm(200)
# wait(1,SECONDS)
# drivetrain.set_drive_velocity(15,PERCENT)
# drivetrain.drive_for(FORWARD, 65, INCHES)
# lower_arm(100)
# open_claw()
# wait(1,SECONDS)
# raise_arm(100)
# drivetrain.drive_for(REVERSE, 66, INCHES)
# drivetrain.turn_for(LEFT, 90,DEGREES)
# drivetrain.drive_for(FORWARD, 47, INCHES)
# drivetrain.turn_for(RIGHT, 90, DEGREES)
# lower_arm(200)
# drivetrain.set_drive_velocity(15)
# drivetrain.drive_for(FORWARD, 4, INCHES)
# close_claw()

# Checkpoint 4.2:
drivetrain.drive_for(FORWARD, 44, INCHES)
raise_arm(230)
drivetrain.turn_for(LEFT, 95, DEGREES)
drivetrain.drive_for(FORWARD, 6.5, INCHES)
drivetrain.turn_for(RIGHT, 95, DEGREES)
drivetrain.drive_for(FORWARD, 13, INCHES)
open_claw()
drivetrain.turn_for(RIGHT, 95, DEGREES)
drivetrain.drive_for(FORWARD, 5.5, INCHES)
close_claw()
wait(0.5,SECONDS)
drivetrain.drive_for(REVERSE, 5.5, INCHES)
drivetrain.turn_for(LEFT, 90, DEGREES)
drivetrain.drive_for(FORWARD, 36, INCHES)
drivetrain.turn_for(LEFT, 85, DEGREES)
raise_arm(70)
wait(1,SECONDS)
drivetrain.set_drive_velocity(100,PERCENT)
drivetrain.drive_for(FORWARD, 86, INCHES)
wait(1,SECONDS)
drivetrain.set_drive_velocity(50,PERCENT)
drivetrain.turn_for(LEFT, 95, DEGREES)
drivetrain.drive_for(FORWARD, 24, INCHES)
drivetrain.turn_for(RIGHT, 95, DEGREES)
open_claw()
drivetrain.drive_for(REVERSE, 92, INCHES)
drivetrain.set_drive_velocity(50,PERCENT)
drivetrain.turn_for(LEFT, 95, DEGREES)
drivetrain.drive_for(FORWARD, 31.5, INCHES)
drivetrain.turn_for(LEFT, 95, DEGREES)
lower_arm(70)
close_claw()
