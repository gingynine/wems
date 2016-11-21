# Put your commands here
COMMAND1 = "name twenty breeds of dogs"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "snouser, terrier, English lab, yellow lab, greyhound, chocolate lab, wolf, pig, bulldog, and more."
        
    return response

