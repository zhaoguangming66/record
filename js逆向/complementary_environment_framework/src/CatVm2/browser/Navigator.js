var Navigator=function Navigator() {
    throw new TypeError("Illegal constructor");
};catvm.safefunction(Navigator);


Object.defineProperties(Navigator.prototype, {
    [Symbol.toStringTag]: {
        value: "Navigator",
        configurable: true,
    }
})

/////////////////////////////////////////////////////////////////////////
Navigator.prototype.plugins = []
Navigator.prototype.languages = ['zh-CN', 'zh', 'en']
navigator={};
navigator.__proto__=Navigator.prototype;
for(var prototype_ in Navigator.prototype){
    navigator[prototype_]=Navigator.prototype[prototype_];
    Navigator.prototype.__defineGetter__(prototype_,function (){
    throw new TypeError('Illegal invocation')
    });
};
///////////////////////////////////////////////////////////////////////

navigator=catvm.proxy(navigator)