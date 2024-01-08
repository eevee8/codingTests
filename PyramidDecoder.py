# Get the last number of the pyramid lines
def get_pyramid_nums(nums):
    ends = []
    step = 1
    while len(nums) != 0:
        print(nums)
        if len(nums) >= step:
            ends.append(nums[step-1])
            nums = nums[step:]
            step += 1
        else:
            nums=[]
    return ends

#Decode a message froom a file    
def decode(message_file):
    word_keys = {}
    nums = []
    message = ""
    # Read the content of the file
    with open(message_file, 'r') as file:
        lines = file.readlines()
    # Get the numbers and words
    for line in lines:
        num = int(line.split()[0])
        nums.append(num)
        word = line.split()[1]
        word_keys[num] = word;
    # Sort the numbers
    nums = sorted(nums)
    word_nums = get_pyramid_nums(nums)
    # Make the message
    for word_num in word_nums:
        message = message + word_keys[word_num] +" "
    return message
