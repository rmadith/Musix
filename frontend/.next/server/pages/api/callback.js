"use strict";
(() => {
var exports = {};
exports.id = 585;
exports.ids = [585];
exports.modules = {

/***/ 2226:
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (/* binding */ handler)
/* harmony export */ });
async function handler(req, res) {
    console.log(req.query);
    res.status(200).json({
        name: "John Doe"
    });
// var callback_code = req.query['code']
// const redirectUri = "http://localhost:3000/api/callback"
// const clientId = '1a1b5b6ffcd84abe970e58d7524b24ce'
// const clientSecret = '79f3ee42b488444e9d9a872a4c4cdd2d'
// const body = `grant_type=authorization_code&code=${callback_code}&redirect_uri=${redirectUri}`
// const callback_to_spotify = await fetch('https://accounts.spotify.com/api/token', {
//     method: 'POST',
//     headers: {
//         'Content-Type': 'application/x-www-form-urlencoded',
//         'Authorization': 'Basic ' + Buffer.from(`${clientId}:${clientSecret}`).toString('base64')
//     },
//     body
// })
// const responseData = await callback_to_spotify.json();
// const response = await fetch("http://127.0.0.1:5000/auth/login", {
//   method: "POST", // or 'PUT'
//   headers: {
//     "Content-Type": "application/json",
//   },
//   body: JSON.stringify(responseData),
// })    // The return value is *not* serialized
// // You can return Date, Map, Set, etc.
// // Recommendation: handle errors
// if (!response.ok) {
//   // This will activate the closest `error.js` Error Boundary
//   throw new Error('Failed to fetch data');
// }
// res.redirect(`http://localhost:3000/`)
}


/***/ })

};
;

// load runtime
var __webpack_require__ = require("../../webpack-api-runtime.js");
__webpack_require__.C(exports);
var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
var __webpack_exports__ = (__webpack_exec__(2226));
module.exports = __webpack_exports__;

})();