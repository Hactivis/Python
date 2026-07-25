class SmartDevice:
    def __init__(self, device_name, power_status):
        self.device_name = device_name
        self.power_status = power_status

        # shadowning the class attribute
        self.brand = "CustomBrand"

def get_status(self):
    status = "ON" if self.power_status else "OFF"
    return f"{self.status} is {status} - {self.brand}"