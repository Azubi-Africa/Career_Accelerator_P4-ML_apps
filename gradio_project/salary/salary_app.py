import gradio as gr
from utils import *
import pickle

with open("ml/salary/model.pkl", "rb") as f:
    model = pickle.load(f)


# def run(dataframe):
#     pass


def run(experience, test_score, interview_score):
    return 1


df = (
    gr.Dataframe(
        headers=[
            "experience",
            "test_score",
            "interview_score",
        ],
        value=[],
    ),
)


if __name__ == "__main__":
    demo = gr.Interface(
        fn=run,
        inputs=[
            gr.Radio(["add", "subtract", "multiply", "divide"]),
            "number",
            "number",
        ],
        outputs="number",
    )
    demo.launch()
