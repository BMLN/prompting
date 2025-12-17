import unittest






from src.prompting import prompt










class PromptTest(unittest.TestCase):
    
    def test1(self):
        to_test = prompt.Prompt


        args = {"An empty string (but prompt)"}

        self.assertEqual(
            "An empty string (but prompt)",
            str(to_test(*args))
        )


    def test2(self):
        to_test = prompt.Prompt


        args = ["Not an empty string that is a prompt! {question}"]

        with self.assertRaises(KeyError):
            print(str(to_test(*args)))

    def test3(self):
        to_test = prompt.Prompt


        args = ["Not an empty string that is a prompt! {question}", "Can you repeat the question?"]

        self.assertEqual(
            "Not an empty string that is a prompt! Can you repeat the question?",
            str(to_test(*args))
        )
        
    def test4(self):
        to_test = prompt.Prompt


        args = ["Not an empty string that is a prompt! {question}", "Can you repeat the question?"]

        
        #test
        p = to_test(*args)
        p.set_formatter("question", lambda x: f"yes no maybe, {x}")
        self.assertEqual(
            "Not an empty string that is a prompt! yes no maybe, Can you repeat the question?",
            str(p)
        )
        