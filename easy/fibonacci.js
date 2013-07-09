var fs  = require("fs");
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line != "") {
        console.log(fibonacci(line));
    }
});

function fibonacci(n) {
    if (n <= 1) {
        return n;
    } else {
        return fibonacci(n - 2) + fibonacci(n - 1);
    }
}
