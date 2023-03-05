"use strict";
(() => {
var exports = {};
exports.id = 613;
exports.ids = [613];
exports.modules = {

/***/ 7796:
/***/ ((module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.a(module, async (__webpack_handle_async_dependencies__, __webpack_async_result__) => { try {
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (/* binding */ HostSession),
/* harmony export */   "getServerSideProps": () => (/* binding */ getServerSideProps)
/* harmony export */ });
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(997);
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _components_layouts_mobile__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(6008);
/* harmony import */ var react_toastify__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(3590);
/* harmony import */ var _shared_constants__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(3147);
/* harmony import */ var react_qr_code__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(3267);
/* harmony import */ var react_qr_code__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(react_qr_code__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var phosphor_react__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(9628);
/* harmony import */ var phosphor_react__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(phosphor_react__WEBPACK_IMPORTED_MODULE_5__);
var __webpack_async_dependencies__ = __webpack_handle_async_dependencies__([_components_layouts_mobile__WEBPACK_IMPORTED_MODULE_1__, react_toastify__WEBPACK_IMPORTED_MODULE_2__]);
([_components_layouts_mobile__WEBPACK_IMPORTED_MODULE_1__, react_toastify__WEBPACK_IMPORTED_MODULE_2__] = __webpack_async_dependencies__.then ? (await __webpack_async_dependencies__)() : __webpack_async_dependencies__);






const handleToast = ()=>{
    toast("Loading...", {
        // toastId: "123",
        position: "bottom-center",
        autoClose: 3000,
        style: {
            marginTop: "20px",
            marginBottom: "0px"
        }
    });
};
function HostSession({ themeID  }) {
    return /*#__PURE__*/ (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxs)("div", {
        className: "flex flex-col justify-between h-full w-full",
        children: [
            /*#__PURE__*/ (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxs)("div", {
                children: [
                    /*#__PURE__*/ react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx("p", {
                        className: "text-xl font-semibold",
                        children: "Session is Active"
                    }),
                    /*#__PURE__*/ (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxs)("p", {
                        className: "text-sm text-gray-600 mt-1",
                        children: [
                            "Theme: ",
                            /*#__PURE__*/ react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx("span", {
                                className: "text-blue-600 font-semibold",
                                children: _shared_constants__WEBPACK_IMPORTED_MODULE_3__/* .themesMap.get */ .l_.get(themeID)
                            })
                        ]
                    }),
                    /*#__PURE__*/ react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx("hr", {
                        className: "mt-5 mb-4"
                    }),
                    /*#__PURE__*/ (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxs)("div", {
                        children: [
                            /*#__PURE__*/ (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxs)("div", {
                                className: "flex items-center gap-x-2",
                                children: [
                                    /*#__PURE__*/ react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx(phosphor_react__WEBPACK_IMPORTED_MODULE_5__.Notepad, {
                                        size: 28
                                    }),
                                    /*#__PURE__*/ react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx("span", {
                                        className: "text-base text-gray-800",
                                        children: "Instructions"
                                    })
                                ]
                            }),
                            /*#__PURE__*/ react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx("p", {
                                className: "text-sm text-gray-600 mt-2",
                                children: "1. Use the QR Code to let people join your session."
                            })
                        ]
                    }),
                    /*#__PURE__*/ react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx("div", {
                        className: "px-6 mt-7",
                        children: /*#__PURE__*/ react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx((react_qr_code__WEBPACK_IMPORTED_MODULE_4___default()), {
                            size: 256,
                            style: {
                                height: "auto",
                                maxWidth: "100%",
                                width: "100%"
                            },
                            value: `https://www.musix.vercel.app/join/${themeID}`,
                            viewBox: `0 0 256 256`
                        })
                    }),
                    /*#__PURE__*/ (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxs)("div", {
                        className: "mt-6",
                        children: [
                            /*#__PURE__*/ (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxs)("p", {
                                className: "text-sm text-gray-600",
                                children: [
                                    "2. Open the",
                                    /*#__PURE__*/ (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxs)("span", {
                                        className: "text-[#1db954] w-min mx-1",
                                        children: [
                                            /*#__PURE__*/ react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx(phosphor_react__WEBPACK_IMPORTED_MODULE_5__.SpotifyLogo, {
                                                size: 32,
                                                color: "#1db954",
                                                className: "inline mb-1"
                                            }),
                                            " Spotify"
                                        ]
                                    }),
                                    "app on your phone and start playing music!"
                                ]
                            }),
                            /*#__PURE__*/ react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx("p", {
                                className: "text-sm text-gray-600 mt-2",
                                children: "3. New songs will be queued every minute."
                            })
                        ]
                    })
                ]
            }),
            /*#__PURE__*/ (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxs)("button", {
                className: "flex items-center justify-center gap-x-2 py-3 rounded-full mt-8 bg-blue-500",
                children: [
                    /*#__PURE__*/ react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx(phosphor_react__WEBPACK_IMPORTED_MODULE_5__.X, {
                        size: 24,
                        color: "#fff",
                        weight: "fill"
                    }),
                    /*#__PURE__*/ react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx("p", {
                        className: "text-white font-semibold",
                        children: "Stop Session"
                    })
                ]
            })
        ]
    });
}
const getServerSideProps = async (context)=>{
    // get query params
    const { theme  } = context.query;
    return {
        props: {
            themeID: theme
        }
    };
};
HostSession.getLayout = function getLayout(page) {
    return /*#__PURE__*/ react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx(_components_layouts_mobile__WEBPACK_IMPORTED_MODULE_1__/* ["default"] */ .Z, {
        children: page
    });
};

__webpack_async_result__();
} catch(e) { __webpack_async_result__(e); } });

/***/ }),

/***/ 5832:
/***/ ((module) => {

module.exports = require("next/dist/shared/lib/loadable.js");

/***/ }),

/***/ 968:
/***/ ((module) => {

module.exports = require("next/head");

/***/ }),

/***/ 9628:
/***/ ((module) => {

module.exports = require("phosphor-react");

/***/ }),

/***/ 6689:
/***/ ((module) => {

module.exports = require("react");

/***/ }),

/***/ 3267:
/***/ ((module) => {

module.exports = require("react-qr-code");

/***/ }),

/***/ 997:
/***/ ((module) => {

module.exports = require("react/jsx-runtime");

/***/ }),

/***/ 5207:
/***/ ((module) => {

module.exports = import("@uiball/loaders");;

/***/ }),

/***/ 3590:
/***/ ((module) => {

module.exports = import("react-toastify");;

/***/ })

};
;

// load runtime
var __webpack_require__ = require("../webpack-runtime.js");
__webpack_require__.C(exports);
var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
var __webpack_exports__ = __webpack_require__.X(0, [735,152,8,147], () => (__webpack_exec__(7796)));
module.exports = __webpack_exports__;

})();