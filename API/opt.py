def optimal(self):
    """Optimized Optimal algorithm implementation"""
    memory = []
    page_faults = 0
    for idx, page in enumerate(self.reference_string):
        if page not in memory:
            page_faults += 1
            if len(memory) < self.frames:
                memory.append(page)
            else:
                future_indices = {}
                for frame in memory:
                    try:
                        future_indices[frame] = self.reference_string[idx+1:].index(frame)
                    except ValueError:
                        future_indices[frame] = float('inf')
                to_remove = max(memory, key=lambda x: future_indices[x])
                memory.remove(to_remove)
                memory.append(page)
    return page_faults