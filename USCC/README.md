## Ultra Super Calculation Computer
You are a software engineer and the new Ultra Super Calculation Computer (USCC) has just arrived in your office to be put online for use by users at USCC Headquarters. Every day the USCC will receive tons of data in the form of binary numbers and it is expected to perform specific calculations on this data but no one has told you how to do it!

Lucky for you, the engineers over at USCC headquarters have just sent you a copy of the Instruction Set Architecture that they are using. Finally, we can figure out what all those 1‘s and 0‘s have meant!

Your job today is to write the code for the CPU that will support the functions required by the ISA. Based on the design specification in the code editor window, you know you are asked to perform five functions:

Add
Subtract
Multiply
Divide
Display a history of calculations
These five functions will also require several other support functions to be written as well so that we can access different parts of our computer hardware. We must also be able to:

Read and split up our incoming data
Store a binary number to a register
Access what is stored in the register
Allocate some registers for a ‘history’ of our calculations
Store/Load from the history when needed
