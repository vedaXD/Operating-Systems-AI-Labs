# Starter code for CPU Scheduling Algorithms Lab

def fcfs(jobs):
    """
    Implement First Come First Serve scheduling.
    jobs: list of (arrival_time, burst_time)
    Returns: schedule, waiting_times, turnaround_times
    """
    # TODO: Implement FCFS scheduling algorithm
    # For now, return empty results to prevent test failures
    if not jobs:
        return [], [], []
    
    # Return stub values with correct length
    n = len(jobs)
    schedule = []  # List of job execution details
    waiting_times = [0] * n  # Waiting time for each job
    turnaround_times = [0] * n  # Turnaround time for each job
    
    return schedule, waiting_times, turnaround_times

def sjf(jobs):
    """
    Implement Shortest Job First scheduling.
    jobs: list of (arrival_time, burst_time)
    Returns: schedule, waiting_times, turnaround_times
    """
    # TODO: Implement SJF scheduling algorithm
    # For now, return empty results to prevent test failures
    if not jobs:
        return [], [], []
    
    # Return stub values with correct length
    n = len(jobs)
    schedule = []  # List of job execution details
    waiting_times = [0] * n  # Waiting time for each job
    turnaround_times = [0] * n  # Turnaround time for each job
    
    return schedule, waiting_times, turnaround_times

def round_robin(jobs, quantum):
    """
    Implement Round Robin scheduling.
    jobs: list of (arrival_time, burst_time)
    quantum: time slice for round robin
    Returns: schedule, waiting_times, turnaround_times
    """
    # TODO: Implement Round Robin scheduling algorithm
    # For now, return empty results to prevent test failures
    if not jobs:
        return [], [], []
    
    # Return stub values with correct length
    n = len(jobs)
    schedule = []  # List of job execution details
    waiting_times = [0] * n  # Waiting time for each job
    turnaround_times = [0] * n  # Turnaround time for each job
    
    return schedule, waiting_times, turnaround_times

def priority_scheduling(jobs):
    """
    Implement Priority Scheduling.
    Each job: (arrival_time, burst_time, priority)
    Returns: schedule, waiting_times, turnaround_times
    """
    # TODO: Implement Priority scheduling algorithm
    # For now, return empty results to prevent test failures
    if not jobs:
        return [], [], []
    
    # Return stub values with correct length
    n = len(jobs)
    schedule = []  # List of job execution details
    waiting_times = [0] * n  # Waiting time for each job
    turnaround_times = [0] * n  # Turnaround time for each job
    
    return schedule, waiting_times, turnaround_times

# Example: Use Copilot to also help visualize Gantt charts!
