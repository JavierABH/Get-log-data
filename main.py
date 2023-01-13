from log import Log
import glob
import matplotlib.pyplot as plt
import csv

# Define the path where the log files are located
logs_path = r"C:\Users\K90011729\Documents\Graph Cycle time\Report"
# fields = ['Model', 'PartNumber', 'Date', 'Cycle Time' ] 
# Define the fields that will be used in the CSV report.
fields = ['Date', 'Serial', 'Model', 'PartNumber', 'Status', 'Green Led X Status', 'X Time', 'Green Led Y Status', 'Y Time ']

def main():
    # Initialize empty lists for storing data from the log files.
    serials = []
    dates = []
    cycle_times = []
    models = []
    part_numbers = []
    leds_greenx_status = []
    leds_greenx_measurements = []
    status = []
    # ADD Y LED GREEN
    leds_greeny_status = []
    leds_greeny_measurements = []

    # Use the glob library to search for log files in the specified directory,
    # and for each log file found:
    for path in glob.iglob(f'{logs_path}/*'):
        log = Log(path)

        # print(log.get_partnumber().__repr__())
        #  Extract the serial number, model, date, cycle time, part number, status, 
        # Green Led X status, Green Led X measurements, Green Led Y status and Green Led Y 
        # measurements from the log file using methods from the Log class.
        serial = log.get_serial()
        model = log.get_model()
        date = log.get_datetime()
        print(date)
        # print(path)
        cycle_time = log.get_cycle_time()
        part_number = log.get_partnumber()
        utt_status = log.get_utt_status()
        led_greenx_info, led_greenx_measurement = log.get_test_green_ledx()
        led_greeny_info, led_greeny_measurement = log.get_test_green_ledy()


        #------------For cycle time---------------#
        # if log.get_utt_status():
            # if log.get_operator():
                # models.append(model)
                # part_numbers.append(part_number)
                # dates.append(date)
                # cycle_times.append(cycle_time)
        #----------------------------------------#

         # Only append data if the model is "Switchback" and the operator is present
        if log.get_operator():
            if model == "Switchback":
                serials.append(serial)
                models.append(model)
                part_numbers.append(part_number)
                dates.append(date)
                cycle_times.append(cycle_time)
                leds_greenx_status.append(led_greenx_info)
                leds_greeny_status.append(led_greeny_info)
                leds_greenx_measurements.append(led_greenx_measurement)
                leds_greeny_measurements.append(led_greeny_measurement)
                status.append(utt_status)
    
    # Write the data stored in the lists to a CSV file using the csv library.
    print("Write CSV")
    # ------------ start write in csv ---------------- #
    with open('Info green led only sw.csv', 'w', newline='') as f:
        write = csv.writer(f)
        write.writerow(fields)
        # for row in zip(models, part_numbers, dates, cycle_times):
        for row in zip(dates ,serials, models, part_numbers, status, leds_greenx_status, leds_greenx_measurements, leds_greeny_status, leds_greeny_measurements):
            write.writerow(row)
            print(row)

    # print(dates)
    # print(cycle_times)
    # plt.plot(dates, cycle_times, marker='.', linestyle='-')
    # plt.xlabel('Day')
    # plt.ylabel('Seconds')
    # plt.title('Cycle time before vs after speed')
    # plt.show()

if __name__ == "__main__":
    main()