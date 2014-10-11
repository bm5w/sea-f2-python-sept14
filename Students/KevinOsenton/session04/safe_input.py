def safe_input():
    try:
        return raw_input("Something goes here: ")
    except (EOFError, KeyboardInterrupt):
        return None
if __name__ == '__main__':
    print safe_input()