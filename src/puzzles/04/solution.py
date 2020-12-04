from typing import List

from aocpuzzle import AoCPuzzle


class Puzzle04(AoCPuzzle):
    def common(self, input_data: List[str]) -> None:
        self.required_fields = {
            'byr': lambda x: int(x) and len(x) == 4 and 1920 <= int(x) <= 2002,
            'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
            'eyr': lambda x: int(x) and len(x) == 4 and 2020 <= int(x) <= 2030,
            'hcl': lambda x: x[0] == '#' and all(v in '1234567890abcdef' for v in x[1:]),
            'hgt': lambda x: x[:-2] != '' and int(x[:-2]) and x[-2:] in ['cm', 'in'] and (
                (
                    x[-2:] == 'cm' and 150 <= int(x[:-2]) <= 193
                ) or (
                    x[-2:] == 'in' and 59 <= int(x[:-2]) <= 76
                )
            ),
            'iyr': lambda x: int(x) and len(x) == 4 and 2010 <= int(x) <= 2020,
            'pid': lambda x: int(x) and len(x) == 9,
        }
        self.passports = []
        input_data = ('\n'.join(input_data)).split('\n\n')

        for line in input_data:
            parts = line.replace('\n', ' ').split(' ')
            passport = {}

            for part in parts:
                field, value = part.split(':')
                passport[field] = value

            self.passports.append(passport)

    def part1(self, input_data: List[str]) -> int:
        valid_passports = 0

        for passport in self.passports:
            valid_passports += all([
                field in passport
                for field in self.required_fields
            ]) is True

        return valid_passports

    def part2(self, input_data: List[str]) -> int:
        valid_passports = 0

        for passport in self.passports:
            for field, validator in self.required_fields.items():
                try:
                    if field not in passport or validator(passport[field]) is False:
                        break
                except ValueError:
                    break
            else:
                valid_passports += 1

        return valid_passports

    def test_cases(self, input_data: List[str]) -> int:
        part1_tests = [
            'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd',
            'byr:1937 iyr:2017 cid:147 hgt:183cm',
            '',
            'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884',
            'hcl:#cfa07d byr:1929',
            '',
            'hcl:#ae17e1 iyr:2013',
            'eyr:2024',
            'ecl:brn pid:760753108 byr:1931',
            'hgt:179cm',
            '',
            'hcl:#cfa07d eyr:2025 pid:166559648',
            'iyr:2011 ecl:brn hgt:59in',
        ]

        part2_tests = [
            'eyr:1972 cid:100',
            'hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926',
            '',
            'iyr:2019',
            'hcl:#602927 eyr:1967 hgt:170cm',
            'ecl:grn pid:012533040 byr:1946',
            '',
            'hcl:dab227 iyr:2012',
            'ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277',
            '',
            'hgt:59cm ecl:zzz',
            'eyr:2038 hcl:74454a iyr:2023',
            'pid:3556412378 byr:2007',
            '',
            'pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980',
            'hcl:#623a2f',
            '',
            'eyr:2029 ecl:blu cid:129 byr:1989',
            'iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm',
            '',
            'hcl:#888785',
            'hgt:164cm byr:2001 iyr:2015 cid:88',
            'pid:545766238 ecl:hzl',
            'eyr:2022',
            '',
            'iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719',
        ]
        total_tests = 0

        self.common(part1_tests)
        total_tests += len(self.passports)
        assert self.part1(part1_tests) == 2

        self.common(input_data)
        assert self.part1(input_data) == 233

        self.common(part2_tests)
        total_tests += len(self.passports)
        assert self.part2(part2_tests) == 4

        self.common(input_data)
        assert self.part2(input_data) == 111

        total_tests += len(self.passports)

        return total_tests
