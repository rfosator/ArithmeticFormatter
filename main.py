from arithmetic_arranger import arithmetic_arranger

if __name__ == "__main__":
  try:
    arithmetic_arranger(
      ["32 + 698", "3801 - 2", "40 - 43", "123 + 49", "5489 - 8632"], True)
  except Exception as error:
    print(error)
