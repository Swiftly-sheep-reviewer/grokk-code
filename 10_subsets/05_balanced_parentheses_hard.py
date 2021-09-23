def generate_valid_parentheses(num):
    result = []

    # TODO: Write your code here
    def helper(open_paren, close_paren, paren_str):
        if open_paren == 0 and close_paren == 0:
            result.append(paren_str)
        if open_paren > 0:
            helper(open_paren - 1, close_paren, paren_str + "(")
        if open_paren < close_paren:
            helper(open_paren, close_paren - 1, paren_str + ")")

    helper(num, num, "")
    return result


def main():
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(2)))
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(3)))


if __name__ == "__main__":
    main()
