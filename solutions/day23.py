from collections import deque
from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def solve(self, part_num: int):
        self.test_runner(part_num)

        func = getattr(self, f"part{part_num}")
        result = func(self.data)
        return result

    def test_runner(self, part_num):
        test_inputs = self.get_test_input()
        test_results = self.get_test_result(part_num)
        test_counter = 1

        func = getattr(self, f"part{part_num}")
        for i, r in zip(test_inputs, test_results):
            if len(r):
                if func(i) == int(r[0]):
                    print(f"test {test_counter} passed")
                else:
                    print(func(i))
                    print(r[0])
                    print(f"test {test_counter} NOT passed")
            test_counter += 1
        print()

    def part1(self, data):
        puzzle = "".join([c for line in data for c in line if c not in "#"])
        organized = "." * 11 + "ABCD" * ((len(puzzle) - 11) // 4)

        return self.find_minimal_energy(puzzle, organized)

    def part2(self, data):
        data = data[:-2] + ["#D#C#B#A#", "#D#B#A#C#"] + data[-2:]
        puzzle = "".join([c for line in data for c in line if c not in "#"])
        organized = "." * 11 + "ABCD" * ((len(puzzle) - 11) // 4)

        return self.find_minimal_energy(puzzle, organized)

    def find_minimal_energy(self, puzzle, organized):
        energies = []

        start = (puzzle, 0, [puzzle])
        seen = {puzzle: 0}

        queue = deque([start])
        while queue:
            state, energy, history = queue.popleft()

            if state == organized:
                energies += [(energy, history)]
            else:
                moves = self.get_next_moves(state, energy)
                for (next_state, next_energy) in moves:
                    if next_state not in seen or seen[next_state] > next_energy:
                        seen[next_state] = next_energy
                        queue.append((next_state, next_energy, history + [next_state]))

        energies = sorted(energies, key=lambda x: x[0])
        # print(energies[0][1])
        return energies[0][0]

    def parse_state(self, state):
        hallway = state[:11]
        rooms = [[state[11:][k * 4 + i] for k in range((len(state) - 11) // 4)] for i in range(4)]
        return hallway, rooms

    def get_next_moves(self, state, energy):
        costs = {"A": 1, "B": 10, "C": 100, "D": 1000}
        room_door_pos = {"A": 2, "B": 4, "C": 6, "D": 8}
        hallway_slot_pos = [0, 1, 3, 5, 7, 9, 10]

        hallway, rooms = self.parse_state(state)
        moves = []

        for pos, c in enumerate(hallway):
            if c != ".":
                a, b = min(room_door_pos[c], pos), max(room_door_pos[c], pos)
                if hallway[a + 1 : b].count(".") == (b - a - 1):
                    target_room = (room_door_pos[c] // 2) - 1
                    if len(set(rooms[target_room]) - {".", c}) == 0:
                        next_state, steps = self.hallway_to_room(state, pos, target_room)
                        moves += [(next_state, energy + steps * costs[c])]

        for room_idx, room in enumerate(rooms):
            if len(set(room) - {".", "ABCD"[room_idx]}) == 0:
                continue

            x = [i for i in room if i != "."][0]
            target = rooms[room_door_pos[x] // 2 - 1]
            if len(set(target) - {".", x}) == 0:
                room1_door_pos = (room_idx + 1) * 2
                room2_door_pos = room_door_pos[x]
                a, b = min(room1_door_pos, room2_door_pos), max(room1_door_pos, room2_door_pos)
                if hallway[a + 1 : b].count(".") == (b - a - 1):
                    next_state, steps = self.room_to_room(state, room1_door_pos, room2_door_pos)
                    moves += [(next_state, energy + steps * costs[x])]
            else:
                for slot_pos in hallway_slot_pos:
                    door_pos = (room_idx + 1) * 2
                    a, b = min(door_pos, slot_pos), max(door_pos, slot_pos)
                    if hallway[a + 1 : b].count(".") == (b - a - 1) and hallway[slot_pos] == ".":
                        depth = min([i for i, v in enumerate(room) if v != "."])
                        next_state, steps = self.room_to_hallway(state, slot_pos, room_idx, depth)
                        moves += [(next_state, energy + steps * costs[room[depth]])]

        return moves

    def hallway_to_room(self, state, pos, target_room):
        hallway, rooms = self.parse_state(state)

        c = hallway[pos]
        steps = 0

        next_state = hallway[:pos] + "." + hallway[pos + 1 :]
        empty = rooms[target_room].count(".")
        depth = empty - 1
        rooms[target_room][depth] = c
        steps += empty

        next_state += "".join(rooms[i][k] for k in range(len(rooms[0])) for i in range(4))

        room_door_pos = (target_room + 1) * 2
        steps += abs(room_door_pos - pos)

        return next_state, steps

    def room_to_hallway(self, state, slot_pos, room_idx, depth):
        hallway, rooms = self.parse_state(state)

        c = rooms[room_idx][depth]
        rooms[room_idx][depth] = "."
        steps = depth + 1
        next_state = hallway[:slot_pos] + c + hallway[slot_pos + 1 :]
        next_state += "".join(rooms[i][k] for k in range(len(rooms[0])) for i in range(4))

        room_door_pos = (room_idx + 1) * 2
        steps += abs(room_door_pos - slot_pos)

        return next_state, steps

    def room_to_room(self, state, room1_door_pos, room2_door_pos):
        hallway, rooms = self.parse_state(state)

        room1_idx = room1_door_pos // 2 - 1
        room2_idx = room2_door_pos // 2 - 1

        depth1 = min([i for i, v in enumerate(rooms[room1_idx]) if v != "."])
        depth2 = max([i for i, v in enumerate(rooms[room2_idx]) if v == "."])

        rooms[room2_idx][depth2] = rooms[room1_idx][depth1]
        rooms[room1_idx][depth1] = "."

        next_state = hallway + "".join(rooms[i][k] for k in range(len(rooms[0])) for i in range(4))
        steps = abs(room1_door_pos - room2_door_pos) + depth1 + depth2 + 2

        return next_state, steps
