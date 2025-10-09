"""
INSTRUCTOR TEST SUITE - Lab 2: Memory Management & Paging
=========================================================
This file contains hidden test cases that validate student implementations.
Students can see this file but should NOT modify it.
These tests run automatically in GitHub Actions.
"""

import sys
import os

# Add the lab directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Lab2_Memory_Management'))

try:
    from paging import lru, fifo, optimal
except ImportError as e:
    print(f"❌ Import Error: {e}")
    print("Make sure paging.py exists in Lab2_Memory_Management/")
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
# HIDDEN TEST CASES FOR MEMORY MANAGEMENT
# =============================================================================

def test_lru_basic_correctness():
    """Test LRU with known correct page fault count"""
    pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    capacity = 3
    result = lru(pages, capacity)
    
    if result is None:
        raise NotImplementedError("LRU not implemented")
    
    assert isinstance(result, int), "LRU should return an integer (page fault count)"
    # For this specific case with capacity 3, LRU should have 9 page faults
    expected_faults = 9
    assert result == expected_faults, f"Expected {expected_faults} page faults, got {result}"

def test_lru_simple_case():
    """Test LRU with simple case"""
    pages = [1, 2, 3, 1, 2]
    capacity = 2
    result = lru(pages, capacity)
    
    if result is None:
        raise NotImplementedError("LRU not implemented")
    
    # Should have 4 page faults: 1(miss), 2(miss), 3(miss,replace 1), 1(miss,replace 2), 2(miss,replace 3)
    expected_faults = 4
    assert result == expected_faults, f"Expected {expected_faults} page faults, got {result}"

def test_lru_edge_cases():
    """Test LRU edge cases"""
    # Empty pages
    result = lru([], 3)
    assert result == 0, "Empty pages should result in 0 page faults"
    
    # Zero capacity
    result = lru([1, 2, 3], 0)
    assert result == 3, "Zero capacity should fault on every page"
    
    # Capacity larger than unique pages
    result = lru([1, 2, 1, 2], 5)
    assert result == 2, "Large capacity should only fault on unique pages"

def test_fifo_basic_correctness():
    """Test FIFO with known correct page fault count"""
    pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    capacity = 3
    result = fifo(pages, capacity)
    
    if result is None:
        raise NotImplementedError("FIFO not implemented")
    
    assert isinstance(result, int), "FIFO should return an integer (page fault count)"
    # For this specific case with capacity 3, FIFO should have 9 page faults
    expected_faults = 9
    assert result == expected_faults, f"Expected {expected_faults} page faults, got {result}"

def test_fifo_simple_case():
    """Test FIFO with simple case"""
    pages = [1, 2, 3, 4]
    capacity = 2
    result = fifo(pages, capacity)
    
    if result is None:
        raise NotImplementedError("FIFO not implemented")
    
    # Should have 4 page faults (all pages fault since capacity < unique pages)
    expected_faults = 4
    assert result == expected_faults, f"Expected {expected_faults} page faults, got {result}"

def test_fifo_edge_cases():
    """Test FIFO edge cases"""
    # Single page
    result = fifo([1], 3)
    assert result == 1, "Single page should result in 1 page fault"
    
    # Repeated same page
    result = fifo([1, 1, 1], 1)
    assert result == 1, "Repeated same page should only fault once"

def test_optimal_basic_correctness():
    """Test Optimal with known correct page fault count"""
    pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    capacity = 3
    result = optimal(pages, capacity)
    
    if result is None:
        raise NotImplementedError("Optimal not implemented")
    
    assert isinstance(result, int), "Optimal should return an integer (page fault count)"
    # Optimal should have the minimum possible page faults (6 for this case)
    expected_faults = 6
    assert result == expected_faults, f"Expected {expected_faults} page faults, got {result}"

def test_optimal_should_be_best():
    """Test that Optimal performs better than or equal to other algorithms"""
    pages = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    capacity = 3
    
    try:
        optimal_faults = optimal(pages, capacity)
        if optimal_faults is None:
            raise NotImplementedError("Optimal not implemented")
            
        # Test against FIFO if implemented
        try:
            fifo_faults = fifo(pages.copy(), capacity)
            if fifo_faults is not None:
                assert optimal_faults <= fifo_faults, f"Optimal ({optimal_faults}) should be ≤ FIFO ({fifo_faults})"
        except:
            pass
            
        # Test against LRU if implemented  
        try:
            lru_faults = lru(pages.copy(), capacity)
            if lru_faults is not None:
                assert optimal_faults <= lru_faults, f"Optimal ({optimal_faults}) should be ≤ LRU ({lru_faults})"
        except:
            pass
            
    except NotImplementedError:
        raise NotImplementedError("Optimal not implemented")

def test_algorithm_consistency():
    """Test that algorithms return consistent results"""
    pages = [1, 2, 3, 2, 1, 4, 5]
    capacity = 3
    
    # Test LRU consistency
    try:
        result1 = lru(pages.copy(), capacity)
        result2 = lru(pages.copy(), capacity)
        if result1 is not None and result2 is not None:
            assert result1 == result2, "LRU should return consistent results"
    except:
        pass
    
    # Test FIFO consistency
    try:
        result1 = fifo(pages.copy(), capacity)
        result2 = fifo(pages.copy(), capacity)
        if result1 is not None and result2 is not None:
            assert result1 == result2, "FIFO should return consistent results"
    except:
        pass

def test_performance_comparison():
    """Test performance characteristics of different algorithms"""
    pages = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7]
    capacity = 4
    
    results = {}
    
    # Collect results from implemented algorithms
    try:
        lru_result = lru(pages.copy(), capacity)
        if lru_result is not None:
            results['LRU'] = lru_result
    except:
        pass
    
    try:
        fifo_result = fifo(pages.copy(), capacity)
        if fifo_result is not None:
            results['FIFO'] = fifo_result
    except:
        pass
        
    try:
        optimal_result = optimal(pages.copy(), capacity)
        if optimal_result is not None:
            results['Optimal'] = optimal_result
    except:
        pass
    
    # Ensure all results are reasonable (not negative, not too high)
    for alg, result in results.items():
        assert 0 <= result <= len(pages), f"{alg} page faults should be between 0 and {len(pages)}"

# =============================================================================
# TEST RUNNER
# =============================================================================

def run_instructor_tests():
    """Run all instructor-defined tests for Lab 2"""
    print("🔒 INSTRUCTOR TEST SUITE - MEMORY MANAGEMENT & PAGING")
    print("=" * 60)
    print("These tests validate the correctness of your implementations")
    print("=" * 60)
    
    runner = HiddenTestRunner()
    
    # LRU Tests (40 points total)
    print("\n📝 Testing LRU Algorithm...")
    runner.run_test("LRU Basic Correctness", test_lru_basic_correctness, 15)
    runner.run_test("LRU Simple Case", test_lru_simple_case, 10)
    runner.run_test("LRU Edge Cases", test_lru_edge_cases, 15)
    
    # FIFO Tests (30 points total)
    print("\n📝 Testing FIFO Algorithm...")
    runner.run_test("FIFO Basic Correctness", test_fifo_basic_correctness, 15)
    runner.run_test("FIFO Simple Case", test_fifo_simple_case, 10)
    runner.run_test("FIFO Edge Cases", test_fifo_edge_cases, 5)
    
    # Optimal Tests (20 points total)
    print("\n📝 Testing Optimal Algorithm...")
    runner.run_test("Optimal Basic Correctness", test_optimal_basic_correctness, 15)
    runner.run_test("Optimal Should Be Best", test_optimal_should_be_best, 5)
    
    # Advanced Tests (10 points total)
    print("\n📝 Testing Advanced Properties...")
    runner.run_test("Algorithm Consistency", test_algorithm_consistency, 5)
    runner.run_test("Performance Comparison", test_performance_comparison, 5)
    
    # Results
    print("\n" + "=" * 60)
    print("📊 FINAL RESULTS - LAB 2")
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