W= input()
t = 0

for w in W:
	match w:
		case 'A'|'B'|'C':
			t += 3
		case 'D'|'E'|'F':
			t += 4
		case 'G'|'H'|'I':
			t += 5
		case 'J'|'K'|'L':
			t += 6
		case 'M'|'N'|'O':
			t += 7
		case 'P'|'Q'|'R'|'S':
			t += 8
		case 'T'|'U'|'V':
			t += 9
		case 'W'|'X'|'Y'|'Z':
			t += 10


print(t)