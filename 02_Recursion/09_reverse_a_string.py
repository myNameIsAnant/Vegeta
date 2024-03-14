def revString(userstring: str, revstring: str = "") -> str:
    if not userstring:
        return revstring
    return revString(userstring[:-1], revstring + userstring[-1])


if __name__ == "__main__":
    print(revString("esaelp siht esrever"))
