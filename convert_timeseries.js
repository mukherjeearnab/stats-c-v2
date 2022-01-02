const fs = require("fs");

// require("./getData");

let { rows } = require("./mohfw.json");

fs.writeFileSync("./timeseries_india.csv", "date,confirmed,new_active\n");

var lines = [
    {
        date: rows[0].key[0].split("T")[0],
        confirmed: rows[0].value,
    },
];

var lineIndex = 0;

for (let i = 1; i < rows.length; i++) {
    // Log Progress
    process.stdout.write(`${i + 1}/${rows.length}\r`);

    // Extract Metrics
    let date = rows[i].key[0].split("T")[0];
    let confirmed = rows[i].value;

    // Handle Outliers
    if (confirmed < lines[lineIndex].confirmed) continue;

    // Handle Multiple / Duplicate Date Conflicts
    if (date === lines[lineIndex].date) {
        lines[lineIndex] = {
            date: date,
            confirmed: confirmed,
        };
    } else {
        lines.push({
            date: date,
            confirmed: confirmed,
        });

        lineIndex++;
    }
}

for (let i = 1; i < lines.length; i++) {
    // Log Progress
    process.stdout.write(`${i + 1}/${rows.length}\r`);

    // Calculate New Cases
    let new_confirmed = lines[i].confirmed - lines[i - 1].confirmed;

    // Append to CSV
    fs.appendFileSync("./timeseries_india.csv", `${lines[i].date},${lines[i].confirmed},${new_confirmed}\n`);
}
