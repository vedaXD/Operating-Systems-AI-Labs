# Starter code for CPU Scheduling Algorithms Lab

def fcfs(jobs):
    """
    Implement First Come First Serve scheduling.
    jobs: list of (arrival_time, burst_time)
    Returns: schedule, waiting_times, turnaround_times
    """
    if not jobs:
        return [], [], []
    
    # Sort jobs by arrival time (FCFS principle)
    sorted_jobs = sorted(enumerate(jobs), key=lambda x: x[1][0])
    
    schedule = []
    waiting_times = [0] * len(jobs)
    turnaround_times = [0] * len(jobs)
    
    current_time = 0
    
    for original_index, (arrival_time, burst_time) in sorted_jobs:
        # If CPU is idle, advance time to job arrival
        if current_time < arrival_time:
            current_time = arrival_time
        
        # Calculate start and end times
        start_time = current_time
        end_time = start_time + burst_time
        
        # Add to schedule
        schedule.append({
            'job_id': original_index,
            'start_time': start_time,
            'end_time': end_time,
            'arrival_time': arrival_time,
            'burst_time': burst_time
        })
        
        # Calculate waiting and turnaround times
        waiting_times[original_index] = start_time - arrival_time
        turnaround_times[original_index] = end_time - arrival_time
        
        # Update current time
        current_time = end_time
    
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

def visualize_gantt_chart(schedule, jobs):
    """
    Create a simple text-based Gantt chart visualization
    """
    if not schedule:
        print("No schedule to visualize!")
        return
    
    print("\n" + "="*60)
    print("📊 GANTT CHART VISUALIZATION")
    print("="*60)
    
    # Sort schedule by start time for proper visualization
    sorted_schedule = sorted(schedule, key=lambda x: x['start_time'])
    
    # Print job details first
    print("\n📋 Job Details:")
    for i, (arrival, burst) in enumerate(jobs):
        print(f"  Job {i}: Arrival={arrival}, Burst={burst}")
    
    # Print timeline
    print(f"\n⏰ Timeline:")
    timeline = "Time: "
    gantt = "Jobs: "
    
    max_time = max(item['end_time'] for item in sorted_schedule)
    
    # Create timeline representation
    current_pos = 0
    for item in sorted_schedule:
        job_id = item['job_id']
        start = item['start_time']
        end = item['end_time']
        duration = end - start
        
        # Add idle time if there's a gap
        if start > current_pos:
            idle_duration = start - current_pos
            timeline += f"{current_pos:>3}"
            gantt += f"{'IDLE':>3}"
            for _ in range(idle_duration - 1):
                timeline += "   "
                gantt += "   "
            current_pos = start
        
        # Add job execution
        timeline += f"{start:>3}"
        gantt += f"J{job_id:>2}"
        for _ in range(duration - 1):
            timeline += "---"
            gantt += "---"
        current_pos = end
    
    # Add final time marker
    timeline += f"{max_time:>3}"
    gantt += "   "
    
    print(timeline)
    print(gantt)
    
    # Print execution order
    print(f"\n🔄 Execution Order:")
    for i, item in enumerate(sorted_schedule):
        job_id = item['job_id']
        start = item['start_time']
        end = item['end_time']
        print(f"  {i+1}. Job {job_id}: Time {start} → {end} (Duration: {end-start})")

def test_fcfs_example():
    """
    Test FCFS with a sample case and visualize results
    """
    print("🧪 TESTING FCFS ALGORITHM")
    print("="*50)
    
    # Test case: Jobs with different arrival times
    jobs = [
        (0, 5),   # Job 0: arrives at 0, needs 5 time units
        (2, 3),   # Job 1: arrives at 2, needs 3 time units  
        (4, 1),   # Job 2: arrives at 4, needs 1 time unit
        (6, 2)    # Job 3: arrives at 6, needs 2 time units
    ]
    
    print(f"\n📝 Input Jobs: {jobs}")
    print("   Format: (arrival_time, burst_time)")
    
    # Run FCFS algorithm
    schedule, waiting_times, turnaround_times = fcfs(jobs)
    
    # Display results
    print(f"\n📊 RESULTS:")
    print(f"⏳ Waiting Times: {waiting_times}")
    print(f"🔄 Turnaround Times: {turnaround_times}")
    print(f"📈 Average Waiting Time: {sum(waiting_times)/len(waiting_times):.2f}")
    print(f"📈 Average Turnaround Time: {sum(turnaround_times)/len(turnaround_times):.2f}")
    
    # Show detailed schedule
    print(f"\n📋 Detailed Schedule:")
    for item in sorted(schedule, key=lambda x: x['start_time']):
        job_id = item['job_id']
        start = item['start_time']
        end = item['end_time']
        arrival = item['arrival_time']
        burst = item['burst_time']
        waiting = waiting_times[job_id]
        turnaround = turnaround_times[job_id]
        
        print(f"  Job {job_id}: Start={start:2d}, End={end:2d} | " +
              f"Waiting={waiting:2d}, Turnaround={turnaround:2d}")
    
    # Visualize Gantt chart
    visualize_gantt_chart(schedule, jobs)
    
    return schedule, waiting_times, turnaround_times

# Run the test when this file is executed directly
if __name__ == "__main__":
    test_fcfs_example()
