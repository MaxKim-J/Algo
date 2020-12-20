'use strict'

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = function(input) {}

const input = [];

rl.on('line', function(line) {
  input.push(line);
}).on('close', function() {
  solution(input);
  process.exit();
})