from openai import OpenAI

client = OpenAI()
import json
import sys

def send_openai_request(model_name="gpt-4-turbo-2024-04-09", prompt_template="{insert your prompt here}", file_path=None):
    # Read content from the file if file_path is provided
    if file_path:
        try:
            with open(file_path, 'r') as file:
                file_content = file.read()
        except FileNotFoundError:
            print("The file was not found. Please check the path and try again.")
            return
    else:
        file_content = ""

    # Replace placeholder in the prompt with the file content
    prompt = prompt_template.replace("{any text}", file_content)

    # Prepare the API request
    try:
        response = client.chat.completions.create(model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1)
        # print("Response from OpenAI:", json.dumps(response, indent=2))
        response_message = response.choices[0].message.content
        print(response_message )
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # Default values
    model = "gpt-4-turbo-2024-04-09"
    prompt = "Here is the content from the file: {any text}"
    file_path = None

    # Parse command-line arguments
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    if len(sys.argv) > 2:
        prompt = sys.argv[2]

    # Call the function with command-line arguments
    send_openai_request(model_name=model, prompt_template=prompt, file_path=file_path)