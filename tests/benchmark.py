from timeit import timeit
import re
import string
import dontpanic.pythonpath.marvin as m


def remove_delimiters(delimiters, s):
    new_s = s
    for i in delimiters:
        new_s = new_s.replace(i, ' ')
    return ' '.join(new_s.split())


def regexpr(s):
    return ' '.join(w for w in re.split(r'\W', s) if w)


def join2(remove_chars, s):
    return ''.join(i for i in s if not (i in remove_chars))


def translate(table, s):
    return ' '.join(s.translate(table).split())


def join_filter(remove_chars, s):
    return ''.join((filter(lambda i: i not in remove_chars, s)))


delete_dict = {sp_character: '' for sp_character in string.punctuation}
# delete_dict[' '] = ''
table = str.maketrans(delete_dict)


def global_time(remove_chars, loops, sd, label=None):
    def time_python_code(code):
        print(code)
        total = timeit(code, number=loops, globals=globals())
        print(f"{total} sec. {total / loops:.10f} sec. per loop")
        sd[f"{label} ({loops}): {code}"] = total / loops

    if label is None:
        label = str(type(remove_chars))

    print(("-" * 8 + "*") * 8)
    print(f"Testing on {label}")
    print(remove_chars)
    for i in range(3):
        time_python_code(f"remove_delimiters(remove_chars, m.all_phrases[{i}])")
        time_python_code(f"join2(remove_chars, m.all_phrases[{i}])")
        time_python_code(f"translate(table, s)")
        time_python_code(f"join_filter(remove_chars, m.all_phrases[{i}])")


if __name__ == "__main__":

    remove_chars = string.punctuation

    # first check it runs correctly
    s = m.all_phrases[0]
    assert(remove_delimiters(remove_chars, s) == "The Ultimate Question of Life the Universe and Everything")
    # print(regexpr(s)) -> The Ultimate Question of Life, the Universe and Everything
    assert(remove_delimiters(remove_chars, s) == join2(remove_chars, s))
    assert(join2(remove_chars, s) == translate(table, s))
    assert(translate(table, s) == join_filter(remove_chars, s))

    # then time it

    list_remove_chars = [i for i in remove_chars]
    fz_remove_chars = frozenset(list_remove_chars)
    sorted_list = list_remove_chars
    sorted_list.sort()
    sd = dict()

    for l in [10000, 100000]:  # [10000,100000,1000000]:
        loops = l
        print(f"{l} loops ...")
        global_time(remove_chars, l, sd)
        global_time(list_remove_chars, l , sd)
        global_time(fz_remove_chars, l, sd)
        global_time(sorted_list, l, sd, "sorted list")

    print("---\nBest results are for :")
    sorted_dict = sorted(sd, key=sd.__getitem__)
    for res in sorted_dict[:8]:
        print(f"{res} {sd[res]:.10f}")
