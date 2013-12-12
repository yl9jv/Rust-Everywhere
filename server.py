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
	'/Rust_Everywhere', 'Everywhere',
	'/p1_solution', 'p1_solution',
	'/p2_solution', 'p2_solution',
	'/p3_solution', 'p3_solution',
	'/p4_solution', 'p4_solution',
	)

class Home:
	def GET(self):
		return """<html>
<head></head>
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
<br>
<br>
<h2 align='center'>Or you can simply test your code with our Rust Everywhere<br></h2><br>
<br>
<p align='center'><a align='center'href='Rust_Everywhere'> Rust Everywhere </a></p> <br>
</body></html>"""

class Everywhere:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head></head><body>
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
<a href='/'> Back </a>
</body></html>"""

    def POST(self):
		x = web.input(myfile={})
		data = web.input().comment
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

		try:
			result = subprocess.check_output(["/usr/bin/rust", "run", fname], stderr=subprocess.STDOUT)
			os.remove(fname)
		except subprocess.CalledProcessError as e:
			return """<html><head></head><body>
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
			return """<html><head></head><body>
				<h2 align='center'> Here is your result! </h2> <br>
				<br>
				<br>
				""" + result + """
				<br>
				<br>
				<a href='/Rust_Everywhere'> Back </a> &nbsp;
				<a href='/'> Home </a>
				</body></html>"""


class Concise:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head></head><body>
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
<a href='/'> Back </a>
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
		
			return """<html><head></head><body>
				<h2 align='center'> Sorry. Try again! </h2> <br>
				<br>
				<br>
				""" + e.output + """
				<br>
				<br>
				<a href='/problem_1'> Back </a> &nbsp;
				<a href='/'> Home </a>
				</body></html>"""
		else:
			if result == "2.25\n":
				return """<html><head></head><body>
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
					<a href='/problem_1'> Back </a> &nbsp;
					<a href='/'> Home </a>
					</body></html>"""
			else:
				return """<html><head></head><body>
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
					<a href='/problem_1'> Back </a> &nbsp;
					<a href='/'> Home </a>
					</body></html>"""



class Return:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head></head><body>
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
<a href='/'> Back </a>
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
		
			return """<html><head></head><body>
				<h2 align='center'> Sorry. Try again! </h2> <br>
				<br>
				<br>
				""" + e.output + """
				<br>
				<br>
				<a href='/problem_2'> Back </a> &nbsp;
				<a href='/'> Home </a>
				</body></html>"""
		else:
			if result == "It is four!\n":
				return """<html><head></head><body>
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
					<a href='/problem_2'> Back </a> &nbsp;
					<a href='/'> Home </a>
					</body></html>"""
			else:
				return """<html><head></head><body>
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
					<a href='/problem_2'> Back </a> &nbsp;
					<a href='/'> Home </a>
					</body></html>"""


class Loop:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head></head><body>
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
<a href='/'> Back </a>
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
		
			return """<html><head></head><body>
				<h2 align='center'> Sorry. Try again! </h2> <br>
				<br>
				<br>
				""" + e.output + """
				<br>
				<br>
				<a href='/problem_3'> Back </a> &nbsp;
				<a href='/'> Home </a>
				</body></html>"""
		else:
			if result == "pig1\npig2\npig_little\n":
				return """<html><head></head><body>
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
					<a href='/problem_3'> Back </a> &nbsp;
					<a href='/'> Home </a>
					</body></html>"""
			else:
				return """<html><head></head><body>
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
					<a href='/problem_3'> Back </a> &nbsp;
					<a href='/'> Home </a>
					</body></html>"""


class Match:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head></head><body>
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
<a href='/'> Back </a>
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
		
			return """<html><head></head><body>
				<h2 align='center'> Sorry. Try again! </h2> <br>
				<br>
				<br>
				""" + e.output + """
				<br>
				<br>
				<a href='/problem_2'> Back </a> &nbsp;
				<a href='/'> Home </a>
				</body></html>"""
		else:
			if result == "It is four!\n":
				return """<html><head></head><body>
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
					<a href='/problem_2'> Back </a> &nbsp;
					<a href='/'> Home </a>
					</body></html>"""
			else:
				return """<html><head></head><body>
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
					<a href='/problem_2'> Back </a> &nbsp;
					<a href='/'> Home </a>
					</body></html>"""



#class p3_solution:
#return """&nbsp;&nbsp;&nbsp;&nbsp;fn main() {<br>
 # &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;let pigs = ~[~"pig1", ~"pig2", ~"pig_little"]; {<br>
  #&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for pig in pigs.iter() {<br>
  #&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;println(*pig);<br>
#&nbsp;&nbsp;&nbsp;&nbsp;}   <br>"""



if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()
