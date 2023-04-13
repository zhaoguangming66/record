// 获取原型链
ccc = []
function aaa(p) {
    if (p.__proto__ != undefined) {
        console.log(p[Symbol.toStringTag])
        aaa(p.__proto__)
    }
    if (p[Symbol.toStringTag] != undefined) {
        ccc.push(p[Symbol.toStringTag])
    }
}
aaa(document.__proto__)
console.log(ccc)
