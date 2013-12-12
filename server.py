import web
import subprocess
import os
import string

urls = (
	'/', 'Home',
	'/problem_1', 'Concise',
	'/problem_2', 'Return',
	'/problem_3', 'Loop',
	'/problem_4', 'Match',
	'/problem_5', 'Closure',
	'/problem_6', 'Mut',
	'/problem_7', 'Visible',
	'/Rust_Everywhere', 'Everywhere',
	'/p1_solution', 'p1_solution',
	'/p2_solution', 'p2_solution',
	'/p3_solution', 'p3_solution',
	'/p4_solution', 'p4_solution',
	'/p5_solution', 'p5_solution',
	'/p6_solution', 'p6_solution',
	'/p7_solution', 'p7_solution'
	)

class Home:
	def GET(self):
		return """<html>
<head>
<style>body {
             background-color:#cccccc;
            }
</style>
</head>
<br>
<br>
<h1 align='center'> Welcome to the World of Rust </h1>
<br>
<br>
<h2 align='center'> Please select an exercise <br>
</h2>
<body>
<br>
<p align='center'><a href='problem_1'> 1.Make It More Concise </a> </p><br>
<p align='center'><a align='center'href='problem_2'> 2.Where Is My Return?! </a> </p><br>
<p align='center'><a align='center'href='problem_3'> 3.Loop the Loop </a></p> <br>
<p align='center'><a align='center'href='problem_4'> 4.Are We a Good Match? </a></p> <br>
<p align='center'><a align='center'href='problem_5'> 5.You need some closure... </a></p> <br>
<p align='center'><a align='center'href='problem_6'> 6.Mut it </a></p> <br>
<p align='center'><a align='center'href='problem_7'> 7.Hoos Invisible </a></p> <br>
<br>
<br>
<h2 align='center'>Or you can simply test your code with our Rust Everywhere<br></h2><br>
<br>
<p align='center'><a align='center'href='Rust_Everywhere'> Rust Everywhere </a></p> <br>
</body></html>"""

class Everywhere:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head><style>body {
             background-color:#cccccc;
            }</style></head><body>
<br>
<form method="POST" enctype="multipart/form-data" action="">
<p> Enter your code here 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Enter user input, if any, before submitting
</p> <br>
<textarea rows="20" cols="100"name='comment'>
</textarea>
<textarea rows="20" cols="100"name='input'>
</textarea>
<br>
<p> Or you code upload a file </p>
<input type="file" name="myfile" />
<br/>
<input type="submit" />
</form>
<br>
<br>
<a href='/'> Home </a>
</body></html>"""

    def POST(self):
		x = web.input(myfile={})
		data = web.input().comment
		user_input = web.input().input
		filedir = '/home/student/Rust-Everywhere'# change this to the directory you want to store the file in.
		filename = 'pig.rs'
		fname = filedir + '/' + filename
		fout = open(fname,'w') # creates the file where file should be stored
		if 'myfile' in x: # to check if the file-object is created
			if len(data) != 0:	
				fout = open(fname, 'w')
				fout.write(data)
			else:
				filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
				fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
		fout.close()

		if len(user_input) == 0:
			try:
				result = subprocess.check_output(["/usr/bin/rust", "run", fname], stderr=subprocess.STDOUT)
				os.remove(fname)
			except subprocess.CalledProcessError as e:
				return """<html>
				<br>
				<br>
				<head><style>body {
             background-color:#cccccc;
            }</style></head><body>
				<h2 align='center'> Here is your result! </h2> <br>
				<br>
				<br>
				""" + e.output + """
				<br>
				<br>
				
				<a href='/Rust_Everywhere'> Back </a> &nbsp;
				<a href='/'> Home </a>
				</body></html>"""
			else:
				return """<html>
				<br>
				<br>
				<head><style>body {
             background-color:#cccccc;
            }</style></head><body>
				<h2 align='center'> Here is your result! </h2> <br>
				<br>
				<br>
				""" + result + """
				<br>
				<br>
				<a href='/Rust_Everywhere'> Back </a> &nbsp;
				<a href='/'> Home </a>
				</body></html>"""

		else:
			p = subprocess.Popen(["/usr/bin/rust", "run", fname], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
			p.stdin.write(user_input)
			output = p.communicate()[0]
			os.remove(fname)
			return """<html>
				<br>
				<br>
				<head><style>body {
             background-color:#cccccc;
            }</style></head><body>
				<h2 align='center'> Here is your result! </h2> <br>
				<br>
				<br>
				""" + output + """
				<br>
				<br>
				
				<a href='/Rust_Everywhere'> Back </a> &nbsp;
				<a href='/'> Home </a>
				</body></html>"""
			

class Concise:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head><style>body {
             background-color:#cccccc;
            }</style></head><body>
<br>
<br>
<p align='center'> <font size='7pt'>Q1.Make It More Concise </font></p>
<br>
<br>
<br>
<p> Though it isn't apparent in all code, there is a fundamental difference between Rust's syntax and predecessors like C. <br>
Many constructs that are statements(with ";" at the end) in C are expressions(without ";" at the end) in Rust, allowing code to be more concise. <br>
For example, you might write a piece of code like this:<br>
<br>
<br>
<font color='green'>
&nbsp;&nbsp;&nbsp;&nbsp;fn main() {<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;let item = "muffin";<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;let price;<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if item == "salad" {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;price = 3.50;<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} else if item == "muffin" {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;price = 2.25;<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} else {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;price = 2.00;<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;println(fmt!("%?", price));<br>
&nbsp;&nbsp;&nbsp;&nbsp;}<br>
</font>
<br>
<br>
<font size='4pt' color='red'>How would you make the code above more concise? (for this question, you can only delete words, punctuations, or change indentations)
</font></p>
<form method="POST" enctype="multipart/form-data" action="">
<p> Enter your code here </p> <br>
<textarea rows="20" cols="100"name='comment'>
</textarea><br>
<p> Or you code upload a file </p>
<input type="file" name="myfile" />
<br/>
<input type="submit" />
</form>
<br>
<br>
<p> Don't know how to do it? No worries! Take a look at the solution and try again. </p>
<a href='/p1_solution'> Solution </a> <br>
<br>
<a href='/'> Home </a>
<br>
<br>
</body></html>"""

    def POST(self):
		x = web.input(myfile={})
		data = web.input().comment
		filedir = '/home/student/Rust-Everywhere'# change this to the directory you want to store the file in.
		filename = 'pig.rs'
		fname = filedir + '/' + filename
		fout = open(fname,'w') # creates the file where file should be stored
		user_input = ""
		if 'myfile' in x: # to check if the file-object is created
			if len(data) != 0:	
				fout = open(fname, 'w')
				fout.write(data)
			else:
				filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
				fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
		fout.close()

		try:
			result = subprocess.check_output(["/usr/bin/rust", "run", fname], stderr=subprocess.STDOUT)
			os.remove(fname)
		except subprocess.CalledProcessError as e:
		
			return """<html>
				<br>
				<br>
				<head><style>body {
             background-color:#cccccc;
            }</style></head><body>
				<h2 align='center'> Sorry. Try again! </h2> <br>
				<br>
				<br>
				""" + e.output + """
				<br>
				<br>
				<img src="http://www.cs.virginia.edu/~evans/pictures/me/08-small.png"><br>
				<br>
				<a href='/problem_1'> Back </a> &nbsp;
				<a href='/'> Home </a>
				</body></html>"""
		else:
			if result == "2.25\n":
				return """<html>
				<br>
				<br>
					<head><style>body {
             background-color:#cccccc;
            }</style></head><body>
					<h2 align='center'> Congratulations! </h2> <br>
					<br>
					<br>
					<p> Your result is: <br>
					""" + result + """
					<br>
					<br>
					Correct result is 2.25!
					</p>
					<br>
					<br>
					<img src="https://lh6.googleusercontent.com/-PZRVLY5Gsvg/Uqk1dnfUVFI/AAAAAAAAAlI/uLc-7FITZpw/w411-h548-no/photo.JPG"><br>
				<br>
					<a href='/problem_1'> Back </a> &nbsp;
					<a href='/'> Home </a>
					</body></html>"""
			else:
				return """<html>
				<br>
				<br>
					<head><style>body {
             background-color:#cccccc;
            }</style></head><body>
					<h2 align='center'> Sorry. Try again! </h2> <br>
					<br>
					<br>
					<p> Your result is: <br>
					""" + result + """
					<br>
					<br>
					Correct result is 2.25!
					</p>
					<br>
					<br>
					<img src="http://www.cs.virginia.edu/~evans/pictures/me/08-small.png"><br>
				<br>
					<a href='/problem_1'> Back </a> &nbsp;
					<a href='/'> Home </a>
					</body></html>"""



class Return:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head><style>body {
             background-color:#cccccc;
            }</style></head><body>
<br>
<br>
<p align='center'><font size='7pt'> Q2: Where Is My Return?! </font></h2>
<br>
<br>
<br>
<p> In Q1, you have learned how expression works, or at least you think you do. <br>
In Rust, basically everything that's not a declaration (declarations are let for variables; fn for functions; and any top-level <br>
named items such as traits, enum types, and static items) is an expression, including function bodies themselves!<br>
Therefore, there is usually no need for a return statement, because the result of the expression is used as the return value.<br>
Isn't this crazy...<br>
<br>
<br>
<font color='green'>
&nbsp;&nbsp;&nbsp;&nbsp;fn main() {<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if is_four(4) {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;println("It is four!");<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>
&nbsp;&nbsp;&nbsp;&nbsp;}   <br>

&nbsp;&nbsp;&nbsp;&nbsp;fn is_four(x: int) -> bool {<br>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return (x == 4);<br>
&nbsp;&nbsp;&nbsp;&nbsp;}<br>
</font>
<br>
<br>
<font size='4pt' color='red'>
Could you help me get rid of the keyword "return"? It just really bothers me...
</font>
</p>
<form method="POST" enctype="multipart/form-data" action="">
<p> Enter your code here </p> <br>
<textarea rows="20" cols="100"name='comment'>
</textarea><br>
<p> Or you code upload a file </p>
<input type="file" name="myfile" />
<br/>
<input type="submit" />
</form>
<br>
<br>
<p> Don't know how to do it? No worries! Take a look at the solution and try again. </p>
<a href='/p2_solution'> Solution </a> <br>
<br>
<a href='/'> Home </a>
<br>
<br>
</body></html>"""

    def POST(self):
		x = web.input(myfile={})
		data = web.input().comment
		filedir = '/home/student/Rust-Everywhere'# change this to the directory you want to store the file in.
		filename = 'pig.rs'
		fname = filedir + '/' + filename
		fout = open(fname,'w') # creates the file where file should be stored
		user_input = ""
		if 'myfile' in x: # to check if the file-object is created
			if len(data) != 0:	
				fout = open(fname, 'w')
				fout.write(data)
			else:
				filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
				fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
		fout.close()

		try:
			result = subprocess.check_output(["/usr/bin/rust", "run", fname], stderr=subprocess.STDOUT)
			os.remove(fname)
		except subprocess.CalledProcessError as e:
		
			return """<html>
				<br>
				<br>
				<head><style>body {
             background-color:#cccccc;
            }</style></head><body>
				<h2 align='center'> Sorry. Try again! </h2> <br>
				<br>
				<br>
				""" + e.output + """
				<br>
				<br>
				<img src="http://www.cs.virginia.edu/~evans/pictures/me/08-small.png"><br>
				<br>
				<a href='/problem_2'> Back </a> &nbsp;
				<a href='/'> Home </a>
				</body></html>"""
		else:
			if result == "It is four!\n":
				return """<html>
				<br>
				<br>
					<head><style>body {
             background-color:#cccccc;
            }</style></head><body>
					<h2 align='center'> Congratulations! </h2> <br>
					<br>
					<br>
					<p> Your result is: <br>
					""" + result + """
					<br>
					<br>
					Correct result is "It is four"!
					</p>
					<br>
					<br>
					<img src="https://lh6.googleusercontent.com/-PZRVLY5Gsvg/Uqk1dnfUVFI/AAAAAAAAAlI/uLc-7FITZpw/w411-h548-no/photo.JPG"><br>
				<br>
					<a href='/problem_2'> Back </a> &nbsp;
					<a href='/'> Home </a>
					</body></html>"""
			else:
				return """<html>
				<br>
				<br>
					<head><style>body {
             background-color:#cccccc;
            }</style></head><body>
					<h2 align='center'> Sorry. Try again! </h2> <br>
					<br>
					<br>
					<p> Your result is: <br>
					""" + result + """
					<br>
					<br>
					Correct result is "It is four"!
					</p>
					<br>
					<br>
					<img src="http://www.cs.virginia.edu/~evans/pictures/me/08-small.png"><br>
				<br>
					<a href='/problem_2'> Back </a> &nbsp;
					<a href='/'> Home </a>
					</body></html>"""


class Loop:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head><style>body {
             background-color:#cccccc;
            }</style></head><body>
<br>
<br>
<p align='center'><font size='7pt'> Q3: Loop the Loop </font></h2>
<br>
<br>
<br>
<p> In Rust, loops are a little bit different. it looks something like this: <br>
<br>
<br>
<font color='green'>
&nbsp;&nbsp;&nbsp;&nbsp;for blah in blahhh.iter() { <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//do something with "blah";<br>
&nbsp;&nbsp;&nbsp;&nbsp;}<br>
</font>
<br>
<br>
<font size='4pt' color='red'>
Now suppose you were given a vector like this:<br>
&nbsp;&nbsp;&nbsp;&nbsp;let pigs = ~[~"pig1", ~"pig2", ~"pig_little"];<br>
How would you print them out in order (note that the strings are specified by pointers)?<br>
</font>
</p>
<form method="POST" enctype="multipart/form-data" action="">
<p> Enter your code here </p> <br>
<textarea rows="20" cols="100"name='comment'>
</textarea><br>
<p> Or you code upload a file </p>
<input type="file" name="myfile" />
<br/>
<input type="submit" />
</form>
<br>
<br>
<p> Don't know how to do it? No worries! Take a look at the solution and try again. </p>
<a href='/p3_solution'> Solution </a> <br>
<br>
<a href='/'> Home </a>
<br>
<br>
</body></html>"""

    def POST(self):
		x = web.input(myfile={})
		data = web.input().comment
		filedir = '/home/student/Rust-Everywhere'# change this to the directory you want to store the file in.
		filename = 'pig.rs'
		fname = filedir + '/' + filename
		fout = open(fname,'w') # creates the file where file should be stored
		user_input = ""
		if 'myfile' in x: # to check if the file-object is created
			if len(data) != 0:	
				fout = open(fname, 'w')
				fout.write(data)
			else:
				filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
				fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
		fout.close()

		try:
			result = subprocess.check_output(["/usr/bin/rust", "run", fname], stderr=subprocess.STDOUT)
			os.remove(fname)
		except subprocess.CalledProcessError as e:
		
			return """<html>
				<br>
				<br>
				<head><style>body {
             background-color:#cccccc;
            }</style></head><body>
				<h2 align='center'> Sorry. Try again! </h2> <br>
				<br>
				<br>
				""" + e.output + """
				<br>
				<br>
				<img src="http://www.cs.virginia.edu/~evans/pictures/me/08-small.png"><br>
				<br>
				<a href='/problem_3'> Back </a> &nbsp;
				<a href='/'> Home </a>
				</body></html>"""
		else:
			if result == "pig1\npig2\npig_little\n":
				return """<html>
				<br>
				<br>
					<head><style>body {
             background-color:#cccccc;
            }</style></head><body>
					<h2 align='center'> Congratulations! </h2> <br>
					<br>
					<br>
					<p> Your result is: <br>
					""" + result + """
					<br>
					<br>
					Correct result is:<br>
					pig1&nbsp;pig2&nbsp;pig_little<br>
					</p>
					<br>
					<br>
					<img src="https://lh6.googleusercontent.com/-PZRVLY5Gsvg/Uqk1dnfUVFI/AAAAAAAAAlI/uLc-7FITZpw/w411-h548-no/photo.JPG"><br>
				<br>
					<a href='/problem_3'> Back </a> &nbsp;
					<a href='/'> Home </a>
					</body></html>"""
			else:
				return """<html>
				<br>
				<br>
					<head><style>body {
             background-color:#cccccc;
            }</style></head><body>
					<h2 align='center'> Sorry. Try again! </h2> <br>
					<br>
					<br>
					<p> Your result is: <br>
					""" + result + """
					<br>
					<br>
					Correct result is:<br>
					pig1&nbsp;pig2&nbsp;pig_little<br>
					</p>
					<br>
					<br>
					<img src="http://www.cs.virginia.edu/~evans/pictures/me/08-small.png"><br>
				<br>
					<a href='/problem_3'> Back </a> &nbsp;
					<a href='/'> Home </a>
					</body></html>"""


class Match:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head><style>body {
             background-color:#cccccc;
            }</style></head><body>
<br>
<br>
<p align='center'><font size='7pt'> Q4: Are We A Good Match? </font></h2>
<br>
<br>
<br>
<p> Rust's match construct is a generalized, cleaned-up version of C's switch construct. You provide it with a value and a number of arms, <br>
each labelled with a pattern, and the code compares the value against each pattern in order until one matches.  <br>
The matching pattern executes its corresponding arm.<br>
<br>
<br>
Now you are given the following code in C:<br>
<br>
<br>
<font color='green'>
&nbsp;&nbsp;&nbsp;&nbsp;#include <stdio.h><br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;int main() {<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;int p = 4;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;switch (p) {<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;case 0: printf("zero\n"); break;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;case 1: ;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;case 2: printf("one or two\n"); break;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;case 3: ;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;case 4: ;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;case 5: printf("three to five\n"); break;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default: printf("something else\n"); break<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>
&nbsp;&nbsp;&nbsp;&nbsp;}   <br>

</font>
<br>
<br>
<font size='4pt' color='red'>
How would you translate that into Rust?
</font>
</p>
<form method="POST" enctype="multipart/form-data" action="">
<p> Enter your code here </p> <br>
<textarea rows="20" cols="100"name='comment'>
</textarea><br>
<p> Or you code upload a file </p>
<input type="file" name="myfile" />
<br/>
<input type="submit" />
</form>
<br>
<br>
<p> Don't know how to do it? No worries! Take a look at the solution and try again. </p>
<a href='/p4_solution'> Solution </a> <br>
<br>
<a href='/'> Home </a>
<br>
<br>
</body></html>"""

    def POST(self):
		x = web.input(myfile={})
		data = web.input().comment
		filedir = '/home/student/Rust-Everywhere'# change this to the directory you want to store the file in.
		filename = 'pig.rs'
		fname = filedir + '/' + filename
		fout = open(fname,'w') # creates the file where file should be stored
		user_input = ""
		if 'myfile' in x: # to check if the file-object is created
			if len(data) != 0:	
				fout = open(fname, 'w')
				fout.write(data)
			else:
				filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
				fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
		fout.close()

		try:
			result = subprocess.check_output(["/usr/bin/rust", "run", fname], stderr=subprocess.STDOUT)
			os.remove(fname)
		except subprocess.CalledProcessError as e:
		
			return """<html>
				<br>
				<br>
				<head><style>body {
             background-color:#cccccc;
            }</style></head><body>
				<h2 align='center'> Sorry. Try again! </h2> <br>
				<br>
				<br>
				""" + e.output + """
				<br>
				<br>
				<img src="http://www.cs.virginia.edu/~evans/pictures/me/08-small.png"><br>
				<br>
				<a href='/problem_4'> Back </a> &nbsp;
				<a href='/'> Home </a>
				</body></html>"""
		else:
			if result == "three to five\n":
				return """<html>
				<br>
				<br>
					<head><style>body {
             background-color:#cccccc;
            }</style></head><body>
					<h2 align='center'> Congratulations! </h2> <br>
					<br>
					<br>
					<p> Your result is: <br>
					""" + result + """
					<br>
					<br>
					Correct result is "three to five"!
					</p>
					<br>
					<br>
					<img src="https://lh6.googleusercontent.com/-PZRVLY5Gsvg/Uqk1dnfUVFI/AAAAAAAAAlI/uLc-7FITZpw/w411-h548-no/photo.JPG"><br>
				<br>
					<a href='/problem_4'> Back </a> &nbsp;
					<a href='/'> Home </a>
					</body></html>"""
			else:
				return """<html>
				<br>
				<br>
					<head><style>body {
             background-color:#cccccc;
            }</style></head><body>
					<h2 align='center'> Sorry. Try again! </h2> <br>
					<br>
					<br>
					<p> Your result is: <br>
					""" + result + """
					<br>
					<br>
					Correct result is "three to five\n"!
					</p>
					<br>
					<br>
					<img src="http://www.cs.virginia.edu/~evans/pictures/me/08-small.png"><br>
				<br>
					<a href='/problem_4'> Back </a> &nbsp;
					<a href='/'> Home </a>
					</body></html>"""


class Closure:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head><style>body {
             background-color:#cccccc;
            }</style></head><body>
<br>
<br>
<p align='center'><font size='7pt'> Q5: You need some closure </font></h2>
<br>
<br>
<br>
<p> Believe it or not, closure ("|blah|") will bring you a pointer to a function, just like in C. <br>
<br>
<br>
<font size='4pt' color='red'>
Write a function that uses the closure to print:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;six = 6<br>
(hint: you really just need one line of code)<br>
<br>
<br>
</font>
<font color='green'>
&nbsp;&nbsp;&nbsp;&nbsp;fn main() { <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;let closure = |num| println(fmt!("six = %?", num));<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;call_closure(closure);<br>
&nbsp;&nbsp;&nbsp;&nbsp;}<br>
</font>
</p>
<form method="POST" enctype="multipart/form-data" action="">
<p> Enter your code here </p> <br>
<textarea rows="20" cols="100"name='comment'>
</textarea><br>
<p> Or you code upload a file </p>
<input type="file" name="myfile" />
<br/>
<input type="submit" />
</form>
<br>
<br>
<p> Don't know how to do it? No worries! Take a look at the solution and try again. </p>
<a href='/p5_solution'> Solution </a> <br>
<br>
<a href='/'> Home </a>
<br>
<br>
</body></html>"""

    def POST(self):
		x = web.input(myfile={})
		data = web.input().comment
		filedir = '/home/student/Rust-Everywhere'# change this to the directory you want to store the file in.
		filename = 'pig.rs'
		fname = filedir + '/' + filename
		fout = open(fname,'w') # creates the file where file should be stored
		user_input = ""
		if 'myfile' in x: # to check if the file-object is created
			if len(data) != 0:	
				fout = open(fname, 'w')
				fout.write(data)
			else:
				filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
				fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
		fout.close()

		try:
			result = subprocess.check_output(["/usr/bin/rust", "run", fname], stderr=subprocess.STDOUT)
			os.remove(fname)
		except subprocess.CalledProcessError as e:
		
			return """<html>
				<br>
				<br>
				<head><style>body {
             background-color:#cccccc;
            }</style></head><body>
				<h2 align='center'> Sorry. Try again! </h2> <br>
				<br>
				<br>
				""" + e.output + """
				<br>
				<br>
				<img src="http://www.cs.virginia.edu/~evans/pictures/me/08-small.png"><br>
				<br>
				<a href='/problem_5'> Back </a> &nbsp;
				<a href='/'> Home </a>
				</body></html>"""
		else:
			if result == "six = 6\n":
				return """<html>
				<br>
				<br>
					<head><style>body {
             background-color:#cccccc;
            }</style></head><body>
					<h2 align='center'> Congratulations! </h2> <br>
					<br>
					<br>
					<p> Your result is: <br>
					""" + result + """
					<br>
					<br>
					Correct result is:<br>
					six = 6
					</p>
					<br>
					<br>
					<img src="https://lh6.googleusercontent.com/-PZRVLY5Gsvg/Uqk1dnfUVFI/AAAAAAAAAlI/uLc-7FITZpw/w411-h548-no/photo.JPG"><br>
				<br>
					<a href='/problem_5'> Back </a> &nbsp;
					<a href='/'> Home </a>
					</body></html>"""
			else:
				return """<html>
				<br>
				<br>
					<head><style>body {
             background-color:#cccccc;
            }</style></head><body>
					<h2 align='center'> Sorry. Try again! </h2> <br>
					<br>
					<br>
					<p> Your result is: <br>
					""" + result + """
					<br>
					<br>
					Correct result is:<br>
					six = 6
					</p>
					<br>
					<br>
					<img src="http://www.cs.virginia.edu/~evans/pictures/me/08-small.png"><br>
				<br>
					<a href='/problem_5'> Back </a> &nbsp;
					<a href='/'> Home </a>
					</body></html>"""


class Mut:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head><style>body {
             background-color:#cccccc;
            }</style></head><body>
<br>
<br>
<p align='center'><font size='7pt'> Q6: Mut it </font></h2>
<br>
<br>
<br>
<p> As you may know, variables in Rust are immutable by default! For example, if you want to change the value of x later, you definitely want to declare it in this way: <br>
<br>
<br>
<font color='green'>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;let mut a = 10;<br>
</font>
<br>
<br>
Without the key word "mut", you will get a compile error! <br>
Rust also formalizes the concept of object ownership to delegate management of an object's lifetime to either a variable or a task-local garbage collector.<br>
An object's owner is responsible for managing the lifetime of the object by calling the destructor, and the owner determines whether the object is mutable.<br>
<br>
<br>
<font size='4pt' color='red'>
Try compiling the following code and see the error message if you want.<br>
Now given that the mutability is inherited, how do you modify the code to make it compile?<br>
Also add code to print out the value of y at the end (hint: you need to dereference it first)?<br>
<br>
<br>
</font>
<font color='green'>
&nbsp;&nbsp;&nbsp;&nbsp;fn main() { <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;struct Foo {x: int, y: ~int}<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;let a = Foo {x: 5, y: ~10};<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a.x += 10;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;println(a.x.to_str());<br>
&nbsp;&nbsp;&nbsp;&nbsp;}<br>
</font>
</p>
<form method="POST" enctype="multipart/form-data" action="">
<p> Enter your code here </p> <br>
<textarea rows="20" cols="100"name='comment'>
</textarea><br>
<p> Or you code upload a file </p>
<input type="file" name="myfile" />
<br/>
<input type="submit" />
</form>
<br>
<br>
<p> Don't know how to do it? No worries! Take a look at the solution and try again. </p>
<a href='/p6_solution'> Solution </a> <br>
<br>
<a href='/'> Home </a>
<br>
<br>
</body></html>"""

    def POST(self):
		x = web.input(myfile={})
		data = web.input().comment
		filedir = '/home/student/Rust-Everywhere'# change this to the directory you want to store the file in.
		filename = 'pig.rs'
		fname = filedir + '/' + filename
		fout = open(fname,'w') # creates the file where file should be stored
		user_input = ""
		if 'myfile' in x: # to check if the file-object is created
			if len(data) != 0:	
				fout = open(fname, 'w')
				fout.write(data)
			else:
				filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
				fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
		fout.close()

		try:
			result = subprocess.check_output(["/usr/bin/rust", "run", fname], stderr=subprocess.STDOUT)
			os.remove(fname)
		except subprocess.CalledProcessError as e:
		
			return """<html>
				<br>
				<br>
				<head><style>body {
             background-color:#cccccc;
            }</style></head><body>
				<h2 align='center'> Sorry. Try again! </h2> <br>
				<br>
				<br>
				""" + e.output + """
				<br>
				<br>
				<img src="http://www.cs.virginia.edu/~evans/pictures/me/08-small.png"><br>
				<br>
				<a href='/problem_6'> Back </a> &nbsp;
				<a href='/'> Home </a>
				</body></html>"""
		else:
			if result == "15\n10\n":
				return """<html>
				<br>
				<br>
					<head><style>body {
             background-color:#cccccc;
            }</style></head><body>
					<h2 align='center'> Congratulations! </h2> <br>
					<br>
					<br>
					<p> Your result is: <br>
					""" + result + """
					<br>
					<br>
					Correct result is:<br>
					15&nbsp;10
					</p>
					<br>
					<br>
					<img src="https://lh6.googleusercontent.com/-PZRVLY5Gsvg/Uqk1dnfUVFI/AAAAAAAAAlI/uLc-7FITZpw/w411-h548-no/photo.JPG"><br>
				<br>
					<a href='/problem_6'> Back </a> &nbsp;
					<a href='/'> Home </a>
					</body></html>"""
			else:
				return """<html>
				<br>
				<br>
					<head><style>body {
             background-color:#cccccc;
            }</style></head><body>
					<h2 align='center'> Sorry. Try again! </h2> <br>
					<br>
					<br>
					<p> Your result is: <br>
					""" + result + """
					<br>
					<br>
					Correct result is:<br>
					15&nbsp;10
					</p>
					<br>
					<br>
					<img src="http://www.cs.virginia.edu/~evans/pictures/me/08-small.png"><br>
				<br>
					<a href='/problem_6'> Back </a> &nbsp;
					<a href='/'> Home </a>
					</body></html>"""


class Visible:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head><style>body {
             background-color:#cccccc;
            }</style></head><body>
<br>
<br>
<p align='center'><font size='7pt'> Q7: Hoos Invisible? </font></h2>
<br>
<br>
<br>
<p> In the following code, our module hierarchy is now two modules deep. There is the crate root, which contains your main() function, and the module farm. <br>
The module farm also contains a function and a module white_animals, which futher contains two functions.<br>
However, somehow the code does not compile due to the visibility problem.<br>
<br>
<br>
<font size='4pt' color='red'>
First compile to see the error message. Then, how would you change the code?<br>
<br>
<br>
</font>
<font color='green'>
&nbsp;&nbsp;&nbsp;&nbsp;mod farm { <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fn pig() { println("Heng heng"); }<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mod white_animals {<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fn cow() { println("Mooo"); }<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fn fox() { println("Ahh..."); }<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} <br>
&nbsp;&nbsp;&nbsp;&nbsp;}<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;fn main() { <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;::farm::pig();<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;::farm::white_animals::cow();<br>
&nbsp;&nbsp;&nbsp;&nbsp;}<br>
</font>
</p>
<form method="POST" enctype="multipart/form-data" action="">
<p> Enter your code here </p> <br>
<textarea rows="20" cols="100"name='comment'>
</textarea><br>
<p> Or you code upload a file </p>
<input type="file" name="myfile" />
<br/>
<input type="submit" />
</form>
<br>
<br>
<p> Don't know how to do it? No worries! Take a look at the solution and try again. </p>
<a href='/p7_solution'> Solution </a> <br>
<br>
<a href='/'> Home </a>
<br>
<br>
</body></html>"""

    def POST(self):
		x = web.input(myfile={})
		data = web.input().comment
		filedir = '/home/student/Rust-Everywhere'# change this to the directory you want to store the file in.
		filename = 'pig.rs'
		fname = filedir + '/' + filename
		fout = open(fname,'w') # creates the file where file should be stored
		user_input = ""
		if 'myfile' in x: # to check if the file-object is created
			if len(data) != 0:	
				fout = open(fname, 'w')
				fout.write(data)
			else:
				filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
				fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
		fout.close()

		try:
			result = subprocess.check_output(["/usr/bin/rust", "run", fname], stderr=subprocess.STDOUT)
			os.remove(fname)
		except subprocess.CalledProcessError as e:
		
			return """<html>
				<br>
				<br>
				<head><style>body {
             background-color:#cccccc;
            }</style></head><body>
				<h2 align='center'> Sorry. Try again! </h2> <br>
				<br>
				<br>
				""" + e.output + """
				<br>
				<br>
				<img src="http://www.cs.virginia.edu/~evans/pictures/me/08-small.png"><br>
				<br>
				<a href='/problem_7'> Back </a> &nbsp;
				<a href='/'> Home </a>
				</body></html>"""
		else:
			if result == "Heng heng\nMooo\n":
				return """<html>
				<br>
				<br>
					<head><style>body {
             background-color:#cccccc;
            }</style></head><body>
					<h2 align='center'> Congratulations! </h2> <br>
					<br>
					<br>
					<p> Your result is: <br>
					""" + result + """
					<br>
					<br>
					Correct result is:<br>
					Heng heng&nbsp;Mooo
					</p>
					<br>
					<br>
					<img src="https://lh6.googleusercontent.com/-PZRVLY5Gsvg/Uqk1dnfUVFI/AAAAAAAAAlI/uLc-7FITZpw/w411-h548-no/photo.JPG"><br>
				<br>
					<a href='/problem_7'> Back </a> &nbsp;
					<a href='/'> Home </a>
					</body></html>"""
			else:
				return """<html>
				<br>
				<br>
					<head><style>body {
             background-color:#cccccc;
            }</style></head><body>
					<h2 align='center'> Sorry. Try again! </h2> <br>
					<br>
					<br>
					<p> Your result is: <br>
					""" + result + """
					<br>
					<br>
					Correct result is:<br>
					Heng heng&nbsp;Mooo
					</p>
					<br>
					<br>
					<img src="http://www.cs.virginia.edu/~evans/pictures/me/08-small.png"><br>
				<br>
					<a href='/problem_7'> Back </a> &nbsp;
					<a href='/'> Home </a>
					</body></html>"""



class p1_solution:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head><style>body {
             background-color:#cccccc;
            }</style></head><body>
<br>
<br>
<p align='center'> <font size='7pt'>Q1.Make It More Concise </font></p>
<br>
<br>
<br>
<p> Though it isn't apparent in all code, there is a fundamental difference between Rust's syntax and predecessors like C. <br>
Many constructs that are statements(with ";" at the end) in C are expressions(without ";" at the end) in Rust, allowing code to be more concise. <br>
For example, you might write a piece of code like this:<br>
<br>
<br>
<font color='green'>
&nbsp;&nbsp;&nbsp;&nbsp;fn main() {<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;let item = "muffin";<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;let price;<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if item == "salad" {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;price = 3.50;<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} else if item == "muffin" {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;price = 2.25;<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} else {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;price = 2.00;<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;println(fmt!("%?", price));<br>
&nbsp;&nbsp;&nbsp;&nbsp;}<br>
</font>
<br>
<br>
<font size='4pt' color='red'>How would you make the code above more concise? (for this question, you can only delete words, punctuations, or change indentations)
</font></p>
<br>
<br>
<p font size = '5pt'> Sample Solution: </p>
<br>
<br>
<br>
<font color='green'>
&nbsp;&nbsp;&nbsp;&nbsp;fn main() {<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;let item = "muffin";<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;let price =<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if item == "salad" {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.50<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} else if item == "muffin" {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.25<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} else {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.00<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;};<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;println(fmt!("%?", price));<br>
&nbsp;&nbsp;&nbsp;&nbsp;}<br>
</font>
<br>
<br>
<a href='/problem_1'> Back </a>
<br>
<br>
</body></html>"""


class p2_solution:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head><style>body {
             background-color:#cccccc;
            }</style></head><body>
<br>
<br>
<p align='center'><font size='7pt'> Q2: Where Is My Return?! </font></h2>
<br>
<br>
<br>
<p> In Q1, you have learned how expression works, or at least you think you do. <br>
In Rust, basically everything that's not a declaration (declarations are let for variables; fn for functions; and any top-level <br>
named items such as traits, enum types, and static items) is an expression, including function bodies themselves!<br>
Therefore, there is usually no need for a return statement, because the result of the expression is used as the return value.<br>
Isn't this crazy...<br>
<br>
<br>
<font color='green'>
&nbsp;&nbsp;&nbsp;&nbsp;fn main() {<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if is_four(4) {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;println("It is four!");<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>
&nbsp;&nbsp;&nbsp;&nbsp;}   <br>

&nbsp;&nbsp;&nbsp;&nbsp;fn is_four(x: int) -> bool {<br>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return (x == 4);<br>
&nbsp;&nbsp;&nbsp;&nbsp;}<br>
</font>
<br>
<br>
<font size='4pt' color='red'>
Could you help me get rid of the keyword "return"? It just really bothers me...
</font>
</p>
<br>
<br>
<p font size = '5pt'> Sample Solution: </p>
<br>
<br>
<br>
<font color='green'>
&nbsp;&nbsp;&nbsp;&nbsp;fn main() {<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if is_four(4) {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;println("It is four!");<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>
&nbsp;&nbsp;&nbsp;&nbsp;}   <br>

&nbsp;&nbsp;&nbsp;&nbsp;fn is_four(x: int) -> bool {<br>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x == 4<br>
&nbsp;&nbsp;&nbsp;&nbsp;}<br>
</font>
<br>
<br>
<a href='/problem_2'> Back </a>
<br>
<br>
</body></html>"""


class p3_solution:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head><style>body {
             background-color:#cccccc;
            }</style></head><body>
<br>
<br>
<p align='center'><font size='7pt'> Q3: Loop the Loop </font></h2>
<br>
<br>
<br>
<p> In Rust, loops are a little bit different. it looks something like this: <br>
<br>
<br>
<font color='green'>
&nbsp;&nbsp;&nbsp;&nbsp;for blah in blahhh.iter() { <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//do something with "blah";<br>
&nbsp;&nbsp;&nbsp;&nbsp;}<br>
</font>
<br>
<br>
<font size='4pt' color='red'>
Now suppose you were given a vector like this:<br>
&nbsp;&nbsp;&nbsp;&nbsp;let pigs = ~[~"pig1", ~"pig2", ~"pig_little"];<br>
How would you print them out in order (note that the strings are specified by pointers)?<br>
</font>
</p>
<br>
<br>
<p font size = '5pt'> Sample Solution: </p>
<br>
<br>
<br>
<font color='green'>
&nbsp;&nbsp;&nbsp;&nbsp;fn main() {<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;let pigs = ~[~"pig1", ~"pig2", ~"pig_little"]; <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for pig in pigs.iter() {<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;println(*pig);<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}   <br>
&nbsp;&nbsp;&nbsp;&nbsp;}   <br>
</font>
<br>
<br>
<a href='/problem_3'> Back </a>
<br>
<br>
</body></html>"""


class p4_solution:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head><style>body {
             background-color:#cccccc;
            }</style></head><body>
<br>
<br>
<p align='center'><font size='7pt'> Q4: Are We A Good Match? </font></h2>
<br>
<br>
<br>
<p> Rust's match construct is a generalized, cleaned-up version of C's switch construct. You provide it with a value and a number of arms, <br>
each labelled with a pattern, and the code compares the value against each pattern in order until one matches.  <br>
The matching pattern executes its corresponding arm.<br>
<br>
<br>
Now you are given the following code in C:<br>
<br>
<br>
<font color='green'>
&nbsp;&nbsp;&nbsp;&nbsp;#include <stdio.h><br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;int main() {<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;int p = 4;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;switch (p) {<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;case 0: printf("zero\n"); break;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;case 1: ;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nmod farm {
        pub fn pig() { println("Heng heng"); }
        mod white_animals {
            pub fn cow() { println("Mooo"); }
            pub fn fox() { println("Ahh..."); }
        }
    }

    fn main() {
        ::farm::pig();
        ::farm::white_animals::cow();
    }bsp;&nbsp;&nbsp;case 2: printf("one or two\n"); break;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;case 3: ;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;case 4: ;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;case 5: printf("three to five\n"); break;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default: printf("something else\n"); break<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>
&nbsp;&nbsp;&nbsp;&nbsp;}   <br>

</font>
<br>
<br>
<font size='4pt' color='red'>
How would you translate that into Rust?
</font>
</p>
<br>
<br>
<p font size = '5pt'> Sample Solution: </p>
<br>
<br>
<br>
<font color='green'>
&nbsp;&nbsp;&nbsp;&nbsp;fn main() {<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;let p = 4;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match p {<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0     => println("zero"),<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 | 2 => println("one or two"),<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3..5  => println("three to five"),<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _     => println("something else")<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>
&nbsp;&nbsp;&nbsp;&nbsp;}   <br>
</font>
<br>
<br>
<a href='/problem_4'> Back </a>
<br>
<br>
</body></html>"""


class p5_solution:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head><style>body {
             background-color:#cccccc;
            }</style></head><body>
<br>
<br>
<p align='center'><font size='7pt'> Q5: You need some closure </font></h2>
<br>
<br>
<br>
<p> Believe it or not, closure ("|blah|") will bring you a pointer to a function, just like in C. <br>
<br>
<br>
<font size='4pt' color='red'>
Write a function that uses the closure to print:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;six = 6<br>
(hint: you really just need one line of code)<br>
<br>
<br>
</font>
<font color='green'>
&nbsp;&nbsp;&nbsp;&nbsp;fn main() { <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;let closure = |num| println(fmt!("six = %?", num));<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;call_closure(closure);<br>
&nbsp;&nbsp;&nbsp;&nbsp;}<br>
</font>
</p>
<br>
<br>
<p font size = '5pt'> Sample Solution: </p>
<br>
<br>
<br>
<font color='green'>
&nbsp;&nbsp;&nbsp;&nbsp;fn call_closure(b: &fn(int)) { b(6); }<br>
&nbsp;&nbsp;&nbsp;&nbsp;fn main() {<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;let closure = |num| println(fmt!("six = %?", num));<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;call_closure(closure);<br>
&nbsp;&nbsp;&nbsp;&nbsp;}<br>
</font>
<br>
<br>
<a href='/problem_5'> Back </a>
<br>
<br>
</body></html>"""


class p6_solution:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head><style>body {
             background-color:#cccccc;
            }</style></head><body>
<br>
<br>
<p align='center'><font size='7pt'> Q6: Mut it </font></h2>
<br>
<br>
<br>
<p> As you may know, variables in Rust are immutable by default! For example, if you want to change the value of x later, you definitely want to declare it in this way: <br>
<br>
<br>
<font color='green'>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;let mut a = 10;<br>
</font>
<br>
<br>
Without the key word "mut", you will get a compile error! <br>
Rust also formalizes the concept of object ownership to delegate management of an object's lifetime to either a variable or a task-local garbage collector.<br>
An object's owner is responsible for managing the lifetime of the object by calling the destructor, and the owner determines whether the object is mutable.<br>
<br>
<br>
<font size='4pt' color='red'>
Try compiling the following code and see the error message if you want.<br>
Now given that the mutability is inherited, how do you modify the code to make it compile?<br>
Also add code to print out the value of y at the end (hint: you need to dereference it first)?<br>
<br>
<br>
</font>
<font color='green'>
&nbsp;&nbsp;&nbsp;&nbsp;fn main() { <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;struct Foo {x: int, y: ~int}<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;let a = Foo {x: 5, y: ~10};<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a.x += 10;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;println(a.x.to_str());<br>
&nbsp;&nbsp;&nbsp;&nbsp;}<br>
</font>
</p>
<br>
<br>
<p font size = '5pt'> Sample Solution: </p>
<br>
<br>
<br>
<font color='green'>
&nbsp;&nbsp;&nbsp;&nbsp;fn main() { <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;struct Foo {x: int, y: ~int}<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;let mut a = Foo {x: 5, y: ~10};<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a.x += 10;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;println(a.x.to_str());<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;println((*a.y).to_str());<br>
&nbsp;&nbsp;&nbsp;&nbsp;}<br>
</font>
<br>
<br>
<a href='/problem_6'> Back </a>
<br>
<br>
</body></html>"""


class p7_solution:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head><style>body {
             background-color:#cccccc;
            }</style></head><body>
<br>
<br>
<p align='center'><font size='7pt'> Q7: Hoos Invisible? </font></h2>
<br>
<br>
<br>
<p> In the following code, our module hierarchy is now two modules deep. There is the crate root, which contains your main() function, and the module farm. <br>
The module farm also contains a function and a module white_animals, which futher contains two functions.<br>
However, somehow the code does not compile due to the visibility problem.<br>
<br>
<br>
<font size='4pt' color='red'>
First compile to see the error message. Then, how would you change the code?<br>
<br>
<br>
</font>
<font color='green'>
&nbsp;&nbsp;&nbsp;&nbsp;mod farm { <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fn pig() { println("Heng heng"); }<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mod white_animals {<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fn cow() { println("Mooo"); }<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fn fox() { println("Ahh..."); }<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} <br>
&nbsp;&nbsp;&nbsp;&nbsp;}<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;fn main() { <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;::farm::pig();<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;::farm::white_animals::cow();<br>
&nbsp;&nbsp;&nbsp;&nbsp;}<br>
</font>
</p>
<br>
<br>
<p font size = '5pt'> Sample Solution: </p>
<br>
<br>
<br>
<font color='green'>
&nbsp;&nbsp;&nbsp;&nbsp;mod farm { <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pub fn pig() { println("Heng heng"); }<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mod white_animals {<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pub fn cow() { println("Mooo"); }<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pub fn fox() { println("Ahh..."); }<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} <br>
&nbsp;&nbsp;&nbsp;&nbsp;}<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;fn main() { <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;::farm::pig();<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;::farm::white_animals::cow();<br>
&nbsp;&nbsp;&nbsp;&nbsp;}<br>
</font>
<br>
<br>
<a href='/problem_7'> Back </a>
<br>
<br>
</body></html>"""








if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()
