(function(e, t) {
    typeof exports == "object" && typeof module != "undefined" ? module.exports = t(e) : typeof define == "function" && define.amd ? define(t) : t(e)
}
)(typeof self != "undefined" ? self : typeof window != "undefined" ? window : typeof global != "undefined" ? global : this, function(e) {
    "use strict";
    var t = e.Base64, n = "2.4.8", r;
    if (typeof module != "undefined" && module.exports)
        if (typeof navigator == "undefined" || navigator.product != "ReactNative")
            try {
                r = require("buffer").Buffer
            } catch (i) {}
    var s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
      , o = function(e) {
        var t = {};
        for (var n = 0, r = e.length; n < r; n++)
            t[e.charAt(n)] = n;
        return t
    }(s)
      , u = String.fromCharCode
      , a = function(e) {
        if (e.length < 2) {
            var t = e.charCodeAt(0);
            return t < 128 ? e : t < 2048 ? u(192 | t >>> 6) + u(128 | t & 63) : u(224 | t >>> 12 & 15) + u(128 | t >>> 6 & 63) + u(128 | t & 63)
        }
        var t = 65536 + (e.charCodeAt(0) - 55296) * 1024 + (e.charCodeAt(1) - 56320);
        return u(240 | t >>> 18 & 7) + u(128 | t >>> 12 & 63) + u(128 | t >>> 6 & 63) + u(128 | t & 63)
    }
      , f = /[\uD800-\uDBFF][\uDC00-\uDFFFF]|[^\x00-\x7F]/g
      , l = function(e) {
        return e.replace(f, a)
    }
      , c = function(e) {
        var t = [0, 2, 1][e.length % 3]
          , n = e.charCodeAt(0) << 16 | (e.length > 1 ? e.charCodeAt(1) : 0) << 8 | (e.length > 2 ? e.charCodeAt(2) : 0)
          , r = [s.charAt(n >>> 18), s.charAt(n >>> 12 & 63), t >= 2 ? "=" : s.charAt(n >>> 6 & 63), t >= 1 ? "=" : s.charAt(n & 63)];
        return r.join("")
    }
      , h = e.btoa ? function(t) {
        return e.btoa(t)
    }
    : function(e) {
        return e.replace(/[\s\S]{1,3}/g, c)
    }
      , p = r ? r.from && Uint8Array && r.from !== Uint8Array.from ? function(e) {
        return (e.constructor === r.constructor ? e : r.from(e)).toString("base64")
    }
    : function(e) {
        return (e.constructor === r.constructor ? e : new r(e)).toString("base64")
    }
    : function(e) {
        return h(l(e))
    }
      , d = function(e, t) {
        return t ? p(String(e)).replace(/[+\/]/g, function(e) {
            return e == "+" ? "-" : "_"
        }).replace(/=/g, "") : p(String(e))
    }
      , v = function(e) {
        return d(e, !0)
    }
      , m = new RegExp(["[À-ß][-¿]", "[à-ï][-¿]{2}", "[ð-÷][-¿]{3}"].join("|"),"g")
      , g = function(e) {
        switch (e.length) {
        case 4:
            var t = (7 & e.charCodeAt(0)) << 18 | (63 & e.charCodeAt(1)) << 12 | (63 & e.charCodeAt(2)) << 6 | 63 & e.charCodeAt(3)
              , n = t - 65536;
            return u((n >>> 10) + 55296) + u((n & 1023) + 56320);
        case 3:
            return u((15 & e.charCodeAt(0)) << 12 | (63 & e.charCodeAt(1)) << 6 | 63 & e.charCodeAt(2));
        default:
            return u((31 & e.charCodeAt(0)) << 6 | 63 & e.charCodeAt(1))
        }
    }
      , y = function(e) {
        return e.replace(m, g)
    }
      , b = function(e) {
        var t = e.length
          , n = t % 4
          , r = (t > 0 ? o[e.charAt(0)] << 18 : 0) | (t > 1 ? o[e.charAt(1)] << 12 : 0) | (t > 2 ? o[e.charAt(2)] << 6 : 0) | (t > 3 ? o[e.charAt(3)] : 0)
          , i = [u(r >>> 16), u(r >>> 8 & 255), u(r & 255)];
        return i.length -= [0, 0, 2, 1][n],
        i.join("")
    }
      , w = e.atob ? function(t) {
        return e.atob(t)
    }
    : function(e) {
        return e.replace(/[\s\S]{1,4}/g, b)
    }
      , E = r ? r.from && Uint8Array && r.from !== Uint8Array.from ? function(e) {
        return (e.constructor === r.constructor ? e : r.from(e, "base64")).toString()
    }
    : function(e) {
        return (e.constructor === r.constructor ? e : new r(e,"base64")).toString()
    }
    : function(e) {
        return y(w(e))
    }
      , S = function(e) {
        return E(String(e).replace(/[-_]/g, function(e) {
            return e == "-" ? "+" : "/"
        }).replace(/[^A-Za-z0-9\+\/]/g, ""))
    }
      , x = function() {
        var n = e.Base64;
        return e.Base64 = t,
        n
    };
    e.Base64 = {
        VERSION: n,
        atob: w,
        btoa: h,
        fromBase64: S,
        toBase64: d,
        utob: l,
        encode: d,
        encodeURI: v,
        btou: y,
        decode: S,
        noConflict: x
    };
    if (typeof Object.defineProperty == "function") {
        var T = function(e) {
            return {
                value: e,
                enumerable: !1,
                writable: !0,
                configurable: !0
            }
        };
        e.Base64.extendString = function() {
            Object.defineProperty(String.prototype, "fromBase64", T(function() {
                return S(this)
            })),
            Object.defineProperty(String.prototype, "toBase64", T(function(e) {
                return d(this, e)
            })),
            Object.defineProperty(String.prototype, "toBase64URI", T(function() {
                return d(this, !0)
            }))
        }
    }
    return e.Meteor && (Base64 = e.Base64),
    typeof module != "undefined" && module.exports ? module.exports.Base64 = e.Base64 : typeof define == "function" && define.amd && define([], function() {
        return e.Base64
    }),
    {
        Base64: e.Base64
    }
});

function r(e) {
            var t = e.slice(0, 1e3).split("").map(function(e, t) {
                return String.fromCharCode(e.charCodeAt() - t % 2)
            }).join("");
            return Base64.decode(t + e.slice(1e3))
        }
