//inline uint32_t jenkins_rev_mix32(uint32_t key) {
//  key += (key << 12);  // key *= (1 + (1 << 12))
//  key ^= (key >> 22);
//  key += (key << 4);   // key *= (1 + (1 << 4))
//  key ^= (key >> 9);
//  key += (key << 10);  // key *= (1 + (1 << 10))
//  key ^= (key >> 2);
//  // key *= (1 + (1 << 7)) * (1 + (1 << 12))
//  key += (key << 7);
//  key += (key << 12);
//  return key;
//}

//var bigInt = require("big-integer");
//function hash(key){
//    key =  bigInt(key);
//    key = key.add( key.shiftLeft(12) );
//    key = key.xor( key.shiftRight(22) );
//    key = key.add( key.shiftLeft(4) );
//    key = key.xor( key.shiftRight(9) );
//    key = key.add( key.shiftLeft(10) );
//    key = key.xor( key.shiftRight(2) );
//    key = key.add( key.shiftLeft(7) );
//    key = key.add( key.shiftLeft(12));
//    return key
//}
//
//console.log( hash(10).multiply(bigInt(2364026753)) );


function hash(key) {
  key += (key << 12);  // key *= (1 + (1 << 12))
  key ^= (key >>> 22);
  key += (key << 4);   // key *= (1 + (1 << 4))
  key ^= (key >>> 9);
  key += (key << 10);  // key *= (1 + (1 << 10))
  key ^= (key >>> 2);
  // key *= (1 + (1 << 7)) * (1 + (1 << 12))
  key += (key << 7);
  key += (key << 12);
  return key;
}

console.log(hash(10));
function inverse_hash(key) {
  // These are the modular multiplicative inverses (in Z_2^32) of the
  // multiplication factors in jenkins_rev_mix32, in reverse order.  They were
  // computed using the Extended Euclidean algorithm, see
  // http://en.wikipedia.org/wiki/Modular_multiplicative_inverse
  key *= 2364026753;
  console.log(key);
  // The inverse of a ^= (a >> n) is
  // b = a
  // for (int i = n; i < 32; i += n) {
  //   b ^= (a >> i);
  // }
  key ^=
    (key >> 2)  ^ (key >> 4)  ^ (key >> 6)  ^ (key >> 8) ^
    (key >> 10) ^ (key >> 12) ^ (key >> 14) ^ (key >> 16) ^
    (key >> 18) ^ (key >> 20) ^ (key >> 22) ^ (key >> 24) ^
    (key >> 26) ^ (key >> 28) ^ (key >> 30);
  console.log(key);
  key *= 3222273025;
  console.log(key);
  key ^= (key >> 9) ^ (key >> 18) ^ (key >> 27);
  key *= 4042322161;
  console.log(key);
  key ^= (key >> 22);
  console.log(key);
  key *= 16773121;
  console.log(key);
  return key;
}
console.log(hash(10));
// console.log(inverse_hash( hash(10)  ));
