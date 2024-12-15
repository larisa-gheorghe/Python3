def running_average():
    running_average.accumulator = 0
    running_average.size = 0
  
    def inner(number):
        running_average.accumulator += number
        running_average.size += 1
        return running_average.accumulator / running_average.size
    
    return inner
