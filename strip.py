def extract_username(instagram_url):
    # If the URL contains a pipe, split by it first
    if "|" in instagram_url:
        url_part = instagram_url.split("|")[0]  # Extract the URL part before the pipe
    else:
        url_part = instagram_url

    # Extract the username part from the URL
    return url_part.split("/")[-2]

def process_file(input_filename, output_filename):
    usernames = []
    
    # Open the input file and read line by line
    with open(input_filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace characters like \n
            line = line.strip()
            # Extract username from each line
            username = extract_username(line)
            usernames.append(username)
    
    # Write the extracted usernames to the output file
    with open(output_filename, 'w') as output_file:
        for username in usernames:
            output_file.write(username + '\n')  # Write each username on a new line

# Example usage
input_filename = 'followers.txt'  # Replace with the name of your input file
output_filename = 'processedfollowers.txt'  # Replace with the desired output file name

# Process the input file and store the output in the new text file
process_file(input_filename, output_filename)
