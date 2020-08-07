
def run_timing():
    run_times = []
    while True:
        run_time = input("Enter 10 km run time: ")

        if not run_time:
            break

        run_times.append(float(run_time))

    print(
        f"Average of {sum(run_times)/len(run_times):.2f}, over {len(run_times)} runs")


run_timing()
