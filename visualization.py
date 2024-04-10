import matplotlib.pyplot as plt

def plot_metrics(task_execution_times_list, task_deadline_miss_rate_list, real_time_compliance_list):
    plt.figure(figsize=(10, 5))
    plt.plot(task_execution_times_list, label='Avg. Task Execution Time')
    plt.plot(task_deadline_miss_rate_list, label='Task Deadline Miss Rate')
    plt.plot(real_time_compliance_list, label='Real-time Compliance')
    plt.xlabel('Time (iterations)')
    plt.ylabel('Metrics')
    plt.title('Metrics Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()
