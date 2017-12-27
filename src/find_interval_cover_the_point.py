"""
Given a set of intervals and a point, find all intervals that contain this point.

Questions you may ask:
How many intervals?
Are they overlapping?
Are end point and query integer only?
How many point queries?
Will the list of intervals change(add, delete, modify) during querying?

follow up: given an interval, find all intervals that overlap with this interval
"""

# An implementation of interval tree, according to Wikipedia
class IntervalTree:
    def __init__(self, intervals):
        self.top_node = self.divide_intervals(intervals)

    def divide_intervals(self, intervals):

        if not intervals:
            return None

        x_center = self.center(intervals)

        s_center = []
        s_left = []
        s_right = []

        for k in intervals:
            if k.get_end() < x_center:
                s_left.append(k)
            elif k.get_begin() > x_center:
                s_right.append(k)
            else:
                s_center.append(k)

        return Node(x_center, s_center, self.divide_intervals(s_left), self.divide_intervals(s_right))
        

    def center(self, intervals):
        fs = sort_by_begin(intervals)
        length = len(fs)

        return fs[int(length/2)].get_begin()

    def search(self, begin, end=None):
        if end:
            result = []

            for j in xrange(int(begin), int(end)+1):
                for k in self.search(j):
                    result.append(k)
                result = list(set(result))
            return sort_by_begin(result)
        else:
            return self._search(self.top_node, begin, [])
    
    def _search(self, node, point, result): 
        for k in node.s_center:
            if k.get_begin() <= point <= k.get_end():
                result.append(k)
        if point < node.x_center and node.left_node:
            for k in self._search(node.left_node, point, []):
                result.append(k)
        if point > node.x_center and node.right_node:
            for k in self._search(node.right_node, point, []):
                result.append(k)

        return list(set(result))

class Interval:
    def __init__(self, interval):
        self.begin = interval[0]
        self.end = interval[1]
    def get_begin(self):
        return self.begin
    def get_end(self):
        return self.end

class Node:
    def __init__(self, x_center, s_center, left_node, right_node):
        self.x_center = x_center
        self.s_center = sort_by_begin(s_center)
        self.left_node = left_node
        self.right_node = right_node

def sort_by_begin(intervals):
    return sorted(intervals, key=lambda x: x.get_begin())

# intervals: a list of intervals(list): [[1,3],[3,4],[9,11]...]
# x: coordinate of the point
def find_interval_cover_the_point(intervals, x):
    T = IntervalTree(map(Interval,intervals))
    res = T.search(x)
    return [[i.begin, i.end] for i in res]

def find_interval_cover_the_interval(intervals, interval):
    T = IntervalTree(map(Interval,intervals))
    res = T.search(interval[0], interval[1])
    return [[i.begin, i.end] for i in res]

# test
print find_interval_cover_the_point([[1,2],[3,9],[1,5],[2,8]], 2)
print find_interval_cover_the_interval([[1.1,2.3],[3.2,9.3],[1.1,5.2],[2.2,8.3]], [2.0, 3.0])