from typing import List

from aocpuzzle import AoCPuzzle


class PasswordRuleLen:
    def __init__(self, min_len: int, max_len: int, char: str, password: str) -> None:
        self.min_len = min_len
        self.max_len = max_len
        self.char = char
        self.password = password


class PasswordRulePos:
    def __init__(self, pos1: int, pos2: int, char: str, password: str) -> None:
        self.pos1 = pos1
        self.pos2 = pos2
        self.char = char
        self.password = password


class Puzzle02(AoCPuzzle):
    def common(self, input_data: List[str]) -> None:
        self.passwords = input_data

    def process_part1_input_data(self) -> List[PasswordRuleLen]:
        processed_input_data = []

        for rule in self.passwords:
            [min_max, char, password] = rule.split()
            min_len, max_len = min_max.split('-')

            processed_input_data.append(
                PasswordRuleLen(int(min_len), int(max_len), char[0], password),
            )

        return processed_input_data

    def process_part2_input_data(self) -> List[PasswordRulePos]:
        processed_input_data = []

        for rule in self.passwords:
            [pos1_pos2, char, password] = rule.split()
            pos1, pos2 = pos1_pos2.split('-')

            processed_input_data.append(
                PasswordRulePos(int(pos1), int(pos2), char[0], password),
            )

        return processed_input_data

    def part1(self) -> int:
        valid_passwords = [
            data.min_len <= data.password.count(data.char) <= data.max_len
            for data in self.process_part1_input_data()
        ]

        return sum(valid_passwords)

    def part2(self) -> int:
        valid_passwords = [
            sum(data.password[pos - 1] == data.char for pos in [data.pos1, data.pos2]) == 1
            for data in self.process_part2_input_data()
        ]

        return sum(valid_passwords)

    def test_cases(self, input_data: List[str]) -> int:
        tests = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
        self.common(tests)
        assert self.part1() == 2
        self.common(tests)
        assert self.part2() == 1

        self.common(input_data)
        assert self.part1() == 620
        self.common(input_data)
        assert self.part2() == 727

        return len(input_data) + len(tests)
