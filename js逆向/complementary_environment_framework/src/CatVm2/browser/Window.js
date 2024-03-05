window = this;


var Window = function Window(){
    throw new TypeError("Illegal constructor");
};catvm.safefunction(Window);

Object.defineProperties(Window.prototype, {
    [Symbol.toStringTag]: {
        value: "Window",
        configurable: true,
    }
})
/////////////////////////////////////////////////////////////////////////
Window.prototype.PERSISTENT = 1;
Window.prototype.TEMPORARY = 0;
window.open = function open(){debugger;};catvm.safefunction(window.open);
window.chrome =catvm.proxy(class chrome{} ) 
///////////////////////////////////////////////////////////////////////

// 自己补得
window.crypto = class crypto{};
self = window

Window.prototype.__proto__ = WindowProperties.prototype;

window.__proto__ = Window.prototype;

// Window=catvm.proxy(Window)
window=catvm.proxy(window)
