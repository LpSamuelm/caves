##What it does
`waterflow.py` simulates water flowing (only from left to right) in a cave, and was made for an excercise on Puzzlenode - see [here](http://www.puzzlenode.com/puzzles/11-hitting-rock-bottom).

##How to use
To launch, either run the script with a file as the only argument, or type in which file you'd like to perform the simulation on at the prompt that appears at the start.

Supply a file in the format seen in `simplecave.txt`. The first line should contain the number of water tiles you want to fill. The rest of the lines represent a cave (they have to be the same length, fill in with spaces for empty), with `#` representing walls, and `~` representing the starting point for water.

You can put the water starting point anywhere, but it is advised to put it along the left edge, seeing as the water will never flow to the left.

The output file (`output.txt`) will contain the cave as it would look with your specified amount of water in it, and a list  separated by spaces containing the depths of every column. A `~` here represents a column that has empty space under the water, and therefore not a measurable depth.