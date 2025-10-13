# Starter code for Memory Management & Paging Lab

def lru(pages, capacity):
    """
    Implement LRU page replacement.
    pages: list of page references
    capacity: number of frames
    Returns: page faults count
    """
    # TODO: Implement LRU page replacement algorithm
    # For now, return 0 to prevent test failures
    if not pages or capacity <= 0:
        return len(pages) if capacity == 0 else 0
    
    # Return stub value - needs actual implementation
    return 0

def fifo(pages, capacity):
    """
    Implement FIFO page replacement.
    pages: list of page references
    capacity: number of frames
    Returns: page faults count
    """
    # TODO: Implement FIFO page replacement algorithm
    # For now, return 0 to prevent test failures
    if not pages or capacity <= 0:
        return len(pages) if capacity == 0 else 0
    
    # Return stub value - needs actual implementation
    return 0

def optimal(pages, capacity):
    """
    Implement Optimal page replacement.
    pages: list of page references
    capacity: number of frames
    Returns: page faults count
    """
    # TODO: Implement Optimal page replacement algorithm
    # For now, return 0 to prevent test failures
    if not pages or capacity <= 0:
        return len(pages) if capacity == 0 else 0
    
    # Return stub value - needs actual implementation
    return 0

# Example: Use Copilot to also help visualize frame contents after each reference!
