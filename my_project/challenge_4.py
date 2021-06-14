import psutil
import pandas as pd


def main() -> int:

    # Creates a list to store processes in
    all_processes = list()

    # goes through list of all processes running on the current machine
    for proc in psutil.process_iter():

        # Gets the processes name, ID and Memory Utilization
        current_process = proc.as_dict(attrs=['pid', 'name', 'memory_percent'])

        # Adds the process info to the list
        all_processes.append(current_process)

    # Prints out list for testing
    # for elem in allProcesses:
    #     print(elem)

    # makes the list into a data frame for easy csv exporting
    process_data_frame = pd.DataFrame(all_processes)
    process_data_frame.to_csv(r'ListProcesses.csv', index=False)

    return 0


if __name__ == '__main__':
    exit(main())
