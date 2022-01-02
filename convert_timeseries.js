const fs = require("fs");

// require("./getData");

let { rows } = require("./mohfw.json");

fs.writeFileSync("./timeseries_statewise.csv", "date,state,new_confirmed,new_cured,confirmed,cured\n");
fs.writeFileSync("./timeseries_india.csv", "date,new_confirmed,new_cured,confirmed,cured\n");

let prevDateState = [];

let prevCountryRecord = {
    confirmed: 0,
    cured: 0,
};

let prevStateRecord = {};

let new_sconf = 0;
let new_scured = 0;

let countryRecord = {
    date: "",
    new_confirmed: 0,
    new_cured: 0,
    confirmed: 0,
    cured: 0,
};

for (let i = 0; i < rows.length; i++) {
    // Log Progress
    process.stdout.write(`${i + 1}/${rows.length}\r`);

    // Prepare to write in CSV
    let data = rows[i].value;
    data.report_time = data.report_time.split("T")[0];

    //// State Wise Data Process
    // Check if Same Date And State Combination
    if (prevDateState.includes(`${data.report_time}$${data.state}`)) continue;
    else prevDateState.push(`${data.report_time}$${data.state}`);

    // Calculate State-wise Daily Change
    if (prevStateRecord[data.state]) {
        let psr = prevStateRecord[data.state];
        new_sconf = data.confirmed - psr.confirmed;
        new_scured = data.cured - psr.cured;
    } else {
        prevStateRecord[data.state] = {
            confirmed: 0,
            cured: 0,
        };
    }

    // Append Record to CSV
    fs.appendFileSync(
        "./timeseries_statewise.csv",
        `${data.report_time.split("T")[0]},${data.state},${new_sconf},${new_scured},${data.confirmed},${data.cured}\n`
    );

    // Update State Previous Record
    prevStateRecord[data.state].confirmed = data.confirmed;
    prevStateRecord[data.state].cured = data.cured;

    //// All India Data Process
    if (data.report_time !== countryRecord.date) {
        if (countryRecord.date == "") {
            countryRecord.date = data.report_time;
        } else {
            // Calculate Daily Change
            let new_confirmed = countryRecord.confirmed - prevCountryRecord.confirmed;
            let new_cured = countryRecord.cured - prevCountryRecord.cured;

            // Append record to CSV
            fs.appendFileSync(
                "./timeseries_india.csv",
                `${countryRecord.date},${new_confirmed},${new_cured},${countryRecord.confirmed},${countryRecord.cured}\n`
            );

            // Update Previous Record
            prevCountryRecord.confirmed = countryRecord.confirmed;
            prevCountryRecord.cured = countryRecord.cured;

            // Reset Country Record
            countryRecord.date = data.report_time;
            countryRecord.confirmed = 0;
            countryRecord.cured = 0;
        }
    } else {
        countryRecord.confirmed += data.confirmed;
        countryRecord.cured += data.cured;
    }
}
