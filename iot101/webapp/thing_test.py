import thing
import time

pi_thing = thing.PiThing() #nesne olusuturuldu.
switch = pi_thing.read_switch()
print('Switch Durumu >> {0}'.format(switch))

print('Led yanip sonecek cikis icin ctrl + C tusuna basiniz!')
while True:
    pi_thing.set_led(True)
    time.sleep(0.5)
    pi_thing.set_led(False)
    time.sleep(0.5)
