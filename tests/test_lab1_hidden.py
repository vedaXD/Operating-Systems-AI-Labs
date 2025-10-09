"""
INSTRUCTOR TEST SUITE - Lab 1: CPU Scheduling
===============================================
This file contains hidden test cases that validate student implementations.
Students can see this file but should NOT modify it.
These tests run automatically in GitHub Actions.
"""

import sys
import os

# Add the lab directory to path for imports
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Lab1_CPU_Scheduling'))

try:
    from scheduling import fcfs, sjf, round_robin, priority_scheduling
except ImportError as e:
    print(f"❌ Import Error: {e}")
    print("Make sure scheduling.py exists in Lab1_CPU_Scheduling/")
    sys.exit(1)

class HiddenTestRunner:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.total = 0
        self.points = 0
        self.max_points = 100
    
    def run_test(self, test_name, test_func, points=10):
        """Run a single test and track results"""
        self.total += 1
        try:
            test_func()
            print(f"✅ {test_name} - PASSED ({points} points)")
            self.passed += 1
            self.points += points
        except NotImplementedError as e:
            print(f"⏸️  {test_name} - NOT IMPLEMENTED ({str(e)})")
            self.failed += 1
        except Exception as e:
            print(f"❌ {test_name} - FAILED: {str(e)}")
            self.failed += 1
    
    def get_grade(self):
        """Calculate final grade"""
        percentage = (self.points / self.max_points) * 100
        return min(percentage, 100)

# =============================================================================
# HIDDEN TEST CASES - THESE ARE THE "REAL" TESTS
# =============================================================================

def test_fcfs_basic_correctness():
    """Test FCFS with known correct output"""
    jobs = [(0, 5), (1, 3), (2, 8), (3, 6)]
    schedule, waiting_times, turnaround_times = fcfs(jobs)
    
    # Expected results for FCFS
    expected_waiting = [0, 4, 6, 12]
    expected_turnaround = [5, 7, 14, 18]
    
    assert waiting_times == expected_waiting, f"Waiting times incorrect. Expected {expected_waiting}, got {waiting_times}"
    assert turnaround_times == expected_turnaround, f"Turnaround times incorrect. Expected {expected_turnaround}, got {turnaround_times}"

def test_fcfs_edge_case_empty():
    """Test FCFS with empty job list"""
    schedule, waiting, turnaround = fcfs([])
    assert len(schedule) == 0 and len(waiting) == 0 and len(turnaround) == 0, "Empty input should return empty results"

def test_fcfs_edge_case_single():
    """Test FCFS with single job"""
    schedule, waiting, turnaround = fcfs([(0, 10)])
    assert waiting == [0] and turnaround == [10], "Single job: waiting=0, turnaround=burst_time"

def test_fcfs_same_arrival():
    """Test FCFS with jobs arriving at same time"""
    jobs = [(0, 5), (0, 3), (0, 8)]
    schedule, waiting, turnaround = fcfs(jobs)
    assert len(waiting) == 3, "Should handle same arrival times"

def test_sjf_basic_correctness():
    """Test SJF with known correct output"""
    jobs = [(0, 8), (1, 4), (2, 9), (3, 5)]
    original_jobs = jobs.copy()  # Keep original for comparison
    schedule, waiting_times, turnaround_times = sjf(jobs)
    
    # SJF should process shorter jobs first (when available)
    assert len(waiting_times) == 4, "Should return 4 waiting times"
    assert len(turnaround_times) == 4, "Should return 4 turnaround times"
    
    # Average waiting time should be better than FCFS for this case
    avg_waiting = sum(waiting_times) / len(waiting_times)
    assert avg_waiting <= 6.0, f"SJF should have better average waiting time, got {avg_waiting}"

def test_sjf_optimal_case():
    """Test SJF with case where it should be clearly optimal"""
    jobs = [(0, 1), (0, 5), (0, 2)]
    schedule, waiting, turnaround = sjf(jobs)
    # Should process in order: 1, 2, 5 (burst times)
    expected_waiting = [0, 1, 3]  # For burst order 1,2,5
    total_waiting = sum(waiting)
    assert total_waiting <= 5, f"SJF should minimize waiting time, got total {total_waiting}"

def test_round_robin_implemented():
    """Check if Round Robin is properly implemented"""
    jobs = [(0, 5), (1, 3), (2, 8)]
    result = round_robin(jobs, 2)
    
    if result is None:
        raise NotImplementedError("Round Robin not implemented")
    
    schedule, waiting, turnaround = result
    assert len(schedule) == 3, "Round Robin should return results for all jobs"
    assert all(isinstance(w, (int, float)) for w in waiting), "Waiting times should be numbers"

def test_priority_implemented():
    """Check if Priority Scheduling is properly implemented"""
    jobs = [(0, 5, 2), (1, 3, 1), (2, 8, 3)]  # (arrival, burst, priority)
    result = priority_scheduling(jobs)
    
    if result is None:
        raise NotImplementedError("Priority Scheduling not implemented")
    
    schedule, waiting, turnaround = result
    assert len(schedule) == 3, "Priority Scheduling should return results for all jobs"

def test_advanced_fcfs_delayed_arrival():
    """Test FCFS with jobs arriving at different times"""
    jobs = [(0, 3), (5, 2), (8, 4)]  # Jobs with gaps in arrival
    schedule, waiting, turnaround = fcfs(jobs)
    
    # Job 1: arrives at 0, starts at 0, finishes at 3, waiting = 0
    # Job 2: arrives at 5, starts at 5, finishes at 7, waiting = 0  
    # Job 3: arrives at 8, starts at 8, finishes at 12, waiting = 0
    expected_waiting = [0, 0, 0]
    assert waiting == expected_waiting, f"Delayed arrivals: expected {expected_waiting}, got {waiting}"

def test_advanced_sjf_complex():
    """Test SJF with a more complex scenario"""
    jobs = [(0, 6), (1, 8), (2, 7), (3, 3)]
    schedule, waiting, turnaround = sjf(jobs.copy())
    
    # Should prioritize job with burst=3 when it arrives
    # Total waiting should be optimal
    total_waiting = sum(waiting)
    assert total_waiting <= 10, f"SJF should be optimal, got total waiting {total_waiting}"

# =============================================================================
# TEST RUNNER
# =============================================================================

def run_instructor_tests():
    """Run all instructor-defined tests"""
    print("🔒 INSTRUCTOR TEST SUITE - CPU SCHEDULING")
    print("=" * 60)
    print("These tests validate the correctness of your implementations")
    print("=" * 60)
    
    runner = HiddenTestRunner()
    
    # FCFS Tests (40 points total)
    print("\n📝 Testing FCFS Algorithm...")
    runner.run_test("FCFS Basic Correctness", test_fcfs_basic_correctness, 15)
    runner.run_test("FCFS Empty Input", test_fcfs_edge_case_empty, 5)
    runner.run_test("FCFS Single Job", test_fcfs_edge_case_single, 5)
    runner.run_test("FCFS Same Arrival Times", test_fcfs_same_arrival, 5)
    runner.run_test("FCFS Delayed Arrivals", test_advanced_fcfs_delayed_arrival, 10)
    
    # SJF Tests (30 points total)
    print("\n📝 Testing SJF Algorithm...")
    runner.run_test("SJF Basic Correctness", test_sjf_basic_correctness, 15)
    runner.run_test("SJF Optimal Case", test_sjf_optimal_case, 10)
    runner.run_test("SJF Complex Scenario", test_advanced_sjf_complex, 5)
    
    # Optional Algorithms (30 points total)
    print("\n📝 Testing Optional Algorithms...")
    runner.run_test("Round Robin Implementation", test_round_robin_implemented, 15)
    runner.run_test("Priority Scheduling Implementation", test_priority_implemented, 15)
    
    # Results
    print("\n" + "=" * 60)
    print("📊 FINAL RESULTS")
    print("=" * 60)
    print(f"Tests Passed: {runner.passed}/{runner.total}")
    print(f"Points Earned: {runner.points}/{runner.max_points}")
    print(f"Grade: {runner.get_grade():.1f}%")
    
    if runner.get_grade() >= 90:
        print("🌟 EXCELLENT WORK!")
    elif runner.get_grade() >= 80:
        print("👍 GOOD JOB!")
    elif runner.get_grade() >= 70:
        print("📈 KEEP IMPROVING!")
    else:
        print("💪 KEEP WORKING ON IT!")
    
    print("=" * 60)
    
    # Return appropriate exit code for CI/CD
    if runner.passed >= runner.total // 2:  # At least 50% pass rate
        return 0
    else:
        return 1

if __name__ == "__main__":
    exit_code = run_instructor_tests()
    sys.exit(exit_code)