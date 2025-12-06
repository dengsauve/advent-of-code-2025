# 🎄🎄🎄 Advent Of Code - 2025 🎄🎄🎄
My solutions to Advent of Code 2025.

**Personal note:** I really appreciate that Eric chose to move to 12 days of Christmas = 12 challenges.
I love AoC, in fact, it's a highlight of my year. However, I always get super busy starting around
the middle of December, and never take/make the time for AoC unless I'm up super late.
So Santa hat's off to Eric for reducing my fomo and making it easier to commit to a smaller challenge.

I'm doing this year's set of challenges with Python, which has introduced its own set of challenges coming from being a Ruby stan for the last few years of AoC.

# 📝 Notes on Various Days
Adding my notes on approaches for various days where I was pleased with how well my solution worked.

## Day 3
I had an intuitive feeling for part 1 that took me a minute to port to part 2:

- If I'm making the biggest possible 2 digit number, then the tens column must be the largest number out of all numbers except the last one.
- The ones column must then be the largest number out of the numbers in the set after the number chosen for the tens column
- If there's a tie for the largest number for the tens column, take the earliest one in the array.

I feel like there's a more formal way to put that, and I needed to wrap my head around it for part 2.
Part 2 called for making the highest value 12 digit number from a fixed ordered list of 15 numbers (in the example).

So I figured:
- Given 15 numbers in a fixed order (for the example)
- All 12 digits had to be in order, no picking and choosing
- Then my first digit could only be chosen from the first four numbers in the 15 number set
- Tiebreaker logic (take the earliest) still applied
- All following digits must then be chosen from the remaining first _n_ numbers of the remaining set

This turned out to scale well for the 100 digit long strings provided in the problem input (oh, and there are 200 of them, not 4)

### Brute Force
So I could definitely see a possibility of brute force, where for part 1 someone would make all possible numbers, put them in an array, and get the max value of that array.
Given 4 15 digit strings in the example, then 2 of 15, and 12 of 15 - well, it seems like that'd be fine.

It breaks down when you get 200 100 digit strings, where there are:
- 4,950 2 digit combinations per line. x200 lines = 990,000 possibilities. Possible still.
- 1,050,421,051,106,700 12 digit combinations per line. x200 lines = 210,084,210,221,340,000 possibilities. That ain't gonna fly.

So kudos again to Eric for making a thought provoking exercise that tempts brute force, but requires more than that.

## Day 4
Fairly straightfoward check, though I did have to rework checking for blank spaces instead of checking for occupied spaces.

Part 2, recursion is king, just keep calling the method and returning a modified floor and a count of how many rolls were removed until that amount returned is 0.

Took me, what, 15 minutes in total, including a break to grab water while mulling the recursion.

## Day 6
Decided to finally write some helpers:
- handy dandy 2d array rotation (something that comes out of the box w/ruby smh).
- is_int checker, also out of the box w/ruby

Part 1 was fairly straightfoward:
- Make a 2d array of input, split on newlines
- Split each row on spaces and then rotate
- Pop and store the operator
- Map the remaining array to ints
- Apply the operator to the row and add to the total
- Part 1 done

Part 2 took me a second, until I realized the key was in parsing the last row to get an array of column lengths.

This allowed me to parse the strings with character spacing intact.

From there:
- Rotate the array
- Pop and store the operator
- Iterate over the strings, bringing in the last char to a num string (omitting if a space)
- Apply the operator, add to the total sum
- Part 2 done

*Day 6 notes may be a little fuzzy, it's midnight 30 after an evening on the town with my fiancee*