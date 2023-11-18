def arithmetic_arranger(problems, show_answers=False):
  if len(problems) > 5:
      return "Error: Too many problems."

  arranged_problems = {"top": [], "bottom": [], "line": [], "answer": []}
  errors = []

  for problem in problems:
      try:
          number1, operator, number2 = problem.split()

          if operator not in ['+', '-']:
              raise ValueError("Operator must be '+' or '-.")

          if not number1.isdigit() or not number2.isdigit():
              raise ValueError("Numbers must only contain digits.")

          if len(number1) > 4 or len(number2) > 4:
              raise ValueError("Numbers cannot be more than four digits.")

          max_width = max(len(number1), len(number2)) + 2 
          arranged_problems["top"].append(number1.rjust(max_width))
          arranged_problems["bottom"].append(operator + number2.rjust(max_width - 1))
          arranged_problems["line"].append('-' * max_width)

          if show_answers:
              answer = str(eval(problem))
              arranged_problems["answer"].append(answer.rjust(max_width))

      except ValueError as e:
          errors.append(str(e))

  if errors:
      return "\n".join(errors)

  arranged_problems_str = "\n".join(
      ["    ".join(arranged_problems["top"]),
       "    ".join(arranged_problems["bottom"]),
       "    ".join(arranged_problems["line"]),])

  if show_answers:
      arranged_problems_str += "\n" + "    ".join(arranged_problems["answer"])

  return arranged_problems_str
