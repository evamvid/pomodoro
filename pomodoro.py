import time
import sys
import datetime
import winsound

def ring(sound):
    winsound.PlaySound('%s.wav' % sound, winsound.SND_FILENAME)

times = 0

while True:
    tomato = 0
    while tomato <= 1500:
        timeLeft = 1500 - tomato
        formatted = str(datetime.timedelta(seconds=timeLeft))
        sys.stdout.write('\r'+ formatted)
        time.sleep( 1 )
        tomato += 1
    ring("MetalGong")

    times += 1
    print()
    print("You have completed {} Pomodoros.".format(times))

    fun = 0
    while fun <= 300:
        funTimeleft = 300 - fun
        funFormatted = str(datetime.timedelta(seconds=funTimeleft))
        sys.stdout.write('\r'+ funFormatted)
        time.sleep( 1 )
        fun +=1
    ring("AirHorn")
