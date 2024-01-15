# <p align = "center">📜 ES6 - Basic</p>
## <p align="center">🎓 Holberton School Program - Lille</p>

<img src="https://i.imgur.com/SYkTyAA.png" width="100%" />

### Learning Objectives
- What ES6 is
- New features introduced in ES6
- The difference between a constant and a variable
- Block-scoped variables
- Arrow functions and function parameters default to them
- Rest and spread function parameters
- String templating in ES6
- Object creation and their properties in ES6
- Iterators and for-of loops

### Tasks

#### Task 0
**0-constants.js** : modify function `taskFirst` to instantiate variables using `const` & function `taskNext` to instantiate variables using `let`
<details>
<summary>Function to modify for task 0</summary>

```javascript
export function taskFirst() {
  var task = 'I prefer const when I can.';
  return task;
}

export function getLast() {
  return ' is okay';
}

export function taskNext() {
  var combination = 'But sometimes let';
  combination += getLast();

  return combination;
}
```
</details>

#### Task 1
**1-block-scoped.js** : modify the variables inside the function `taskBlock` so that the variables aren’t overwritten inside the conditional block
<details>
<summary>Function to modify for task 1</summary>

```javascript
export default function taskBlock(trueOrFalse) {
  var task = false;
  var task2 = true;

  if (trueOrFalse) {
    var task = true;
    var task2 = false;
  }

  return [task, task2];
}
```
</details>

#### Task 2
**2-arrow.js** : rewrite the following standard function to use ES6’s arrow syntax of the function `add` (it will be an anonymous function after)
<details>
<summary>Function to modify for task 2</summary>

```javascript
export default function getNeighborhoodsList() {
  this.sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];

  const self = this;
  this.addNeighborhood = function add(newNeighborhood) {
    self.sanFranciscoNeighborhoods.push(newNeighborhood);
    return self.sanFranciscoNeighborhoods;
  };
}
```
</details>

#### Task 3
**3-default-parameter.js** : condense the internals of the following function to 1 line - without changing the name of each function/variable
<details>
<summary>Function to modify for task 3</summary>

```javascript
export default function getSumOfHoods(initialNumber, expansion1989, expansion2019) {
  if (expansion1989 === undefined) {
    expansion1989 = 89;
  }

  if (expansion2019 === undefined) {
    expansion2019 = 19;
  }
  return initialNumber + expansion1989 + expansion2019;
}
```
</details>

#### Task 4

