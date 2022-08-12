class DataCapture:
    inputs = []

    def build_stats(self):
        return self

    def add(self, value: int):
        if (value > 1000):
            print(f'Cant add {value} is greater than 1000')
        else:
            self.inputs.append(value)

    def less(self, value: int) -> None:
        result = 0
        for x in self.inputs: 
            if x < value:
                result += 1
        print(f'Result: {result}. Only {result} values are less than {value}.')

    def between(self, value1: int, value2: int) -> None:
        result = 0
        for x in self.inputs: 
            if value1 <= x <= value2:
                result += 1
        print(f'Result: {result}. Only {result} values are between {value1} and {value2}.')

    def greater(self, value: int) -> None:
        result = 0
        for x in self.inputs: 
            if x > value:
                result += 1
        print(f'Result: {result}. Only {result} values are greater than {value}.')


if __name__ == '__main__':
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()
    stats.less(4)
    stats.between(3, 6)
    stats.greater(4)