# 🎓 Operating Systems AI Labs

[![CI](https://github.com/vedaXD/Operating-Systems-AI-Labs/actions/workflows/test.yml/badge.svg)](https://github.com/vedaXD/Operating-Systems-AI-Labs/actions/workflows/test.yml)

Welcome to the Operating Systems AI Labs! This repository contains hands-on programming exercises to explore fundamental Operating System concepts using modern AI-assisted development tools.

## 🤖 AI-Enhanced Learning

This course is designed to work with **GitHub Copilot** - an AI pair programmer that helps you write code faster and learn more effectively. Make sure you have GitHub Copilot enabled in your VS Code!

## 📚 Labs Overview

### 🖥️ **Lab 1: CPU Scheduling Algorithms**
**Location**: `Lab1_CPU_Scheduling/scheduling.py`

Implement and analyze different CPU scheduling algorithms:
- **First Come First Serve (FCFS)** - Simple queue-based scheduling
- **Shortest Job First (SJF)** - Optimal average waiting time
- **Round Robin** - Time-sliced preemptive scheduling  
- **Priority Scheduling** - Process priority-based scheduling

### 💾 **Lab 2: Memory Management & Paging**
**Location**: `Lab2_Memory_Management/paging.py`

Explore page replacement algorithms for virtual memory:
- **LRU (Least Recently Used)** - Replace least recently accessed page
- **FIFO (First In First Out)** - Replace oldest page in memory
- **Optimal** - Replace page not used for longest time (theoretical)

### 📁 **Lab 3: File System Operations**
**Location**: `Lab3_File_System/filesystem.py`

Simulate different file allocation methods:
- **Contiguous Allocation** - Files stored in consecutive blocks
- **Linked Allocation** - Files stored using linked list of blocks
- **Indexed Allocation** - Files use index blocks for location tracking

## 🚀 Getting Started

### 1. **Clone the Repository**
```bash
git clone https://github.com/vedaXD/Operating-Systems-AI-Labs.git
cd Operating-Systems-AI-Labs
```

### 2. **Set Up Your Environment**
```bash
# Install any additional dependencies you need
pip install -r requirements.txt

# Open in VS Code with Copilot enabled
code .
```

### 3. **Choose a Lab and Start Coding**
```bash
# Navigate to any lab directory
cd Lab1_CPU_Scheduling

# Open the main file and start implementing!
code scheduling.py
```

## � How to Use GitHub Copilot

### **Step 1: Write Clear Function Signatures**
GitHub Copilot works best with descriptive function names and docstrings:

```python
def fcfs(jobs):
    """
    Implement First Come First Serve scheduling.
    jobs: list of (arrival_time, burst_time)
    Returns: schedule, waiting_times, turnaround_times
    """
    # Copilot will suggest implementation here!
```

### **Step 2: Use Descriptive Comments**
Guide Copilot with comments about what you want to accomplish:

```python
# Sort jobs by arrival time for FCFS processing
# Calculate waiting time for each job
# Generate schedule with start and end times
```

### **Step 3: Accept and Refine Suggestions**
- Press `Tab` to accept Copilot suggestions
- Press `Esc` to reject suggestions
- Modify suggestions to match your exact requirements

## 🎯 Learning Objectives

By completing these labs, you will:

- ✅ **Understand Core OS Concepts**: CPU scheduling, memory management, file systems
- ✅ **Implement Real Algorithms**: Code the same algorithms used in production systems
- ✅ **Practice AI-Assisted Development**: Learn to work effectively with AI coding tools
- ✅ **Analyze Performance**: Compare different algorithms and understand trade-offs
- ✅ **Professional Development**: Use Git, automated testing, and code review practices

## � Development Workflow

### **For Each Algorithm:**

1. **📖 Read the Documentation**: Understand the algorithm requirements
2. **💻 Write Code with Copilot**: Use AI assistance to implement the algorithm
3. **🧪 Test Your Implementation**: Run your code with sample data
4. **📊 Analyze Results**: Compare performance with other algorithms
5. **📝 Document Your Work**: Add comments and explanations
6. **🚀 Submit via Git**: Push your changes to see automated validation

### **Example Development Session:**
```bash
# 1. Navigate to a lab
cd Lab1_CPU_Scheduling

# 2. Edit the file
code scheduling.py

# 3. Implement using Copilot suggestions
# 4. Test your implementation
python scheduling.py

# 5. Commit your work
git add .
git commit -m "Implement FCFS scheduling algorithm"
git push origin main
```

## 📈 Progress Tracking

Your progress is automatically tracked through GitHub:
- ✅ **Green checkmarks** = Your code passes basic validation
- ❌ **Red X marks** = Issues detected in your submission
- 📊 **Commit history** = Shows your development progression

Check the **Actions** tab in GitHub to see validation results for your submissions.

## 💼 Professional Skills

This course teaches not just Operating Systems concepts, but also modern software development practices:

- **🤖 AI-Assisted Programming**: Working effectively with GitHub Copilot
- **📝 Version Control**: Using Git for code management and collaboration  
- **🔄 Continuous Integration**: Automated validation and testing
- **📖 Code Documentation**: Writing clear, maintainable code
- **🎯 Problem Solving**: Breaking down complex algorithms into manageable pieces

## 🎓 Tips for Success

### **Maximize Copilot Effectiveness:**
- Write detailed docstrings and comments
- Use descriptive variable names
- Break complex problems into smaller functions
- Iterate and refine Copilot suggestions

### **Operating Systems Focus:**
- Understand the **why** behind each algorithm, not just the **how**
- Consider real-world scenarios where each algorithm would be used
- Think about trade-offs: time complexity vs space complexity
- Analyze which algorithms work best for different workloads

### **Professional Development:**
- Commit code frequently with meaningful messages
- Test your implementations thoroughly
- Document any assumptions or design decisions
- Learn from the automated feedback

## 🚀 Ready to Start?

1. Pick a lab that interests you (Lab 1 is recommended for beginners)
2. Open the Python file in VS Code
3. Start coding with GitHub Copilot
4. Push your progress to see automated validation

**Happy coding, and welcome to the world of AI-enhanced Operating Systems learning! 🎉**