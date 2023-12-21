from transformers import MvpTokenizer, MvpForConditionalGeneration
from tabula import read_pdf
from tabulate import tabulate

df = read_pdf("sample.pdf", pages="all", multiple_tables=True)  # address of pdf file
# print(df)
# print("---------------")
# print(tabulate(df[0]))

def to_string(df, sep, columns):
    rows = []
    for i in range(len(df)):
        row = '|'.join([str(df.loc[i, col]) for col in columns])
        rows.append(f'{row} {sep}')

    return ''.join(rows)


result_df = []
for table in df:
    print("----------")
    result = []
    print(table)
    temp = table.columns.to_list()
    temp = ",".join(temp) + "[SEP]"
    result.append(temp)
    result.append(to_string(table, "[SEP]", columns = table.columns))
    result_df.append(result)

print(result_df)
tokenizer = MvpTokenizer.from_pretrained("models/mvp")
model = MvpForConditionalGeneration.from_pretrained("models/mtl-data-to-text")

inputs = tokenizer(
    f"Describe the following data: {result_df[-1]}",
    return_tensors="pt",
    max_length=1026,
    truncation=True,
    # max_new_tokens=512
)
generated_ids = model.generate(**inputs)
response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
print(response)