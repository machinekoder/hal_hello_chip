from machinekit import hal
from machinekit import rtapi as rt

# we need a thread to execute the component functions
rt.newthread('main-thread', 1000000, fp=True)

# load GPIO driver
rt.loadrt('hal_chip_gpio', output_pins='0,1,2,3', input_pins='4,5,6,7')
gpio = hal.Component('chip_gpio')
gpio.pin('out-00').link('square')

# load siggen
rt.loadrt('siggen')
siggen = hal.Component('siggen.0')
siggen.pin('frequency').set(10.0)
siggen.pin('clock').link('square')

# setup update functions
hal.addf('chip_gpio.read', 'main-thread')
hal.addf('siggen.0.update', 'main-thread')
hal.addf('chip_gpio.write', 'main-thread')

# ready to start the threads
hal.start_threads()

# start haltalk server after everything is initialized
# else binding the remote components on the UI might fail
#hal.loadusr('haltalk')

