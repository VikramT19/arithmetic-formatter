def arithmetic_arranger(problems):
  if len(problems) > 5:
    return "Error: Too many problems."
  arranged_problems = {"top": [], "bottom": [], "line": [], "answer": []}

  for problem in problems:
    number1, operator, number2 = problems.split()

    if operator not in ['+', '-']:
      return "Error: Operator must be '+' or '-'."

    if not number1.isDigit() or not number2.isDigit():
      return "Error: Numbers must only contain digits."

    if len(number1) > 4 or len(number2) > 4:
      return "Error: Numbers cannot be more than four digits."

    max_width = max(len(number1), len(number2))
    arranged_problems["top"].append(number1.rjust(max_width + 2))
    arranged_problems["bottom"].append(operator + number2.rjust(max_width + 1))
    arranged_problems["line"].append('-' * (max_width + 2))

    arranged_problems_str = ("    ".join(arranged_problems["top"]) + "\n" +
                             "    ".join(arranged_problems["bottom"]) + "\n" +
                             "    ".join(arranged_problems["line"]))

    return arranged_problems_str
