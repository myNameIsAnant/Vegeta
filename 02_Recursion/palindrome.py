def checkPalindrome(inp: str, chk: int) -> bool:
    if chk >= len(inp) // 2:
        return True
    if inp[chk] != inp[len(inp) - 1 - chk]:
        return False
    return checkPalindrome(inp, chk + 1)


if __name__ == "__main__":
    inp = "GOG"
    print(checkPalindrome(inp, 0))
