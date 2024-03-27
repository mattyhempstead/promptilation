print("pcc")

from pathlib import Path

from llm import get_chat_response


def promptile(
    input_file: Path,
    output_dir: Path,
):
    print("dirs", input_file, output_dir)

    if input_file.suffix != ".promptpy":
        raise Exception("Expecting input file of type .promptpy")

    # Read input file as text
    input_file_string = input_file.read_text()
    # print(input_file_string)

    # Build prompt
    prompt = "The following is code in natural language, please convert it to python.\n"
    prompt += "```"
    prompt += input_file_string
    prompt += "```"

    print("Sending the following prompt\n\n")
    print(prompt)
    print("\n")

    # Send prompt
    chat_response = get_chat_response(
        system_message="""
            You convert a special natural language code to python.
            Place the entire output python code in a single block of ``` triple backticks.
        """,
        user_request=prompt,
        seed=0,
    )
    print(chat_response)

    # Extract code from prompt response
    chat_response_split = chat_response.split("```")
    assert len(chat_response_split) == 3

    output_code = chat_response_split[1]
    print("Output code:")
    print(output_code)

    # Write output to disk
    output_path = output_dir / (input_file.stem + ".py")
    print("Promptiling code to", output_path)

    with open(output_path, 'w') as file:
        file.write(output_code)

