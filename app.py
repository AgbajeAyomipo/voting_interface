import gradio as gr

def run():
    title = "<h1>Vote For Your Preferred Candidates</h1>"
    title_2 = "<h2>Vote Wisely</h2>"
    description = "<h3><b>Verify Your Identity</b></h3> First, enter your matric number and name in the designated fields(We trust that before you gained access to this page, you must have done this). Our system will verify your identity and ensure you are eligible to vote.\
                \
                <h3><b>Select Your Candidate</b></h3> Once verified, you will be presented with a dropdown menu containing the names of all eligible candidates. Simply select the candidate of your choice by clicking on their name.\
                <h3><b>Confirm Your Selection</b></h3> Review your selection carefully and confirm your choice."

    names1 = [
        "Adebayo Oladimeji", "Okoro Emmanuel", "Nwosu Chukwuemeka", "Ogunyemi Olamide", "Adeyemi Abiodun", "Eze Chidinma", "Okeke Ifeanyi", "Akindele Oluwaseun", "Onyeka Nneoma", "Ibezim Chukwudi"
    ]
    names2 = [
        "Ojo Oluwafemi", "Njoku Chidiebere", "Okafor Uchechukwu", "Afolabi Oluwatoyin", "Ekeh Chukwuemeka", "Okonkwo Chukwuma", "Ogunbiyi Olamide", "Akanbi Oluwaseun", "Nwosu Chukwuemeka", "Okeke Ifeanyi"
    ]
    names3 = [
        "Nwosu Chukwuemeka", "Okeke Ifeanyi", "Adebayo Oladimeji", "Eze Chidinma", "Ojo Oluwafemi", "Ibezim Chukwudi", "Okafor Uchechukwu", "Afolabi Oluwatoyin", "Ekeh Chukwuemeka", "Okonkwo Chukwuma"
    ]
    def ui_fn(a = [f"Candidate {i+0}" for i in range(1,5)], b = [f"Candidate {i+0}" for i in range(1,5)], c = [f"Candidate {i+0}" for i in range(1,5)], \
            d = [f"Candidate {i+0}" for i in range(1,5)], e = [f"Candidate {i+0}" for i in range(1,5)]):
        return "Congrats, Your votes have been Saved and recorded"


    with gr.Blocks(title = title) as demo:
        gr.Markdown(title)
        gr.Markdown(title_2)
        gr.Markdown(description)
        with gr.Row(equal_height = False):
            # pos_1 = gr.TextArea(placeholder = "Input Matric Number in the format (DEPT/YY/NNNN) here:", label = "Position 1: President")
            rad_1 = gr.Dropdown(choices = [""] + names1[:5], info = "Select just one Candidate", multiselect=False, label = "Position 1: President")
        with gr.Row(equal_height = False):
            # pos_2 = gr.TextArea(placeholder = "Input your name here", label = "Position 2: Vice President")
            rad_2 = gr.Dropdown(choices = [""] + names1[5:], info = "Select just one Candidate", multiselect=False, label = "Position 2: Vice President")
        with gr.Row(equal_height = False):
            # pos_3 = gr.TextArea(placeholder = "", label = "Position 3: General Secretary)
            rad_3 = gr.Dropdown(choices = [""] + names2[:5], info = "Select just one Candidate", multiselect=False, label = "Position 3: Treasurer")
        with gr.Row(equal_height = False):
            # pos_4 = gr.TextArea(placeholder = "Input your name here", label = "Student Name".upper())
            rad_4 = gr.Dropdown(choices = [""] + names2[5:], info = "Select just one Candidate", multiselect=False, label = "Position 4: General Secretary")
        with gr.Row(equal_height = False):
            # pos_5 = gr.TextArea(placeholder = "Input Matric Number in the format (DEPT/YY/NNNN) here:", label = "MATRIC NO")
            rad_5 = gr.Dropdown(choices = [""] + names3[:5], info = "Select just one Candidate", multiselect=False, label = "Position 5: Assistant General Secretary")
        output1 = gr.TextArea(placeholder = "Your Voting Status is here", label = "Voting Status", lines = 1)
        btn = gr.Button('Submit Vote')
        btn.click(fn = ui_fn, inputs = [rad_1, rad_2, rad_3, rad_4, rad_5], outputs = [output1])
    
    demo.launch(share = False)

if __name__ == "__main__":
    run()