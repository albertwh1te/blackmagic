console.log("Hello, World!")
console.log("testy")

function hash(key) {
    key = (~key) + (key << 21); // key = (key << 21) - key - 1;
    key = key ^ (key >> 24);
    key = (key + (key << 3)) + (key << 8); // key * 265
    key = key ^ (key >> 14);
    key = (key + (key << 2)) + (key << 4); // key * 21
    key = key ^ (key >> 28);
    key = key + (key << 31);
    return key;
}
console.log(hash(10));


function inverse_hash(key) {
    var tmp;

    // Invert key = key + (key << 31)
    tmp = key-(key<<31);
    key = key-(tmp<<31);

    // Invert key = key ^ (key >> 28)
    tmp = key^key>>28;
    key = key^tmp>>28;

    // Invert key *= 21
    // key *= 14933078535860113213u;
    key *= 14933078535860113213;

    // Invert key = key ^ (key >> 14)
    tmp = key^key>>14;
    tmp = key^tmp>>14;
    tmp = key^tmp>>14;
    key = key^tmp>>14;

    // Invert key *= 265
    // key *= 15244667743933553977u;
    key *= 15244667743933553977;

    // Invert key = key ^ (key >> 24)
    tmp = key^key>>24;
    key = key^tmp>>24;

    // Invert key = (~key) + (key << 21)
    tmp = ~key;
    tmp = ~(key-(tmp<<21));
    tmp = ~(key-(tmp<<21));
    key = ~(key-(tmp<<21));

    return key;
}

console.log(inverse_hash(hash(10)));
