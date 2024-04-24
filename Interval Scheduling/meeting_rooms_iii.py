import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Sort the meetings based on their start times
        sorted_meetings = sorted(meetings, key=lambda x: x[0])

        # Initialize lists to track room occupancy and availability
        occupied = []  # Heap to track occupied rooms (sorted by end time)
        available = [idx for idx in range(n)]  # List to track available rooms
        room_mappings = [0] * n  # List to track the number of meetings booked in each room

        # Iterate through the sorted meetings
        for meeting_start, meeting_end in sorted_meetings:
            # Update the occupied rooms based on the current meeting's start time
            while occupied and occupied[0][0] <= meeting_start:
                _end, room_id = heapq.heappop(occupied)
                heapq.heappush(available, room_id)

            # Assign a room for the current meeting
            if available:
                room_idx = heapq.heappop(available)  # Get the room with the lowest index
                heapq.heappush(occupied, (meeting_end, room_idx))  # Mark the room as occupied
            else:
                # If no available rooms, find the earliest ending meeting and extend its duration
                _end, room_idx = heapq.heappop(occupied)
                meeting_end = (_end - meeting_start) + meeting_end
                heapq.heappush(occupied, (meeting_end, room_idx))

            # Update the number of meetings booked in the assigned room
            room_mappings[room_idx] += 1

        # Find the index of the room with the maximum number of booked meetings
        most_booked_room_idx = room_mappings.index(max(room_mappings))
        return most_booked_room_idx
