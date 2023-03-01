import contextlib
from pathlib import Path

import gradio as gr

import modules.scripts as scripts

def PGD():
    return

class PGDScript(scripts.Script):

    def title(self):
        return "Paste Generation Data"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        
        with gr.Row(elem_id="Paste") as self.ratio_row:
            pb = gr.Button(value = "Paste Generation Data")
            with contextlib.suppress(AttributeError):
                pb.click(fn= PGD)

