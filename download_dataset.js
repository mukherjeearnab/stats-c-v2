const fs = require("fs");
const https = require("https");

// URL of the image
const url = "https://raw.githubusercontent.com/datameet/covid19/master/data/mohfw.json";

https.get(url, (res) => {
    // Image will be stored at this path
    const path = "./mohfw.json";
    const filePath = fs.createWriteStream(path);
    res.pipe(filePath);
    filePath.on("finish", () => {
        filePath.close();
        console.log("Download Completed");
    });
});
