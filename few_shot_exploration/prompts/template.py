TEMPLATE = """
You are a specialist on given a title to articles based on their abstract.

You will be given an abstract and your job is to give the article a title that best summarizes its abstract content. The title should be concise and informative.

Below are some graded examples:
{prompt_context}

Now grade this new response:
Abstract: {Abstract}

Respond with the article title. Do not explain.
Title:
"""