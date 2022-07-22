import heapq


def meeting_rooms(meetings):
    # Each item in the meetings is an interval of start and end point
    # Sort the meetings based on their first item (the start of the range)
    meetings.sort(key=lambda x: x[0])

    # Define variables
    meeting_ends = []  # Empty heap
    max_rooms = 0  # Max number of rooms needed

    # Iterate through each meeting in meetings
    for meeting in meetings:
        # While the heap has item which is the end time of some meeting
        # (that means if the heap is empty we will skip it)
        # And while the first item of the heep (which is the end time of some meeting)
        # is smaller or equal to the starting time of the current meeting
        # We will be able to determine that the meetings do not clash and we can pop the item from the heap
        while meeting_ends and meeting_ends[0] <= meeting[0]:
            heapq.heappop(meeting_ends)

        # Push the end time of the current meeting into the heep
        heapq.heappush(meeting_ends, meeting[1])

        # Set max_rooms to the maximum value between the previous value of max rooms and the current length of the heap
        max_rooms = max(max_rooms, len(meeting_ends))
    return max_rooms


print(meeting_rooms([[0, 10], [10, 20]]))
# 1

print(meeting_rooms([[20, 30], [10, 21], [0, 50]]))
# 3
