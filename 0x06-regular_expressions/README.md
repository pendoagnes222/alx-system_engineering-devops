# Regular Expressions
For this project I am learning how to build regular expressions using `Oniguruma`, a regular expression library which is used by `Ruby` by default.

## Tasks
* **0. Simply matching School**
	* [0-simply_match_school.rb](./0-simply_match_school.rb): Ruby script that accepts one argument and pass it to a regular expression matching method.
	* The regex must match `School

| Test string:	| Match result:  |
|---------------|----------------|
| School	| `School`  	 |
| school	| school  	 |
| Sch0ol	| Sch0ol  	 |
| aaahSchool	| aaah`School` 	 |
| Schoolaaa	| `School`aaa  	 |


* **1. Repetition Token #0**
	* [1-repetition_token_0.rb](./1-repetition_token_0.rb): Ruby script that accepts one argument and pass it to a regular expression matching method.
	* Find the regex that will match the below cases:

| Test string:	| Match result:  |
|---------------|----------------|
| hbn 		| hbn 	  	 |
| hbtn 		| hbtn 	  	 |
| hbttn 	| `hbttn` 	 |
| hbtttn 	| `hbtttn` 	 |
| hbttttn 	| `hbttttn` 	 |
| hbtttttn 	| `hbtttttn` 	 |
| hbttttttn 	| hbttttttn 	 |


* **2. Repetition Token #1**
	* [2-repetition_token_1.rb](./2-repetition_token_1.rb): Ruby script that accepts one argument and pass it to a regular expression matching method.
	* Find the regular expression that will match the below cases:

| Test string:	| Match result:  |
|---------------|----------------|
| htn 		| `htn` 	 |
| hbtn 		| `hbtn` 	 |
| hbbtn 	| hbbtn 	 |
| hbbbtn 	| hbbbtn 	 |


* **3. Repetition Token #2**
	* [3-repetition_token_2.rb](./3-repetition_token_2.rb): Ruby script that accepts one argument and pass it to a regular expression matching method.
	* Find the regular expression that will match the below cases:

| Test string:	| Match result:  |
|---------------|----------------|
| hbn 		| htn 	 	 |
| hbtn 		| `hbtn` 	 |
| hbttn 	| `hbbtn` 	 |
| hbtttn 	| `hbbbtn` 	 |
| hbttttn 	| `hbbbtn` 	 |


* **4. Repetition Token #3**
	* [4-repetition_token_3.rb](./4-repetition_token_3.rb): Ruby script that accepts one argument and pass it to a regular expression matching method.
	* The regex should not contain square brackets
	* Find the regular expression that will match the below cases:

| Test string:	| Match result:  |
|---------------|----------------|
| hbn 		| `hbn`	 	 |
| hbon 		| hbon 	 	 |
| hbtn 		| `hbtn` 	 |
| hbttn		| `hbttn` 	 |
| hbtttn	| `hbtttn` 	 |
| hbttttn	| `hbttttn` 	 |


* **5. Not quite HBTN yet**
	* [5-beginning_and_end.rb](./5-beginning_and_end.rb): Ruby script that accepts one argument and pass it to a regular expression matching method.
	* Regex must be exactly matching a string that starts with `h` ends with `n` and can have any single character in between


* **6. Call me may be**
	* [6-phone_number.rb](./6-phone_number.rb): Ruby script with regex that msut match a 10 digit number

* **7. OMG WHY ARE YOU SHOUTING**
	* [7-OMG_WHY_ARE_YOU_SHOUTING.rb](./7-OMG_WHY_ARE_YOU_SHOUTING.rb): Ruby script with regex that matches only capital letters.

Author: Sangwani P Zyambo <sangwani-coder>
