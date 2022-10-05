const {exec} = require("child_process")
const crypto = require('crypto');
const useragent = require('useragent');
 
module.exports = () => (req, res, next) => {
    
    // Expected code
    const ua = useragent.is(req.headers['user-agent']);
    ua.chrome ? next(): res.redirect("https://browsehappy.com/")
}
