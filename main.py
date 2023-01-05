from log import Log
import glob
import matplotlib.pyplot as plt
import csv

logs_path = r"C:\Users\K90011729\Documents\Graph Cycle time\Report"
# fields = ['Model', 'PartNumber', 'Date', 'Cycle Time' ] 
fields = ['Date', 'Serial', 'Model', 'PartNumber', 'Status', 'Green Led X Status', 'X Time', 'Green Led Y Status', 'Y Time ']

def main():
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

    for path in glob.iglob(f'{logs_path}/*'):
        log = Log(path)

        # print(log.get_partnumber().__repr__())

        serial = log.get_serial()
        model = log.get_model()
        date = log.get_datetime()
        print(date)
        cycle_time = log.get_cycle_time()
        part_number = log.get_partnumber()
        led_greenx_info, led_greenx_measurement = log.get_test_green_ledx()
        utt_status = log.get_utt_status()
        led_greeny_info, led_greeny_measurement = log.get_test_green_ledy()

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
            leds_greenx_status.append(led_greenx_info)
            leds_greeny_status.append(led_greeny_info)
            leds_greenx_measurements.append(led_greenx_measurement)
            leds_greeny_measurements.append(led_greeny_measurement)
            status.append(utt_status)
    
    print("Write CSV")
    # ------------ start write in csv ---------------- #
    with open('Info green x led.csv', 'w', newline='') as f:
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