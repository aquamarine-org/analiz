from pathlib import Path


with Path("dataset.csv").open() as f:
    data = f.read().split("\n")[1:]

counter = 0
summ = 0

for line in data:
    seq = line.split(";")

    if seq[4] == "None":
        counter += 1

    summ += float(seq[3])

percentage = 100 - counter / (len(data) / 100)
index = summ / len(data)

print(f"Процент играющих в цифровые игры: {percentage}")
print(f"Средний индекс заинтересованности ЦА играми:  {index}")
