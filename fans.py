import glob

MAX_PWM=255
MIN_PWM=100


def determine_target_pwm(t_target,cards):
        t_pwm=[]
        for card in cards:
                f = open(card+'temp1_input','r')
                t_current=f.readline()
                #print(t_current)
                f.close()

                f = open(card+'pwm1','r')
                pwm_current=int(f.readline())
                f.close()

                print (pwm_current)

                t_current=(float(t_current)/1000)

                print(t_current)
                temp_pwm=pwm_current

                if t_current < t_target*0.97:

                        temp_pwm=int(pwm_current*0.9)

                elif t_current > t_target*1.025:

                        temp_pwm=int(pwm_current*1.1)



                temp_pwm = MAX_PWM if temp_pwm>MAX_PWM else temp_pwm

                temp_pwm = MIN_PWM if temp_pwm<MIN_PWM else temp_pwm

                t_pwm.append(temp_pwm )

                print()

        return(t_pwm)

def change_pwm1(cards,target_pwm):
        
        for k,card in enumerate(cards):
                print (k)
		
                f = open(card+'pwm1','w+')
                f.write(str(target_pwm[k]))
                

if __name__=="__main__":

        paths='/sys/class/drm/card?/device/hwmon/hwmon?/'
        cards=glob.glob(paths)
        target_temp=65
        print (cards)
        target_pwm=determine_target_pwm(target_temp,cards)
        print(target_pwm)
        change_pwm1(cards,target_pwm)

