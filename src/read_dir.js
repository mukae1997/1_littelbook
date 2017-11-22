var fs = require('fs');


// if (process.argv.length <= 2) {
//     console.log("Usage: " + __filename + " path/to/directory");
//     process.exit(-1);
// }

var path = '.././literature/';

exports.readBooks = fs.readdir(path, function(err, items) {
 console.log('read Books');
    console.log(items);

    for (var i=0; i<items.length; i++) {
        console.log(items[i]);
    }
});
