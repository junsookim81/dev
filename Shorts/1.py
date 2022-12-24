import gradio

def greet(name) :
    return 'hi, '+name
    
app=gradio.Interface(
    inputs=gradio.Textbox(lines=2, placeholder="Name Here..."),
    fn=greet,
    outputs="text"

)

app.launch(share=True)
