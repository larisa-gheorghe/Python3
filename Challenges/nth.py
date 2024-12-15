def nth(arr, idx):
    if idx >= 0:
        return arr[idx]
    return arr[idx + len(arr)]