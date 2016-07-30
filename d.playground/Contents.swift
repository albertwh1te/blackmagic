//: Playground - noun: a place where people can play

import Cocoa


var airports = [12:"wangdagua",24:"madagua",33:"maxiaogua"]
for x in airports.keys {
    airports[x] = "0"
}
for (a,b) in airports {
    print("\(a):\(b)")
}