# <p align = "center">📜 ES6 - Promise</p>
## <p align="center">🎓 Holberton School Program - Lille</p>

<img src="https://i.imgur.com/SYkTyAA.png" width="100%" />

### Learning Objectives
- Promises (how, why, and what)
- How to use the `then`, `resolve`, `catch` methods
- How to use every method of the Promise object
- Throw / Try
- The await operator
- How to use an `async` function

### Tasks
- **0-promise.js** : return a Promise using this prototype `function getResponseFromAPI()`
- **1-promise.js** : using the prototype `getFullResponseFromAPI(success)`, return a promise. The parameter is a `boolean`
- **2-then.js** : append 3 handlers to this function `function handleResponseFromAPI(promise)`
- **3-all.js** : using this prototype `function handleProfileSignup()` collectively resolve all promises and `log body firstName lastName` to the console.
- **4-user-promise.js** : returns a resolved promise using this prototyle `function signUpUser(firstName, lastName) {}`
- **5-photo-reject.js** : write and export a function named `uploadPhoto`. It should accept one argument `fileName` (string). The function should return a Promise rejecting with an Error and the string `$fileName cannot be processed`
- **6-final-user.js** : import `signUpUser` from `4-user-promise.js` and `uploadPhoto` from `5-photo-reject.js` Write and export a function named `handleProfileSignup`. It should accept three arguments `firstName` (string), `lastName` (string), and `fileName` (string). The function should call the two other functions.
- **7-load_balancer.js** : write and export a function named `loadBalancer`. It should accept two arguments `chinaDownload` (Promise) and `USDownload` (Promise)
- **8-try.js** : write a function named `divideFunction` that will accept two arguments: `numerator` (Number) and `denominator` (Number)
- **9-try.js** : Write a function named `guardrail` that will accept one argument `mathFunction` (Function)
