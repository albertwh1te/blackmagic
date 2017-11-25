document.writeln('Hello, world!'); // Define a walk_the_DOM function that visits every // node of the tree in HTML source order, starting // from some given node. It invokes a function,
// passing it each node in turn. walk_the_DOM calls
// itself to process each of the child nodes.
var walk_the_DOM = function walk(node, func) {
    func(node);
    node = node.firstChild;
    while (node) {
    walk(node, func);
    node = node.nextSibling;
    }
    };
// Define a getElementsByAttribute function. It
// takes an attribute name string and an optional
// matching value. It calls walk_the_DOM, passing it a
// function that looks for an attribute name in the
// node. The matching nodes are accumulated in a
// results array.
var getElementsByAttribute = function (att, value) {
    var results = [];
    walk_the_DOM(document.body, function (node) {
    var actual = node.nodeType === 1 && node.getAttribute(att);
    if (typeof actual === 'string' &&
    (actual === value || typeof value !== 'string')) {
    results.push(node);
    }
    });
    return results;
    };

// Make a factorial function with tail
// recursion. It is tail recursive because
// it returns the result of calling itself.
// JavaScript does not currently optimize this form.
var factorial = function factorial(i, a) {
    a = a || 1;
    document.writeln(i,':',a);
    if (i < 2) {
    return a;
    }
    return factorial(i - 1, a * i);
    };
document.writeln(factorial(4)); // 24

// test add function
var add = function (a, b) {
    if (typeof a !== 'number' || typeof b !== 'number') {
    throw {
    name: 'TypeError',
    message: 'add needs numbers'
    }
    }
    return a + b;
    }

document.writeln(add(4,3));
// document.writeln(add(4,'ddd')) //trow

var myObject = function(){
    var value = 0 ;
    return {
        increment:function(inc){
            value += typeof inc === 'number' ? inc :1;
        },
        getvalue:function(){
            return value;
        }
    }
}();
value  = myObject.getvalue()
document.writeln(value)
myObject.increment()
value  = myObject.getvalue()
document.writeln(value)
var fade = function(node){
    var level = 1;
    var step = function(){
        var hex = level.toString(16);
        node.style.backgroundColor = '#FFFF'+hex+hex;
        if (level<20){
            level += 1
            setTimeout(step,100)
    }
};
setTimeout(step,100)
};
fade(document.body)

// var hello = "testhello"
// var world = "testworld"
// var fuck = "${hello}$(world)"
// document.writeln(fuck)
// String.method('deentityify',function(){
//     var entity= {
//         quot: '"',
//         lt: '<',
//         gt: '>'
//     };
//     return function(){
//         return this.replace(/&([^&;]+);/g,
//         function(a,b){
//             var r = entity[b];
//             return typeof r === 'string'? r:a;
//         }
//     );
//     };
// }());
// document.writeln('&lt;&quot;&gt;'.deentityify( ));
var serial_number = function(){
    var prefix = '';
    var seq = 0;
    return {
        set_perfix:function(p){
            prefix = String(p);
        },
        set_seq:function(s){
            seq = s;
        },
        gensym:function(){
            var result = prefix + seq;
            seq += 1
            return result
        }
    }
}
var seqer = serial_number();
seqer.set_perfix('test');

seqer.set_seq(21);
var unique1 = seqer.gensym();
var unique2 = seqer.gensym();
document.writeln(unique1)
document.writeln(unique2)
var fibonacci = function(){
    var memo = [0,1];
    var fib = function(n){
        var result = memo[n];
        if (typeof result !== 'number'){
            result = fib(n-1) + fib(n-2);
            memo[n] = result;
        }
        return result;
    }
    return fib;
}();
for (var i = 0; i <= 10; i += 1) {
    document.writeln('// ' + i + ': ' + fibonacci(i));
    }
myArray = ['apple','banana','orange']
var i;
for (i = 0; i < myArray.length; i += 1) {
    document.writeln(myArray[i]);
}
Array.prototype.test = function(){
    return this
}
document.writeln(myArray.test())
var add = function(a,b){
    return a + b
}
myArray.total = function(){return this.reduce(add)}
document.writeln(myArray.total())
var parse_url = /^(?:([A-Za-z]+):)?(\/{0,3})([0-9.\-A-Za-z]+)(?::(\d+))?(?:\/([^?#]*))?(?:\?([^#]*))?(?:#(.*))?$/;
var url = "http://www.ora.com:80/goodparts?q#fragment";
var url = "http://wiki2.jrj.com.cn/pages/viewpage.action?pageId=5643810"
var result = parse_url.exec(url);
var names = ['url', 'scheme', 'slash', 'host', 'port',
'path', 'query', 'hash'];
var blanks = ' ';
var i;
for (i = 0; i < names.length; i += 1) {
document.writeln(names[i] + ':' +
blanks.substring(names[i].length), result[i]);
}
var parser_number = /^-?\d+(?:\.\d*)?(?:e[+\-]?\d+)?$/i;
var test = function(num){
    document.writeln(parser_number.test(num))
}
test('1'); // true
test('number'); // false
test('98.6'); // true
test('132.21.86.100'); // false
test('123.45E-67'); // true
test('123.45D-67'); // false
document.writeln(Math.PI.toFixed(0));
document.writeln(Math.PI.toFixed(2));
document.writeln(Math.PI.toFixed(7));
document.writeln(Math.PI.toFixed(20)); //zero to twenty
document.writeln(Math.PI.toPrecision(2));
document.writeln(Math.PI.toPrecision(7));
document.writeln(Math.PI.toPrecision(16));//without zero