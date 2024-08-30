# Report

Please answer the questions below. Make sure to ask questions if you have them. 


For all these questions, it is recommended you open up IDLE or the python interpreter and try out the code.  You can also use the python visualizer to help you visualize the code.  You can find the visualizer here: [http://www.pythontutor.com/visualize.html#mode=edit](http://www.pythontutor.com/visualize.html#mode=edit)

1. Given the following code:
   ```python
   def check_valid(num):
       if num < 100:
           return True
       else:
           return False

   def main():
      number = int(input("Enter a number between 1 and 100: "))
      if check_valid(number):
          print("Valid")
      else:
          print("Invalid")
   ```
   a. Does the code properly check to see if the number is between 1 and 100?  If not, what is the problem?

   b. If not, go ahead and re-write the check_valid function here. You will notice, that num is a parameter of the function, and something you can use within the function itself as a variable. 
   ```python
   def check_valid(num):
      # your code here
   

   ```

   c. Now let's take a moment. Define an *edge case* using your own words. You may need to do some research on edge cases (make sure to cite sources).

   d. Now let's say you are writing a function to test if check_valid is actually correct! We can start with the following code
   ```python
   def test_check_valid():
      passed = 0
      if check_valid(50):
          passed += 1
      if check_valid(100):
          passed += 1
      if check_valid(101) == False:
          passed += 1

      print(f"Passed: {passed} of 3 tests")
   ```
   Does the code above test all the *edge* cases? If not, what is missing? 

   > Suggestion: Go ahead and copy the above code (both blocks) into a file, then load it into idle. You can run the test_check_valid() by the built in interrupter once the file is loaded. 

2. Draw a flowchart for a function that checks to make sure a number is between the range 1 and 100. Go ahead and include it in your submission. In your own words, how does the flow chart help you see edge cases?

3. Now thinking about edge cases, temp_guess.py, what would be the edge cases for the application? (btw, these are the same cases you should test your code with before submitting your code)


> Test Functions?   
> As we explore functions in Module 03, we will learn often with every function you write, you write a second (or more) function to test it. In industry, test-driven-development actually has teams write tests *first* and then they write their code. As you progress, make sure to think about how you can test your code in addition to writing your code. The process may feel slow now, but it will save you time in the long run. 


## Deeper Thinking

Assume you are writing a guessing game application in which the computer generates a random number, and you get to keep guessing until you find the number. You know the number is between 1 and 100.

* Can you come up with an algorithm to guess the correct number? As you have as many chances as possible, it is alright to do the simplest case. 
* Assuming there are 100 possible numbers, which are ordered from 1 to 100, how many guesses would it take in the worst case?
* Can you figure out an algorithm that would take less guesses in the worst case and still come up with the same answer?
  * This is challenging! do the best you can, talk with others, and no need to have the correct answer at this time - just any answer will be valid. We are more interested in your thought process.
    For example, did you try a few algorithms out on paper? Ask yourself the worst case and best case for finding the number?
  * For reference, there is a fast algorithm that is based on one of the oldest documented search algorithms in history - back to the Romans talking about how to use an address book for Rome. 
  