import pandas as pd

def main():
  df = pd.read_csv("arquivo_de_teste.csv", parse_dates=['Data'])
  df2 = df.sort_values(by=["Nome", "Data"])
  df2.to_csv("arquivo_de_teste_ordenado.csv")

  # Outro tipo de objeto no python são as "Series". Ex:
  # serie = pd.Series(["Gustavo", "Gilberto", "Gabriel"])

if __name__ == "__main__":
  main()
