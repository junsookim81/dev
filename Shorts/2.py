import gradio as gr

def greet(name, is_morning, temperature, age):
    salutation = "Good morning" if is_morning else "Good evening"
    greeting = f"{salutation} {name}. It is {temperature} degrees today"
    celsius = (temperature - 32) * 5 / 9
    howold = "your age is " +age
    return greeting, round(celsius, 2), howold

demo = gr.Interface(
    fn=greet,
    inputs=["text", "checkbox", gr.Slider(0, 100), "text"],
    outputs=["text", "number", "text"],
)
demo.launch()