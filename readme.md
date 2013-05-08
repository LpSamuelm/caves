##What it does
`waterflow.py` simulates water flowing (only from left to right) in a cave, and was made for an excercise on Puzzlenode - see [here](http://www.puzzlenode.com/puzzles/11-hitting-rock-bottom).

`waterflow-excerciseonly.py` does the same thing, except optimized for the excercise and not as flexible.

##How to use
To launch, either run the script with a file and an output file as the arguments, or type in your filename choices at the prompt that appears at the start.

Supply a file in the format seen in `simplecave.txt`. The first line should contain the number of water tiles you want to fill. The rest of the lines represent a cave (they have to be the same length, fill in with spaces for empty), with `#` representing walls, and `~` representing the starting point for water.

You can put the water starting point anywhere, but it is advised to put it along the left edge, seeing as the water will never flow to the left.

The output file will contain the cave as it would look with your specified amount of water in it. A `~` here represents a column that has empty space under the water, and therefore not a measurable depth.

An output file with the suffix `-depths` will also be generated. This is a list separated by spaces containing the depths of every column.