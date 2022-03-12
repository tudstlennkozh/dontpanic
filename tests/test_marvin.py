import string

import dontpanic.pythonpath.marvin as m


def test_phrases():
    assert(m.all_phrases[0] == "The Ultimate Question of Life, the Universe and Everything")
    assert(m.all_phrases[1] == "La grande question sur la vie, l'univers et le reste")
    assert(m.all_phrases[2] == "Das Leben, das Universum und der ganze Rest")


def test_remove_delimiters():
    assert(m.remove_delimiters(string.punctuation, m.all_phrases[0]) == ['The', 'Ultimate', 'Question', 'of', 'Life', 'the', 'Universe', 'and', 'Everything'])
    assert(m.remove_delimiters(string.punctuation, "hi ! there ... !")) == ['hi', 'there']
    assert(m.remove_delimiters(string.punctuation, "Hello-man") == ['Hello', 'man'])
    assert(m.remove_delimiters(".:;,", "Hello-man") == ['Hello-man'])


def test_close_to_same_order():
    for s in m.all_sets:
        assert(m.close_to(s, s) == 1.0)


def test_close_to_different_order():
    for fs in m.all_sets:
        l = list(fs)
        l.sort()  # sure we won't have same order
        fsl = frozenset(l)
        assert(m.close_to(fsl, fs) == 1.0)


def test_close_to_almost_same():
    for s in m.all_phrases:
        res = s.lower()
        for r in ['the ', 'and ', 'das ', 'und ', 'le ', 'la ', 'et ']:
            res = res.replace(r, '')
        fss = m.prepare_sentence(s)
        fres = m.prepare_sentence(res)
        assert(m.close_to(fres, fss) >= 0.5)


def test_always_equal():
    ref = m.prepare_sentence("The Ultimate Question of Life, the Universe and Everything")

    def compare(s1: str, ref: frozenset) -> None:
        assert(m.close_to(m.prepare_sentence(s1), ref) == 1.0)

    compare("The{ Ultimate.: Question of Life, the Universe and Everything", ref)
    compare("The]]] Ultimate.:./,? Question of Life, the Universe and Everything", ref)
    compare("The\" Ultimate :-) Question of Life, , , , ,, the Universe and Everything", ref)
    compare("The~ Ultimate :-( Question of Life!!     !!, the Universe and Everything", ref)
    compare("The Ultimate ;-) Question of Life, the Universe and Everything", ref)
    compare("The Ultimate :-| Question of Life, the Universe and Everything", ref)
    compare("The Ultimate.:./!' Question of Life, the Universe and Everything", ref)
