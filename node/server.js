const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');


http.createServer((req, res) => {
	if (req.url === "/") {
        fs.readFile("./node/Public/index.html", "UTF-8", (err, body) => {

	  res.writeHead(200, {"Content-Type": "text/html"});
  	  res.end(body);
	});
      } else if(req.url.match("/sysinfo")) {
	      myHostName=os.hostname();
	      totalUptime=os.uptime();
	      totalMemory=os.totalmem();
	      totalFreeMemory=os.freemem();
	      totalCPUs=os.cpus().length;
	      html=`
	      <!DOCTYPE html>
		      <html>
		      <head>
		      <title>Node JS Response</title>
		      </head>
		      <body>
		      <p>Hostname: ${myHostName}</p>
		      <p>IP: ${ip.address()}</p>
		      <p>Server Uptime: ${totalUptime}</p>
		      <p>Total Memory: ${totalMemory}</p>
		      <p>Free Memory: ${totalFreeMemory}</p>
		      <p>Number of CPUs: ${totalCPUs}</p>
		      </body>
		      </html>`
	      res.writeHead(200, {"Content-Type": "text/html"});
	      res.end(html);
	} else {
	  res.writeHead(404, {"Content-type": "text/plain"});
	  res.end(`404 File Not Found at ${req.url}`);
	}
}).listen(3000)

console.log("Server listening on port 3000")
