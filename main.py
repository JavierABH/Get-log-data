from log import Log
import glob
import matplotlib.pyplot as plt
import csv

logs_path = r"C:\Users\K90011729\Documents\Graph Cycle time\Report"
# fields = ['Model', 'PartNumber', 'Date', 'Cycle Time' ] 
fields = ['Serial', 'Model', 'PartNumber', 'Date', 'Red Led X Status', 'Red Led X Time' ]

def main():
    serials = []
    dates = []
    cycle_times = []
    models = []
    part_numbers = []
    leds_red_status = []
    leds_red_measurements = []

    for path in glob.iglob(f'{logs_path}/*'):
        log = Log(path)

        # print(log.get_partnumber().__repr__())

        serial = log.serial()
        model = log.get_model()
        date = log.get_datetime()
        print(date)
        cycle_time = log.get_cycle_time()
        part_number = log.get_partnumber()
        led_red_info, led_red_measurement = log.get_test_redled()

        #------------For cycle time---------------#
        # if log.get_utt_status():
            # if log.get_operator():
                # models.append(model)
                # part_numbers.append(part_number)
                # dates.append(date)
                # cycle_times.append(cycle_time)
        #----------------------------------------#
        if log.get_operator():
            serials.append(serial)
            models.append(model)
            part_numbers.append(part_number)
            dates.append(date)
            cycle_times.append(cycle_time)
            leds_red_status.append(led_red_info)
            leds_red_measurements.append(led_red_measurement)
    
    print("Write CSV")
    with open('Info red led.csv', 'w', newline='') as f:
        write = csv.writer(f)
        write.writerow(fields)
        # for row in zip(models, part_numbers, dates, cycle_times):
        for row in zip(serials, models, part_numbers, dates, leds_red_status, leds_red_measurements):
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