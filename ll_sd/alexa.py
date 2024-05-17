Give me OOD python code - // There are a wide variety of Alexa devices
// 1. Alexa devices that only have a speaker (Echo Dot, Echo Flex, https://www.amazon.com/dp/B07FZ8S74R)
// 2. Alexa devices that only have a screen/display (Alexa enabled Microwave or AC, https://www.amazon.com/dp/B07894S727)
// 3. Alexa devices that have both, speaker and screen (Echo Show, Echo Spot, https://www.amazon.com/dp/B08KJN3333).
// 4. Alexa devices that have neither a speaker, nor a screen (Echo Input, Echo link, https://www.amazon.com/dp/B0798DVZCY).
// 5. Alexa devices that have a speaker, but can be connected to a display (FireTV cube, https://www.amazon.com/dp/B08XMDNVX6).
//
// Also,
// 1. Some Alexa devices that have batteries (Fire Tablets, Echo Tap, Echo Buds, https://www.amazon.com/dp/B085WTYQ4X)
// 2. Others that do not have batteries (Echo Dot, Echo Show).
//
// Design a set of classes that will report the current battery/power status to the user.
// Depending on the hardware, the response may need to be spoken, or displayed on a screen, or both.
// Also, depending on whether there is a battery or not, the status message will differ.
// For example, if the device is a Tablet which has a battery, a speaker, and a display, and currently
// it happens to be plugged in and recharging (let's say at 75%), then your code should return the following:
//      {
//          "say": "Current battery level is 75% and charging",
//          "display": "Current battery level is 75% and charging"
//      }
//
// Whereas if the device is an Echo Dot, which has a speaker but no battery and no screen,
// then your code should only return:
//      {
//          "say": "Currently plugged into wall power"
//      }
//
// and should NOT attempt to display anything (since there is no screen).
//
// For simplicity, ignore the details of speech generation and image/visual card generation, we can safely assume those are provided.
// Focus more on modeling the Alexa devices and their properties, and returning the correct responses.

from enum import Enum
from abc import abstractmethod

class DeviceType(Enum):
    ECHO_SHOW = 1
    ECHO_DOT = 2

class InputType(Enum):
    TYPE = 1
    VOICE = 2
    TOUCH = 3

class OutputType(Enum):
    DISPLAY = 'display'
    SOUND = 'say'

class BatteryStatus(Enum):
    PLUGGEDIN = 1
    ONBATTERY = 2

class Input:
    def __init__(self, input_type):
        self.input_type = input_type

    def get_input_type(self):
        return self.input_type

class Output:
    def __init__(self, output_type):
        self.output_type = output_type

    def get_output_type(self):
        return self.output_type

class Battery:
    def __init__(self, battery_type, status, value):
        self.battery_type = battery_type
        self.status = status
        self.value = value

    def get_battery_type(self):
        return self.battery_type

    def get_status(self):
        return self.status

    def get_value(self):
        return self.value

    def update_status(self, status):
        self.status = status

    def update_value(self, value):
        self.value = value

class Device:
    def __init__(self, input_type, output_type):
        self.input_type = input_type
        self.output_type = output_type

    def get_input_type(self):
        return self.input_type

    def get_output_type(self):
        return self.output_type

    @abstractmethod
    def get_power_status(self):
        pass

class EchoShow(Device):
    def __init__(self, input_type, output_type, battery):
        super().__init__(input_type=input_type, output_type=output_type)
        self.battery = battery

    def get_power_status(self):
        final_val = {}
        for op in self.output_type:
            curr_str = f"You have a battery of {self.battery.get_value()}%"
            if self.battery.get_status() == BatteryStatus.PLUGGEDIN:
                curr_str += " and charging"
            final_val[op] = curr_str
        return final_val

class EchoDot(Device):
    def __init__(self, input_type, output_type):
        super().__init__(input_type=input_type, output_type=output_type)

    def get_power_status(self):
        final_val = {}
        for op in self.output_type:
            final_val[op] = f"You are connected to wallpower"
        return final_val


# Create instances of the classes
battery = Battery(True, BatteryStatus.ONBATTERY.value, 100)
echo_show = EchoShow(InputType.TYPE.value, [OutputType.DISPLAY.value, OutputType.SOUND.value], battery)
print(echo_show.get_power_status())

battery = Battery(None, BatteryStatus.PLUGGEDIN.value, None)
echo_dot = EchoDot(InputType.TYPE.value, [OutputType.SOUND.value])
print(echo_dot.get_power_status())


###########


from enum import Enum
from abc import ABC, abstractmethod

class DeviceType(Enum):
    ECHO_SHOW = 1
    ECHO_DOT = 2

class InputType(Enum):
    TYPE = 1
    VOICE = 2
    TOUCH = 3

class OutputType(Enum):
    DISPLAY = 'display'
    SOUND = 'say'

class BatteryStatus(Enum):
    PLUGGEDIN = 1
    ONBATTERY = 2

class Input(ABC):
    @abstractmethod
    def get_input_type(self):
        pass

class Output(ABC):
    @abstractmethod
    def get_output_type(self):
        pass

class Battery:
    def __init__(self, status, value):
        self.status = status
        self.value = value

    def get_status(self):
        return self.status

    def get_value(self):
        return self.value

    def update_status(self, status):
        self.status = status

    def update_value(self, value):
        self.value = value

class Device(ABC):
    def __init__(self, input_device, output_device):
        self.input_device = input_device
        self.output_device = output_device

    def get_input_device(self):
        return self.input_device

    def get_output_device(self):
        return self.output_device

    @abstractmethod
    def get_power_status(self):
        pass

class EchoShow(Device):
    def __init__(self, input_device, output_device, battery):
        super().__init__(input_device, output_device)
        self.battery = battery

    def get_power_status(self):
        final_val = {}
        for output in self.output_device:
            status_str = f"You have a battery of {self.battery.get_value()}%"
            if self.battery.get_status() == BatteryStatus.PLUGGEDIN:
                status_str += " and charging"
            final_val[output] = status_str
        return final_val

class EchoDot(Device):
    def __init__(self, input_device, output_device):
        super().__init__(input_device=input_device, output_device=output_device)

    def get_power_status(self):
        final_val = {}
        for output in self.output_device:
            final_val[output] = f"You are connected to wall power"
        return final_val

# Factory for creating devices
class DeviceFactory:
    @staticmethod
    def create_device(device_type, input_type, output_type, battery=None):
        input_device = None
        output_device = None

        if input_type == InputType.TYPE:
            input_device = KeyboardInput()
        elif input_type == InputType.VOICE:
            input_device = VoiceInput()
        elif input_type == InputType.TOUCH:
            input_device = TouchInput()

        if output_type == OutputType.DISPLAY:
            output_device = DisplayOutput()
        elif output_type == OutputType.SOUND:
            output_device = SoundOutput()

        if device_type == DeviceType.ECHO_SHOW:
            return EchoShow(input_device, output_device, battery)
        elif device_type == DeviceType.ECHO_DOT:
            return EchoDot(input_device, output_device)

# Concrete implementations of Input and Output interfaces
class KeyboardInput(Input):
    def get_input_type(self):
        return InputType.TYPE

class VoiceInput(Input):
    def get_input_type(self):
        return InputType.VOICE

class TouchInput(Input):
    def get_input_type(self):
        return InputType.TOUCH

class DisplayOutput(Output):
    def get_output_type(self):
        return OutputType.DISPLAY

class SoundOutput(Output):
    def get_output_type(self):
        return OutputType.SOUND


# Usage example
battery = Battery(BatteryStatus.ONBATTERY, 100)
echo_show = DeviceFactory.create_device(DeviceType.ECHO_SHOW, InputType.TYPE, [OutputType.DISPLAY, OutputType.SOUND], battery)
print(echo_show.get_power_status())

echo_dot = DeviceFactory.create_device(DeviceType.ECHO_DOT, InputType.TYPE, [OutputType.SOUND])
print(echo_dot.get_power_status())




