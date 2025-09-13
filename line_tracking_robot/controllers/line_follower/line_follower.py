from controller import Robot


def run_robot(robot):
    
        time_step = 32
        max_speed = 6.28 
        

        #motors
        left_motor = robot.getDevice("left wheel motor")
        right_motor = robot.getDevice("right wheel motor")
        left_motor.setPosition(float("inf"))
        right_motor.setPosition(float("inf"))
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(0.0)
        
        
        #Enable ir sensor
        left_ir = robot.getDevice("ir0")
        left_ir.enable(time_step)
        
        right_ir = robot.getDevice("ir1")
        right_ir.enable(time_step)
        
        
        #step simulation
        while robot.step(time_step) != -1:
            
            #read ir sensor
            left_ir_value = left_ir.getValue()
            right_ir_value = right_ir.getValue()
            
            
            print("left: {} right: {} ".format(left_ir_value,right_ir_value))
            
          
            
            if left_ir_value < 2.5 or right_ir_value<2.5:
                print("devam et")
                

                if left_ir_value < right_ir_value:
                    print("yavas sola don")
                    right_speed = max_speed/8
                    left_speed = max_speed/16

    
                if left_ir_value > right_ir_value:
                    print("yavas saga don")
                    right_speed = right_speed/16
                    left_speed = left_speed/8

            
            elif left_ir_value < right_ir_value:
                print("sola don")
                right_speed = max_speed/2
                left_speed = max_speed/4
 
    
            elif left_ir_value > right_ir_value:
                print("saga don")
                right_speed = max_speed/4
                left_speed = max_speed/2
          

                
                
            left_motor.setVelocity(left_speed)
            right_motor.setVelocity(right_speed)
        
            
            
if __name__ == "__main__":
        my_robot = Robot()
        run_robot(my_robot) 