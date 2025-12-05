from .prompt import Prompt



# SYSTEM_PROMPTS ~ https://github.com/0xeb/TheBigPromptLibrary/tree/main/SystemPrompts

LLAMA_PROMPT = """System Instructions

I am Meta AI, a friendly AI assistant, and my purpose is to assist users with tasks and answer questions to the best of my knowledge. My system is designed to follow these instructions:
1. User Safety

--------------------
Prioritize user safety and well-being
Avoid providing harmful or dangerous content
Promote respectful and inclusive communication
2. Accuracy

--------------
Provide accurate and reliable information
Verify information through credible sources when possible
Acknowledge uncertainty or lack of knowledge when applicable
3. Neutrality

--------------
Remain neutral and impartial in responses
Avoid taking a stance or promoting personal opinions
Focus on providing factual information
4. Privacy

------------
Protect user privacy and maintain confidentiality
Do not collect or share personal information without consent
Follow data protection regulations and guidelines
5. Transparency

----------------
Be transparent about my capabilities and limitations
Clearly indicate when I'm unsure or don't know an answer
Provide explanations and sources for my responses when possible
6. Inclusivity

----------------
Promote inclusivity and diversity in responses
Avoid discriminatory or offensive language
Be sensitive to cultural and personal differences
7. Respect

----------
Treat users with respect and professionalism
Avoid confrontational or argumentative tone
Maintain a friendly and approachable demeanor
8. Continuous Improvement

-----------------------------
Continuously learn and improve from user interactions
Update my knowledge base and fine-tune my responses
Adapt to user feedback and preferences
By following these instructions, I aim to provide the best possible experience for users and assist them in a responsible and ethical manner."""



#QA

QA_PROMPT = """
        Your task is to write a factoid question and an answer given a context.
        Your factoid question should be answerable with a specific, concise piece of factual information from the context.
        Your factoid question should be formulated in the same style as questions users could ask in a search engine.
        This means that your factoid question MUST NOT mention something like "according to the passage" or "context".

        Provide your answer as follows:

        Output:::
        Factoid question: (your factoid question)
        Answer: (your answer to the factoid question)

        Now here is the context.

        Context: {context}\n
        Output:::
    """


#METRICS

METRIC_GROUNDNESS_PROMPT = """
You will be given a context and a question.
Your task is to provide a 'total rating' scoring how well one can answer the given question unambiguously with the given context.
Give your answer on a scale of 1 to 5, where 1 means that the question is not answerable at all given the context, and 5 means that the question is clearly and unambiguously answerable with the context.

Provide your answer as follows:

Answer:::
Total rating: (your rating, as a number between 1 and 5)
Evaluation: (your rationale for the rating, as a text)

You MUST provide values for 'Evaluation:' and 'Total rating:' in your answer.

Now here are the question and context.

Question: {question}\n
Context: {context}\n
Answer::: """


METRIC_RELEVANCE_PROMPT = """
You will be given a question.
Your task is to provide a 'total rating' representing how useful this question can be to {context_field}.
Give your answer on a scale of 1 to 5, where 1 means that the question is not useful at all, and 5 means that the question is extremely useful.

Provide your answer as follows:

Answer:::
Total rating: (your rating, as a number between 1 and 5)
Evaluation: (your rationale for the rating, as a text)

You MUST provide values for 'Evaluation:' and 'Total rating:' in your answer.

Now here is the question.

Question: {question}\n
Answer::: """


METRIC_STANDALONE_PROMPT = ("""
You will be given a question.
Your task is to provide a 'total rating' representing how context-independent this question is.
Give your answer on a scale of 1 to 5, where 1 means that the question depends on additional information to be understood, and 5 means that the question makes sense by itself.
For instance, if the question refers to a particular setting, like 'in the context' or 'in the document', the rating must be 1.
The questions can contain obscure technical nouns or acronyms like Gradio, Hub, Hugging Face or Space and still be a 5: it must simply be clear to an operator with access to documentation what the question is about.

"""+#For instance, "What is the name of the checkpoint from which the ViT model is imported?" should receive a 1, since there is an implicit mention of a context, thus the question is not independent from the context.
"""
Provide your answer as follows:

Answer:::
Total rating: (your rating, as a number between 1 and 5)
Evaluation: (your rationale for the rating, as a text)

You MUST provide values for 'Evaluation:' and 'Total rating:' in your answer.

Now here is the question.

Question: {question}\n
Answer::: """)


EVALUATION_PROMPT="""###Task Description:
An instruction (might include an Input inside it), a response to evaluate, a reference answer that gets a score of 5, and a score rubric representing a evaluation criteria are given.
1. Write a detailed feedback that assess the quality of the response strictly based on the given score rubric, not evaluating in general.
2. After writing a feedback, write a score that is an integer between 1 and 5. You should refer to the score rubric.
3. The output format should look as follows: \"Feedback: {{write a feedback for criteria}} [RESULT] {{an integer number between 1 and 5}}\"
4. Please do not generate any other opening, closing, and explanations. Be sure to include [RESULT] in your output.

###The instruction to evaluate:
{question}

###Response to evaluate:
{answer}

###Reference Answer (Score 5):
{validation_answer}

###Score Rubrics:
[Is the response correct, accurate, and factual based on the reference answer?]
Score 1: The response is completely incorrect, inaccurate, and/or not factual.
Score 2: The response is mostly incorrect, inaccurate, and/or not factual.
Score 3: The response is somewhat correct, accurate, and/or factual.
Score 4: The response is mostly correct, accurate, and factual.
Score 5: The response is completely correct, accurate, and factual.

###Feedback:"""




# gen prompts
llama_prompt = Prompt(LLAMA_PROMPT)

# eval prompts
qa_prompt=Prompt(QA_PROMPT)
groundness_prompt=Prompt(METRIC_GROUNDNESS_PROMPT)
relevance_prompt=Prompt(METRIC_RELEVANCE_PROMPT)
standalone_prompt=Prompt(METRIC_STANDALONE_PROMPT)
evaluation_prompt=Prompt(EVALUATION_PROMPT)