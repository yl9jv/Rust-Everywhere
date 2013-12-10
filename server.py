import web
import subprocess
import os

urls = ('/', 'Upload')

class Upload:
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
</body></html>"""

    def POST(self):
	x = web.input(myfile={})
	data = web.input().comment
	filedir = '/home/student/Rust-Everywhere'# change this to the directory you want to store the file in.
	filename = 'pig.rs'
	fname = filedir + '/' + filename
	fout = open(fname,'w') # creates the file where file should be stored
	if 'myfile' in x: # to check if the file-object is created
		if data != "":	
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
		return e.output
	else:
		return result


        raise web.seeother('/upload')


if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()
