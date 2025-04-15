import pandas as pd
import os
import json

from langchain_ollama.llms import OllamaLLM
from langchain.prompts import ChatPromptTemplate

from prompts.template import TEMPLATE
from prompts.few_shot import create_few_shot_examples, few_shot_format

# Load the config file
with open('../config/config.json', 'r') as f:
    config = json.load(f)

# Load data
data_loc = config["data_loc"]

# Define file path
train_file_name = "QTL_text.json"
train_final_path = os.path.join(data_loc, train_file_name) 

# Load json file
df_train = pd.read_json(train_final_path)
df_train = df_train.drop(columns=['Journal', 'PMID'])


# Create few-shot examples
few_shot_df = create_few_shot_examples(df_train, n=2)
prompt_context = "\n".join(few_shot_df.apply(few_shot_format, axis=1).tolist())
# print("=== Few Shot Context ===\n", prompt_context)

# Initialize the model
model = OllamaLLM(model="llama3.2")

# Define the prompt template
prompt = ChatPromptTemplate.from_template(TEMPLATE)

# Create the chain
chain = prompt | model 

# Run one example
row = df_train.iloc[1]
result = chain.invoke({
        "prompt_context": prompt_context,
        "Abstract": row["Abstract"],
        "Title": row["Title"]
        })

# Output
formatted_prompt = prompt.format_messages(
    prompt_context=prompt_context,
    Abstract=row["Abstract"],
    Title=row["Title"]
)

print("=== Prompt Sent ===\n", formatted_prompt[0].content, "\n")

print("=== Result ===\n", result)