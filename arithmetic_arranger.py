import re


class Operation():

  def __init__(self, string: str):
    regex = r"\+|\-"
    match = re.search(regex, string)
    if not match:
      raise Exception("Error: Operator must be '+' or '-'.")
    self.operator = match.group()

    values = string.split(self.operator)
    self.__validate_len__(values[0])
    self.__validate_len__(values[1])

    try:
      self.val1 = int(values[0])
      self.val2 = int("{}{}".format(self.operator, values[1].lstrip()))
    except ValueError:
      raise Exception("Error: Numbers must only contain digits.")

    self.result = self.val1 + self.val2

  def __validate_len__(self, value: str):
    if len(value.lstrip().rstrip()) > 4:
      raise Exception("Error: Numbers cannot be more than four digits.")

  def __str__(self):
    val1 = str(self.val1).rjust(5, " ")
    val2 = str(abs(self.val2)).rjust(5, " ")
    result = str(self.result).rjust(6, " ")
    return " {}\n{}{}\n------\n{}".format(val1, self.operator, val2, result)


def arithmetic_arranger(list: list[str], result: bool = False):
  if len(list) > 5:
    raise Exception("Error: Too many problems.")

  op_list = []
  for item in list:
    op_list.append(Operation(item))

  first_line = []
  second_line = []
  third_line = []
  fourth_line = []
  for op in op_list:
    first_line.append(str(op.val1).rjust(7, " "))
    second_line.append(" {}{}".format(op.operator,
                                      str(abs(op.val2)).rjust(5, " ")))
    third_line.append(" ------")
    fourth_line.append(str(op.result).rjust(7, " "))

  print(" ".join(first_line))
  print(" ".join(second_line))
  print(" ".join(third_line))
  if result:
    print(" ".join(fourth_line))
