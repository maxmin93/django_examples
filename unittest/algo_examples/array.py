class Array(object):

    def sum_1st_version(self, size, array_string):
        return 0

    def sum_2nd_version(self, size, array_string):
        numbers = [int(number) for number in array_string.split(' ')]
        return sum(numbers)

    def sum(self, size, array_string):
        numbers = [int(number) for number in array_string.split(' ')]
        if size != len(numbers):
            raise Exception('array size is not matched')
        return sum(numbers)