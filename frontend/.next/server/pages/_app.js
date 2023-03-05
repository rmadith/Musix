(() => {
var exports = {};
exports.id = 888;
exports.ids = [888];
exports.modules = {

/***/ 3820:
/***/ ((module) => {

// Exports
module.exports = {
	"style": {"fontFamily":"'__Manrope_9176a2', '__Manrope_Fallback_9176a2'","fontStyle":"normal"},
	"className": "__className_9176a2"
};


/***/ }),

/***/ 7692:
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
// ESM COMPAT FLAG
__webpack_require__.r(__webpack_exports__);

// EXPORTS
__webpack_require__.d(__webpack_exports__, {
  "default": () => (/* binding */ _app)
});

// EXTERNAL MODULE: external "react/jsx-runtime"
var jsx_runtime_ = __webpack_require__(997);
// EXTERNAL MODULE: ./node_modules/next/font/google/target.css?{"path":"pages/_app.tsx","import":"Manrope","arguments":[{"subsets":["latin"]}],"variableName":"manrope"}
var _app_tsx_import_Manrope_arguments_subsets_latin_variableName_manrope_ = __webpack_require__(3820);
var _app_tsx_import_Manrope_arguments_subsets_latin_variableName_manrope_default = /*#__PURE__*/__webpack_require__.n(_app_tsx_import_Manrope_arguments_subsets_latin_variableName_manrope_);
;// CONCATENATED MODULE: external "styled-jsx/style"
const style_namespaceObject = require("styled-jsx/style");
var style_default = /*#__PURE__*/__webpack_require__.n(style_namespaceObject);
// EXTERNAL MODULE: ./styles/globals.css
var globals = __webpack_require__(6764);
;// CONCATENATED MODULE: ./pages/_app.tsx




function MyApp({ Component , pageProps  }) {
    // get layout
    const getLayout = Component.getLayout || ((page)=>page);
    return getLayout(/*#__PURE__*/ (0,jsx_runtime_.jsxs)(jsx_runtime_.Fragment, {
        children: [
            jsx_runtime_.jsx((style_default()), {
                id: "e0ca08ab5d7d106c",
                dynamic: [
                    (_app_tsx_import_Manrope_arguments_subsets_latin_variableName_manrope_default()).style.fontFamily
                ],
                children: `:root{--manrope-font:${(_app_tsx_import_Manrope_arguments_subsets_latin_variableName_manrope_default()).style.fontFamily}}`
            }),
            /*#__PURE__*/ jsx_runtime_.jsx(Component, {
                ...pageProps,
                className: style_default().dynamic([
                    [
                        "e0ca08ab5d7d106c",
                        [
                            (_app_tsx_import_Manrope_arguments_subsets_latin_variableName_manrope_default()).style.fontFamily
                        ]
                    ]
                ]) + " " + (pageProps && pageProps.className != null && pageProps.className || "")
            })
        ]
    }));
}
/* harmony default export */ const _app = (MyApp);


/***/ }),

/***/ 6764:
/***/ (() => {



/***/ }),

/***/ 997:
/***/ ((module) => {

"use strict";
module.exports = require("react/jsx-runtime");

/***/ })

};
;

// load runtime
var __webpack_require__ = require("../webpack-runtime.js");
__webpack_require__.C(exports);
var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
var __webpack_exports__ = (__webpack_exec__(7692));
module.exports = __webpack_exports__;

})();