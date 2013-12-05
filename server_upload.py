import web
import subprocess

urls = ('/upload', 'Upload')

class Upload:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head></head><body>
<form method="POST" enctype="multipart/form-data" action="">
<input type="file" name="myfile" />
<br/>
<input type="submit" />
</form>
</body></html>"""

    def POST(self):
        x = web.input(myfile={})
        filedir = '/home/student/Rust-Everywhere' # change this to the directory you want to store the file in.
        if 'myfile' in x: # to check if the file-object is created
            filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
            filename="pig.rs"
	    fname = filedir + '/' + filename
            fout = open(fname,'w') # creates the file where the uploaded file should be stored
            fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
            fout.close() # closes the file, upload complete.

	try:
		result = subprocess.check_output(["/usr/bin/rust", "run", fname], stderr=subprocess.STDOUT)
	except subprocess.CalledProcessError as e:
		return e.output
	else:
		return result

        raise web.seeother('/upload')


if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()
