def reverse_slice(text):
    return text[::-1]


def reverse_loop(text):
    result = ""
    for char in text:
        result = char + result
    return result


def reverse_builtin(text):
    return "".join(reversed(text))


if __name__ == "__main__":
    for sample in ["Python", "Hello, World!", "Привіт, світе", ""]:
        print(f"Початковий рядок : {sample!r}")
        print(f"  зріз [::-1]    : {reverse_slice(sample)!r}")
        print(f"  цикл for       : {reverse_loop(sample)!r}")
        print(f"  reversed+join  : {reverse_builtin(sample)!r}")
