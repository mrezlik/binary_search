class BinarySearch:

    def __init__(self, numbers, number):
        self.numbers = sorted(numbers)
        self.number = number
        self.upperRange = len(numbers)-1
        self.minRange = 0;

    def binarySearch(self):
        while True:
            if(self.upperRange < self.minRange):
                return False
            else:
                midPoint = int(self.minRange + (self.upperRange - self.minRange) / 2)
                if(self.numbers[midPoint] < self.number):
                    self.minRange = midPoint + 1
                elif(self.numbers[midPoint] > self.number):
                    self.upperRange = midPoint - 1
                elif(self.number == self.numbers[midPoint]):
                     return True


