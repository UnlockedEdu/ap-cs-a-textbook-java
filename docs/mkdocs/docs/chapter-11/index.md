# Chapter 11
As Uncle Ben said to Spider-Man "With great data, comes great storage," or something like that.
So the question has remained, how do you deal with a dynamic amount of information.
Consider the very broad idea of a situation where you must consider large amounts of information, and refer back to it.
If the amount of information changes every time the program runs, you are unable to hard-code the correct number of variables.
So you only option is to have a dynamic amount of variables.

Now imagine the scenario of storing books someplace. How much room you will need depends on how many books you are, and once you now that, you can create a place to store them.
This works in the same way in computer science, but instead of books, we have raw data. If we can determine how much raw data we ahve at the begining of a program, we can create the space to store the data.
And this is the power of an array.
An array allows us to store a large amount of data, however upon creation of an array, it cannot change.
Imagine a bookshelf, which, once created, has an upper limit on to how many books it can actually hold, but if you want to store less than that amount, you are able to.
This is the same situation for an array, you can create an array of a specific size, and then you are able to store that much data or less.
But how does one create an array.
In java it is quite simple, you simply write int[] array = new int[7];
Well, not exactly that, but very close. That is an example of a properly initialized array, but only one that can store 7 ints.
Lets start merging the real world example with code.
Lets say I am trying to build a bookcase that can hold 40 books.
If I was to write that in code I would type Book[] bookcase = new Book[40];
As can be seen, arrays are initialized by the formula DataType[] variableName = new DataType[Size];
The DataType tells us exactly what information can be stored inside of the array, so in example one, only ints could be stored.
The variableName is whatever you wish to call you Array so that you may use the data later, so in the second example, our variableName was bookcase.
And the Size tells us exactly how big our array is, in the first example it was 7, in the second example it was 40.

So we know how to create an array. Yippe. This is useless to us until we are able to fill it with data however.
Believe it or not, once a bookcase is created, the books do not magically get shelved, we still have to do that.
So how do we shelve the books?
Well first we must have something to shelve.
So using the bookcase example, lets go write a little bit of code and explain it.
	Book[] bookcase = new Book[40];
	Book HarryPotter1 = new Book("Harry Potter and the Sorcerer's Stone");
	bookcase[0] = HarryPotter1;
Now, what exactly is going on here.
First, we have the initialization(creation) of our array, which was explained prior.
Next, we are creating a Book.
Finally, we are shelving the Book int the bookcase at the position 0.
Well, that clearly must be wrong because you can't label a position 0 can you?
As it turns out, in Computer Science, counting starts at 0. Do not forget this, as it will trip you up countless times otherwise.
Golden rule of Computer Science, if you remember anything, always remember that you start counting at 0.
Ok, so we start shelving at 0, and we can shelve 40 books. So we can shelve a book anywhere in the range of 0-40 correct? Wrong.
Well, ok, almost right. Yes, it is possible to shelve a book anywhere inside of an array, it is not required that you shelve sequentially, with the first being at 0, and the second being at 1. However the range is not 0-40. It is 0-39 because we start counting at 0. So everything is shifted to the left by 1.

So we have all the information stored now. How do we get it back.
As it turns out, getting your information back from an array is basically the opposite of putting it into an array.
Continuing from the previous code segment
	Book alsoTheFirstHarryPotter = bookcase[0];
Just like how you assign things everywhere else
A good way to think of it is as if the array is just a bunch of variables.
Instead of typing
	int var1 = 7;
	int var2 = 5;
	int var3 = 11;
We can type
	int[] var = new int[3];
	var[0] = 7;
	var[1] = 5;
	var[2] = 11;
But wait, I just typed more characters to do the same thing, thats worthless.
//***
You forgot this dummy int[] newCoolStuff = {3, 1, 7};

***//
Ok, I admit, in this specific case, yea, you wasted keystrokes.
But lets imagine that you knew you were going to be given a list of numbers, preceded by a number indicating how many numbers are in the list. Example,
	4
	1 5 8 4
What could we type then.
Well, using our good old input reading we might be able to do something like this.
	Scanner keyboard = new Scanner(System.in);
	int num = keyboard.nextInt();
	int[] numbers = new int[num];
	for(int x = 0; x < num; x++)
	{
		numbers[x] = keyboard.nextInt();
	}
Ta-da! We have added all the numbers to the list.
What? Thats still more keystrokes than doing it the previous way? But what about how dynamic it is! This way works for any amount of numbers! Imagine having to write a program to handle the data set below without an array.
	42
	5 8 9 1 0 6 4 9 1 5 1 1 0 2 7 7 1 7 8 9 3 3 0 3 8 6 1 3 3 2 1 9 7 5 3 0 1 9 6 2 3 9
Suddenly seems like a much more daunting task doesn't it? Well good thing we have that code above that works for every amount of numbers.
Now you can handle any array that comes your way! Well, as long as you remember some very common methods. Such as, the .length method. Slap this method onto the end of your variableName and you can get how long the array is!
	System.out.println(bookcase.length); (40)
The Arrays.sort method. Use this method if you want your data sorted from least to greatest.
	Arrays.sort(bookcase);
Wait... what defines the greatest book, besides the fact that the greatest book ever written was the Lord of the Rings, but how do you determine which books are greater than other books? For more information on this, go see Chapter 17: Searching and Sorting.
But for now, lets just do an easier to sort.
	Arrays.sort(newCoolStuff);
	for(int x = 0; x < newCoolStuff.length; x++)
		System.out.println(newCoolStuff[x]);
	(1 3 7)
Its easy to determine lesser than and greater than for numbers, 1 is less than 3, 1 is less than 7, and 3 is less than 7, so now we have the sorted 1 3 7!

2D arrays.

	
