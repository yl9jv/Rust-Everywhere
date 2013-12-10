import web
import subprocess

urls = ('/', 'Upload')

class Upload:
    def GET(self):
        return """<html><head></head><body>
<form method="POST" action="">
<textarea rows="20" cols="100"name='comment'>
</textarea><br>
<input type="submit">
</form>
</body></html>"""

    def POST(self):
	data = web.input().comment
	filedir = '/home/student/Rust-Everywhere'
	filename = 'pig.rs'
	fname = filedir + '/' + filename
	fout = open(fname, 'w')
	fout.write(data)
	fout.close()
	try:
		result = subprocess.check_output(["/usr/bin/rust", "run", fname], stderr=subprocess.STDOUT)
	except subprocess.CalledProcessError as e:
		return e.output
	else:
		return result

if __name__ == "__main__":
  app = web.application(urls, globals())
  app.run()
