from datetime import datetime

class Log:  
    def __init__(self, path) -> None:
        """
        Initialize a Log object with the path to the log file.
        """
        self.path = path
        self.cycle_time = None
        self.date = None
        self.model = None
        self.utt_status = None
        self.partnumber = None
        self.operator = None
        self.serial = None

    def get_raw(self):
        """
        Read the contents of the log file as a string
        """
        with open(self.path) as logfile:
            return logfile.read()

    def get_lines(self):
        """
        Read the contents of the log file as a list of lines
        """
        with open(self.path) as logfile:
            return logfile.readlines()

    def get_str_date(self):
        """
        Extract and return the date string from the log file.
        """
        for line in self.get_lines():
            if "Date:" in line:
                date_str = line[30:]
                return date_str.rstrip('\n')

    def get_datetime(self):
        """
        Extract and return the datetime from the log file.
        """
        date_str = self.get_str_date()
        date_tmp = datetime.strptime(date_str, '%A, %B %d, %Y')
        self.date = date_tmp.strftime("%m/%d/%Y")
        return self.date

    def get_cycle_time(self):
        """
        Extract and return the cycle time from the log file
        """
        for line in self.get_lines():
            if "Execution Time:" in line:
                cycle_time_str = line[30:].rstrip('\n').split(' ')[0]
                self.cycle_time = float(cycle_time_str) #round(float(cycle_time_str),2)
                return self.cycle_time

    def get_model(self):
        """
        Extract and return the model from the log file.
        """
        for line in self.get_lines():
            if "(C:\Topaz Sequence\Sequence File" in line:
                model_temp = line[33:].replace(".seq)",'').rstrip('\n')
                if "Topaz" in model_temp:
                    self.model = "Topaz"
                elif "Switchback" in model_temp:
                    self.model = "Switchback"
                return self.model
    
    def get_utt_status(self):
        """
        Extract and return the UTT status from the log file.
        """
        for line in self.get_lines():
            if "UUT Result:" in line:
                self.utt_status = line[30:].rstrip('\n')
                return True if self.utt_status == "Passed" else False

    def get_partnumber(self):
        """
        Extract and return the part number from the log file.
        """
        for line in self.get_lines():
            if "     String:" in line:
                self.partnumber = line[31:].rstrip('\n')
                return self.partnumber

    def get_operator(self):
        """
        Extract and return the operator from the log file.
        """
        for line in self.get_lines():
            if "Operator:" in line:
                self.operator = line[30:].rstrip('\n')
                return True if self.operator == "operator" else False

    def get_test_green_ledx(self):
        """
        Extract and return the data Green Led X status and measurements from the log file.
        """
        led_status = None
        Measurement = None
        lines_i = self.get_lines().__iter__()
        for line in lines_i:
            # ------------------ For test ---------------------------------- #
            # if "TEST 24 - K24 Digital Output - Activate Debug Red LED X:" in line:
            #     status_str = line.split(": ")[1].rstrip('\n')
            #     led_status = True if status_str == "Passed" else False
            #     next_line = lines_i.__next__()
            #     Measurement = next_line[31:].rstrip('\n')
            # ------------------ For test led green x---------------------------------- #
            if "X LED Power Green:" in line:
                status_str = line.split(':')[1].strip(' ').rstrip('\n')
                led_status = True if status_str == "Passed" else False
                next_line = lines_i.__next__()
                Measurement = next_line.split(':')[1].strip(' ').rstrip('\n')

        return (led_status, Measurement)

    def get_test_green_ledy(self):
        """
        Extract and return the data Green Led Y status and measurements from the log file.
        """
        led_status = None
        Measurement = None
        lines_i = self.get_lines().__iter__()
        for line in lines_i:
            if "Y LED Power Green:" in line:
                status_str = line.split(':')[1].strip(' ').rstrip('\n')
                led_status = True if status_str == "Passed" else False
                next_line = lines_i.__next__()
                Measurement = next_line.split(':')[1].strip(' ').rstrip('\n')

        return (led_status, Measurement)

    def get_serial(self):
        """
        Extract and return the serial number from the log file.
        """
        for line in self.get_lines():
            if "Serial Number:" in line:
                self.serial = line[30:].rstrip('\n')
                return self.serial
