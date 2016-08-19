//configure vue
Vue.config.delimiters = ["{$", "$}"];
Vue.filter('child', function (value, childName) {
  return value[childName]
});
