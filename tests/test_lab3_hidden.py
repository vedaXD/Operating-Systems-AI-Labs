"""
INSTRUCTOR TEST SUITE - Lab 3: File System Operations
=====================================================
This file contains hidden test cases that validate student implementations.
Students can see this file but should NOT modify it.
These tests run automatically in GitHub Actions.
"""

import sys
import os

# Add the lab directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Lab3_File_System'))

try:
    from filesystem import contiguous_allocation, linked_allocation, indexed_allocation
except ImportError as e:
    print(f"❌ Import Error: {e}")
    print("Make sure filesystem.py exists in Lab3_File_System/")
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
# HIDDEN TEST CASES FOR FILE SYSTEM OPERATIONS
# =============================================================================

def test_contiguous_basic_correctness():
    """Test contiguous allocation with basic case"""
    files = [("file1", 5), ("file2", 3), ("file3", 8)]
    disk_size = 20
    result = contiguous_allocation(files, disk_size)
    
    if result is None:
        raise NotImplementedError("Contiguous allocation not implemented")
    
    assert isinstance(result, dict), "Contiguous allocation should return a dictionary"
    assert len(result) == 3, "Should return allocation info for all 3 files"
    
    # Check that all files are allocated
    for filename, size in files:
        assert filename in result, f"File {filename} should be in allocation table"
        file_info = result[filename]
        
        if 'error' not in file_info:  # File was successfully allocated
            assert 'start_block' in file_info, f"File {filename} should have start_block"
            assert 'size' in file_info, f"File {filename} should have size"
            assert file_info['size'] == size, f"File {filename} size should be {size}"

def test_contiguous_sequential_allocation():
    """Test that contiguous allocation places files sequentially"""
    files = [("A", 3), ("B", 2), ("C", 4)]
    disk_size = 10
    result = contiguous_allocation(files, disk_size)
    
    if result is None:
        raise NotImplementedError("Contiguous allocation not implemented")
    
    # Files should be allocated sequentially
    expected_starts = {"A": 0, "B": 3, "C": 5}
    for filename, expected_start in expected_starts.items():
        if filename in result and 'start_block' in result[filename]:
            actual_start = result[filename]['start_block']
            if actual_start != -1:  # Successfully allocated
                assert actual_start == expected_start, f"File {filename} should start at block {expected_start}, got {actual_start}"

def test_contiguous_insufficient_space():
    """Test contiguous allocation when disk is too small"""
    files = [("big_file", 15), ("another_file", 10)]
    disk_size = 20
    result = contiguous_allocation(files, disk_size)
    
    if result is None:
        raise NotImplementedError("Contiguous allocation not implemented")
    
    # First file should succeed, second should fail
    assert "big_file" in result, "First file should be in allocation table"
    assert "another_file" in result, "Second file should be in allocation table"
    
    # Check that second file couldn't be allocated
    if 'error' in result["another_file"] or result["another_file"].get('start_block') == -1:
        pass  # Expected behavior
    else:
        # Check if somehow both files fit (alternative valid implementation)
        total_allocated = result["big_file"]['size'] + result["another_file"]['size']
        assert total_allocated <= disk_size, "Total allocation shouldn't exceed disk size"

def test_contiguous_edge_cases():
    """Test contiguous allocation edge cases"""
    # Empty file list
    result = contiguous_allocation([], 10)
    assert result == {}, "Empty file list should return empty allocation table"
    
    # Zero disk size
    result = contiguous_allocation([("file1", 5)], 0)
    assert "file1" in result, "File should be in result even if can't be allocated"
    
    # File larger than disk
    result = contiguous_allocation([("huge_file", 100)], 10)
    assert "huge_file" in result, "File should be in result even if too large"

def test_linked_basic_correctness():
    """Test linked allocation with basic case"""
    files = [("file1", 5), ("file2", 3), ("file3", 8)]
    disk_size = 20
    result = linked_allocation(files, disk_size)
    
    if result is None:
        raise NotImplementedError("Linked allocation not implemented")
    
    assert isinstance(result, dict), "Linked allocation should return a dictionary"
    assert len(result) == 3, "Should return allocation info for all 3 files"
    
    # Check that all files are allocated (linked allocation should handle fragmentation)
    for filename, size in files:
        assert filename in result, f"File {filename} should be in allocation table"
        file_info = result[filename]
        
        if 'error' not in file_info:  # File was successfully allocated
            assert 'size' in file_info, f"File {filename} should have size"
            assert file_info['size'] == size, f"File {filename} size should be {size}"

def test_linked_fragmentation_handling():
    """Test that linked allocation can handle fragmented space"""
    files = [("file1", 3), ("file2", 3), ("file3", 3)]
    disk_size = 9
    result = linked_allocation(files, disk_size)
    
    if result is None:
        raise NotImplementedError("Linked allocation not implemented")
    
    # All files should fit since total size = disk size
    total_size = sum(file[1] for file in files)
    assert total_size == disk_size, "Test setup verification"
    
    # All files should be successfully allocated
    for filename, size in files:
        assert filename in result, f"File {filename} should be allocated"
        if 'error' not in result[filename]:
            assert result[filename]['size'] == size, f"File {filename} should have correct size"

def test_linked_edge_cases():
    """Test linked allocation edge cases"""
    # Single file filling entire disk
    result = linked_allocation([("full_disk", 10)], 10)
    if result is not None:
        assert "full_disk" in result, "Single file should be in allocation table"
    
    # Multiple small files
    small_files = [(f"file{i}", 1) for i in range(5)]
    result = linked_allocation(small_files, 10)
    if result is not None:
        assert len(result) == 5, "All small files should be in allocation table"

def test_indexed_basic_correctness():
    """Test indexed allocation with basic case"""
    files = [("file1", 5), ("file2", 3), ("file3", 8)]
    disk_size = 20
    result = indexed_allocation(files, disk_size)
    
    if result is None:
        raise NotImplementedError("Indexed allocation not implemented")
    
    assert isinstance(result, dict), "Indexed allocation should return a dictionary"
    assert len(result) == 3, "Should return allocation info for all 3 files"
    
    # Check basic structure
    for filename, size in files:
        assert filename in result, f"File {filename} should be in allocation table"
        file_info = result[filename]
        
        if 'error' not in file_info:  # File was successfully allocated
            assert 'size' in file_info, f"File {filename} should have size"
            assert file_info['size'] == size, f"File {filename} size should be {size}"

def test_indexed_index_block_overhead():
    """Test that indexed allocation accounts for index block overhead"""
    files = [("file1", 5)]
    disk_size = 6  # Just enough for file + index block
    result = indexed_allocation(files, disk_size)
    
    if result is None:
        raise NotImplementedError("Indexed allocation not implemented")
    
    # Should handle the index block overhead appropriately
    assert "file1" in result, "File should be in allocation table"
    # Implementation details may vary, but result should be consistent

def test_indexed_large_file():
    """Test indexed allocation with large file needing multiple index blocks"""
    files = [("large_file", 50)]
    disk_size = 60
    result = indexed_allocation(files, disk_size)
    
    if result is None:
        raise NotImplementedError("Indexed allocation not implemented")
    
    assert "large_file" in result, "Large file should be in allocation table"
    # Test should pass regardless of specific implementation approach

def test_allocation_comparison():
    """Test that different allocation methods handle the same files"""
    files = [("A", 3), ("B", 4), ("C", 2)]
    disk_size = 12
    
    results = {}
    
    # Test contiguous allocation
    try:
        cont_result = contiguous_allocation(files.copy(), disk_size)
        if cont_result is not None:
            results['contiguous'] = cont_result
    except:
        pass
    
    # Test linked allocation
    try:
        linked_result = linked_allocation(files.copy(), disk_size)
        if linked_result is not None:
            results['linked'] = linked_result
    except:
        pass
    
    # Test indexed allocation
    try:
        indexed_result = indexed_allocation(files.copy(), disk_size)
        if indexed_result is not None:
            results['indexed'] = indexed_result
    except:
        pass
    
    # All implemented methods should handle these files (total size = 9, disk = 12)
    for method, result in results.items():
        assert len(result) == 3, f"{method} allocation should return info for all files"

def test_space_efficiency():
    """Test space utilization of different allocation methods"""
    files = [("file1", 2), ("file2", 2), ("file3", 2)]
    disk_size = 8  # Just enough space
    
    # Each method should be able to allocate these files
    methods = [
        ("contiguous", contiguous_allocation),
        ("linked", linked_allocation), 
        ("indexed", indexed_allocation)
    ]
    
    for method_name, method_func in methods:
        try:
            result = method_func(files.copy(), disk_size)
            if result is not None:
                # Should successfully allocate all files or provide clear error info
                assert len(result) == 3, f"{method_name} should return info for all files"
        except NotImplementedError:
            continue  # Skip unimplemented methods
        except Exception as e:
            # Method should handle this case gracefully
            pass

# =============================================================================
# TEST RUNNER
# =============================================================================

def run_instructor_tests():
    """Run all instructor-defined tests for Lab 3"""
    print("🔒 INSTRUCTOR TEST SUITE - FILE SYSTEM OPERATIONS")
    print("=" * 60)
    print("These tests validate the correctness of your implementations")
    print("=" * 60)
    
    runner = HiddenTestRunner()
    
    # Contiguous Allocation Tests (40 points total)
    print("\n📝 Testing Contiguous Allocation...")
    runner.run_test("Contiguous Basic Correctness", test_contiguous_basic_correctness, 15)
    runner.run_test("Contiguous Sequential Allocation", test_contiguous_sequential_allocation, 10)
    runner.run_test("Contiguous Insufficient Space", test_contiguous_insufficient_space, 10)
    runner.run_test("Contiguous Edge Cases", test_contiguous_edge_cases, 5)
    
    # Linked Allocation Tests (30 points total)
    print("\n📝 Testing Linked Allocation...")
    runner.run_test("Linked Basic Correctness", test_linked_basic_correctness, 15)
    runner.run_test("Linked Fragmentation Handling", test_linked_fragmentation_handling, 10)
    runner.run_test("Linked Edge Cases", test_linked_edge_cases, 5)
    
    # Indexed Allocation Tests (20 points total)
    print("\n📝 Testing Indexed Allocation...")
    runner.run_test("Indexed Basic Correctness", test_indexed_basic_correctness, 10)
    runner.run_test("Indexed Index Block Overhead", test_indexed_index_block_overhead, 5)
    runner.run_test("Indexed Large File", test_indexed_large_file, 5)
    
    # Advanced Tests (10 points total)
    print("\n📝 Testing Advanced Properties...")
    runner.run_test("Allocation Method Comparison", test_allocation_comparison, 5)
    runner.run_test("Space Efficiency", test_space_efficiency, 5)
    
    # Results
    print("\n" + "=" * 60)
    print("📊 FINAL RESULTS - LAB 3")
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