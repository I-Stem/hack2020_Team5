
import pandas as pd
from ast import literal_eval

from cdqa.utils.filters import filter_paragraphs
from cdqa.utils.download import download_model, download_bnpp_data
from cdqa.pipeline.cdqa_sklearn import QAPipeline


cdqa_pipeline = QAPipeline(reader='models/bert_qa.joblib')
text_data = []
with open("goods.txt") as f:
    text_data.append(f.readlines())



data_df = pd.DataFrame(text_data[0],columns = ["data"])
data_df.to_csv("text.csv")
new_data = pd.read_csv("text.csv",converters={'paragraphs': literal_eval})
print(new_data.head())
data = filter_paragraphs(new_data["data"])
cdqa_pipeline.fit_retriever(new_data.data)
query = "what is spatiotemporal data"
predicted = sdqa_pipeline.predict(X=query)
print(predicted)
print("done")
