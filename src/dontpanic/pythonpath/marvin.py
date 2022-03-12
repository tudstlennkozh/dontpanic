import string

all_phrases = (
	"The Ultimate Question of Life, the Universe and Everything",  # en
	"La grande question sur la vie, l'univers et le reste",  # fr
	"Das Leben, das Universum und der ganze Rest"  # de
)


def remove_delimiters(delimiters: iter, s: str) -> list:
	new_s = s
	for i in delimiters:
		new_s = new_s.replace(i, ' ')
	return new_s.split()


def prepare_sentence(s: str) -> frozenset:
	return frozenset(remove_delimiters(string.punctuation, s.lower()))


def close_to(s1: frozenset, s2: frozenset) -> float:
	return len(s1.intersection(s2)) / len(s2)


all_sets = [prepare_sentence(s) for s in all_phrases]


def check_question(q: str, tolerance: float) -> bool:
	""" will return True if the question is correctly put, i.e. related to h2g2 """
	if tolerance > 1.0:
		tolerance = 1.0

	qfset = prepare_sentence(q)

	for sentence in all_sets:
		if close_to(qfset, sentence) >= tolerance:
			return True
	return False
