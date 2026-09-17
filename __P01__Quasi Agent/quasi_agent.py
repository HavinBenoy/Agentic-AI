from litellm import completion
import sys

def generate_response(message):

    """ Generate the responce from the model based on the chatml based prompt"""

    response = completion(
        model = "openai/gpt-4",
        messages = message,
        max_tokens = 1024
    )

    return response.choices[0].message.content



def parse_code(response):

    ''' Parse the code block from the generated response'''

    if "```" not in response:
        return response

    parsed = response.split("```")[1].strip()

    if parsed.starswith("python"):
        parsed = parsed[6:]

    return parsed



# ChatML based message
message = [{'role': 'system',
            'content': 'You are a Python expert helping to generate a function'}]



# asking the user for what kind of function they need to produce
print("Hello..\nThis is python code generator which are generate functions for specified task in a well documented manner and also will return test cases as well. ")
print("Please type in what kind of function would you like to create: ")
func_required = input().strip()

# Now appending the user requirement into the message

message.append({
    'role': 'user',
    'content': f'Generate a function for {func_required} . Use modular and optimal coding approach . Output the function within a ``` python code block```.' 
})

# Generating the response :

function_result = generate_response(message)

# Parsing the code out of the respose
parsed_code = parse_code(function_result)

print("=================== Function result ==========================")

print(parsed_code)

# Adding the response into the chatml message

message.append({
    'role': 'assistant',
    'content': "\`\`\`python\n\n" + parsed_code + "\n\n\`\`\`"
})

# =================================  Second stage  ===================================================

# Now adding the instruction for adding documentation into the code .

message.append({
    'role': 'user',
    'content': 'Add comprehensive documentation to this function , including description, parameters, return values, examples and edge cases. output the function in a ``` python code block```.'
})

documented_code = generate_response(message)
parsed_code = parsed_code(documented_code)

print("=================== Documented code =========================")

print(parsed_code)

# adding the documnted code result into the chatml message list

message.append({
    'role': 'assistant',
    'content': "\`\`\`python\n\n" + parsed_code + "\n\n\`\`\`"
})

# =================================  Third stage  ===================================================

# Now adding the instruction generating the unit test cases .

message.append({
    'role': 'user',
    'content': 'add unittest test cases for this function including , tests for basic functionality , edge cases , error cases , and various input scenarios.output the function in a ``` python code block```.'
})

test_cases = generate_response(message)
test_cases_parsed = parsed_code(documented_code)

print("=================== unittest test cases =========================")

print(test_cases_parsed)

# adding the documnted code result into the chatml message list

message.append({
    'role': 'assistant',
    'content': test_cases_parsed
})


# =============================== Saving the result into a python file ======================================


file_name = func_required.lower()
file_name = ''.join(i for i in file_name if i.isalnum() or i.isspace())
file_name = file_name.replace(" ", "_")[:30].strip() + ".py"

# Write the file content and save 

with open(file_name, 'w') as f:
    f.write(parsed_code + "\n\n" + test_cases_parsed)

print(f'File is saved with the name : {file_name}')