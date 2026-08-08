from counter import Counter
from counter_man import CounterMan

counter_man = CounterMan("Hillary", False)
counter_man.greet()

while counter_man.end != True:
    counter_man.help()


