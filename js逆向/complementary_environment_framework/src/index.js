const {VM,VMScript} = require('vm2');
var fs=require('fs')
var catvm2=require('./CatVm2/catvm2.node.js')
var catvm2_code=catvm2.Getcode()
const codefile=`${__dirname}/code.js`;
const vm = new VM();
const script=new VMScript(catvm2_code+fs.readFileSync(codefile),`${__dirname}/tem.js`)
debugger;
vm.run(script)