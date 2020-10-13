### Challenge scammed

#### Theory
Once we netcat the server, we can enter a credit card number, on wrong number it exits.\
The level text displays the credit card number with 4 hidden digits marked as astericks(*). And we have to fill in those blanks.\
The file attached in the level text shows an algorithm, that may be useful for getting possible credit card numbers that may prune-up the search.

### Finding the correct credit card

To get the flag I bruteforced all the possible credict card numbers matching the case ``83684****0706910`` and send it to the netcat using a python code.

content = "83684"+str(num).zfill(4)+"0706910"
`zfill` was used to fill starting charactes with zeroes for numbers having less than 4 digits

Some modifications were also made in the code to display only output changes.
### Running the code

The code ran for a few minutes and the flag displayed at card number ``8368480020706910``
And the flag is ``dcrypt{cr3d1t_c4rd_sc4m}``