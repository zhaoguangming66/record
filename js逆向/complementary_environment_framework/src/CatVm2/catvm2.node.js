var fs =require('fs');
//框架工具模块
var vmtools=require('./tools/tools.node.js');
// var htmlelements=require('./browser/HTMLElements/htmlelements.node.js');
function Getcode(config,func_text){
    var code='';
    //引入框架工具代码
    code+=vmtools.Getcode()+"\r\n";
    //引入用户框架配置for
    for (var item in config){
        code+="catvm.memory.config."+item+ "=" +config[item]+";\n\r"
    }
                  
    // code+=func_text+';\r\n';
    //引入浏览器相关
    code+=fs.readFileSync(`${__dirname}/browser/EventTarget.js`)+"\r\n";
    code+=fs.readFileSync(`${__dirname}/browser/WindowProperties.js`)+"\r\n";
    code+=fs.readFileSync(`${__dirname}/browser/Window.js`)+"\r\n";
    code+=fs.readFileSync(`${__dirname}/browser/Location.js`)+"\r\n";
    code+=fs.readFileSync(`${__dirname}/browser/Navigator.js`)+"\r\n";
    code+=fs.readFileSync(`${__dirname}/browser/Screen.js`)+"\r\n";
    // code+=fs.readFileSync(`${__dirname}/browser/Storage.js`)+"\r\n";
    // code+=fs.readFileSync(`${__dirname}/browser/MimeType.js`)+"\r\n";
    // code+=fs.readFileSync(`${__dirname}/browser/Plugin.js`)+"\r\n";
    // code+=fs.readFileSync(`${__dirname}/browser/PluginArray.js`)+"\r\n";
    // code+=fs.readFileSync(`${__dirname}/browser/MimeTypeArray.js`)+"\r\n";
    // code+=htmlelements.Getcode()+"\r\n";
    // code+=fs.readFileSync(`${__dirname}/browser/HTMLDocument.js`)+"\r\n";
    code+=fs.readFileSync(`${__dirname}/browser/Document.js`)+"\r\n";
    code+="\ndebugger;\r\n";;
    //引入用户自定义环境
    return code
}

module.exports={
    Getcode
}