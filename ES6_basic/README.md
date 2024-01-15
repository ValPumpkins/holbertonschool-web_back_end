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
**4-rest-parameter.js** : modify the following function to return the number of arguments passed to it using the rest parameter syntax
<details>
<summary>Function to modify for task 4</summary>

```javascript
export default function returnHowManyArguments() {

}
```
</details>

#### Task 5
**5-spread-operator.js** : using spread syntax, concatenate 2 arrays and each character of a string by modifying the function below. Your function body should be one line long
<details>
<summary>Function to modify for task 5</summary>

```javascript
export default function concatArrays(array1, array2, string) {

}
```
</details>

#### Task 6
**6-string-interpolation.js** : rewrite the return statement to use a template literal so you can the substitute the variables you’ve defined

<details>
<summary>Function to modify for task 6</summary>

```javascript
export default function getSanFranciscoDescription() {
  const year = 2017;
  const budget = {
    income: '$119,868',
    gdp: '$154.2 billion',
    capita: '$178,479',
  };

  return 'As of ' + year + ', it was the seventh-highest income county in the United States'
        / ', with a per capita personal income of ' + budget.income + '. As of 2015, San Francisco'
        / ' proper had a GDP of ' + budget.gdp + ', and a GDP per capita of ' + budget.capita + '.';
}
```
</details>

#### Task 7
**7-getBudgetObject.js** : modify the following function’s `budget` object to simply use the keyname instead
<details>
<summary>Function to modify for task 7</summary>

```javascript
export default function getBudgetObject(income, gdp, capita) {
  const budget = {
    income: income,
    gdp: gdp,
    capita: capita,
  };

  return budget;
}
```
</details>

#### Task 8
**8-getBudgetCurrentYear.js** : rewrite the `getBudgetForCurrentYear` function to use ES6 computed property names on the `budget` object
<details>
<summary>Function to modify for task 8</summary>

```javascript
function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
  const budget = {};

  budget[`income-${getCurrentYear()}`] = income;
  budget[`gdp-${getCurrentYear()}`] = gdp;
  budget[`capita-${getCurrentYear()}`] = capita;

  return budget;
}
```
</details>

#### Task 9
**9-getFullBudget.js** : rewrite `getFullBudgetObject` to use ES6 method properties in the `fullBudget` object
<details>
<summary>Function to modify for task 9</summary>

```javascript
import getBudgetObject from './7-getBudgetObject.js';

export default function getFullBudgetObject(income, gdp, capita) {
  const budget = getBudgetObject(income, gdp, capita);
  const fullBudget = {
    ...budget,
    getIncomeInDollars: function (income) {
      return `$${income}`;
    },
    getIncomeInEuros: function (income) {
      return `${income} euros`;
    },
  };

  return fullBudget;
}
```
</details>

#### Task 10
**10-loops.js** : rewrite the function appendToEachArrayValue to use ES6’s for...of operator. And don’t forget that var is not ES6-friendly
<details>
<summary>Function to modify for task 10</summary>

```javascript
export default function appendToEachArrayValue(array, appendString) {
  for (var idx in array) {
    var value = array[idx];
    array[idx] = appendString + value;
  }

  return array;
}
```
</details>

#### Task 11
**11-createEmployeesObject.js** : write a function named `createEmployeesObject` that will receive two arguments: `departmentName` (String) & `employees` (Array of Strings)
<details>
<summary>Function to modify for task 11</summary>

```javascript
export default function createEmployeesObject(departmentName, employees) {

}
```
</details>

#### Task 12
**12-createReportObject.js** : write a function named `createReportObject` whose parameter, `employeesList`, is the return value of the previous function `createEmployeesObject`
<details>
<summary>Function to modify for task 12</summary>

```javascript
export default function createReportObject(employeesList) {

}
```
</details>
