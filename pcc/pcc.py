from pathlib import Path

from llm import get_chat_response
from prompt import PROMPT_SYSTEM, PROMPT_USER


def promptile(
    input_file: Path,
    output_dir: Path,
):
    # Check if the input file parameter is provided
    if not input_file:
        raise ValueError("Error: '--input-file' argument is required")

    # Print both input file and output directory
    print(f"Input file:\n\t{input_file}")
    if input_file.suffix != ".promptpy":
        raise Exception("Expecting input file of type .promptpy")
    print()

    print(f"Output directory:\n\t{output_dir}")
    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)
        print(f"Creating directory '{output_dir}' as it does not exist.")
    print()

    # Read input file as string
    input_file_string = input_file.read_text()
    # print(input_file_string)

    # Build prompt
    prompt = PROMPT_USER.format(code=input_file_string)

    # print("Sending the following prompt\n\n")
    # print(prompt)
    # print("\n")

    # Send prompt
    print("Promptiling...")
    chat_response = get_chat_response(
        system_message=PROMPT_SYSTEM,
        user_request=prompt,
        seed=0,
    )
    # print(chat_response)

    # Extract code from prompt response
    chat_response_split = chat_response.split("```")
    assert len(chat_response_split) == 3
    output_code = chat_response_split[1]

    # Remove the word python from ```python on the first line.
    assert output_code.startswith("python\n")
    output_code = output_code[len("python\n"):]

    # print("Output code:")
    # print(output_code)

    # Write output to disk
    output_path = output_dir / (input_file.stem + ".py")
    with open(output_path, 'w') as file:
        file.write(output_code)
    print(f"Saved output to\n\t{output_path}")
    print()

    print("Promptilation complete.")
