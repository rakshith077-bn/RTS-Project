import matplotlib.pyplot as plt

def plot_metrics(task_execution_times, task_deadline_miss_rate, real_time_compliance):
    plt.figure(figsize=(10, 5))
    plt.plot(task_execution_times, label='Avg. Task Execution Time')
    plt.plot(task_deadline_miss_rate, label='Task Deadline Miss Rate')
    plt.plot(real_time_compliance, label='Real-time Compliance')
    plt.xlabel('Time (iterations)')
    plt.ylabel('Metrics')
    plt.title('Metrics Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()