# Starter code for File System Operations Lab

def contiguous_allocation(files, disk_size):
    """
    Simulate contiguous allocation of files on disk.
    files: list of (filename, size)
    disk_size: total disk blocks
    Returns: allocation table
    """
    pass  # Use Copilot to generate this function!

def linked_allocation(files, disk_size):
    """
    Simulate linked allocation of files on disk.
    files: list of (filename, size) or list of dicts with 'name' and 'size'
    disk_size: total disk blocks
    Returns: allocation table
    """
    # TODO: Implement linked allocation algorithm
    # For now, return empty dict to prevent test failures
    if not files or disk_size <= 0:
        return {}
    
    # Return stub value - needs actual implementation
    return {}

def indexed_allocation(files, disk_size):
    """
    Simulate indexed allocation of files on disk.
    files: list of (filename, size) or list of dicts with 'name' and 'size'
    disk_size: total disk blocks
    Returns: allocation table
    """
    # TODO: Implement indexed allocation algorithm
    # For now, return empty dict to prevent test failures
    if not files or disk_size <= 0:
        return {}
    
    # Return stub value - needs actual implementation
    return {}

# Example: Use Copilot to simulate file search and visualize disk allocation!
