import frida

test = """
Java.perform(
    function(){
    var MainActivity = Java.use('com.example.seccon2015.rock_paper_scissors.MainActivity')
    MainActivity.onClick.implementation = function(v){
    console.log(this.m.value) 
    this.onClick(v)
    }
    }
)
"""

process = frida.get_usb_device()
print(process)