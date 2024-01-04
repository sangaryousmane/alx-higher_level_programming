#!/usr/bin/node

const request = require('request');

const todosUrl = process.argv[2];

request.get(todosUrl, (err, response, body) => {
  if (err) {
    console.error('Error: ', err);
  } else {
    try {
      const todosData = JSON.parse(body);
      const completedTasksByUser = {};

      todosData.forEach((todo) => {
        if (todo.completed) {
          if (completedTasksByUser[todo.userId]) {
            completedTasksByUser[todo.userId]++;
          } else {
            completedTasksByUser[todo.userId] = 1;
          }
        }
      });
	    console.log(completedTasksByUser);
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
