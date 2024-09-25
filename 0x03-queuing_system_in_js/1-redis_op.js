// 1-redis_op.js

import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

// Function to set a new school value in Redis
const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

// Function to display the school value from Redis
const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (error, reply) => {
    if (error) {
      console.error(`Error fetching value: ${error}`);
    } else {
      console.log(`Value for ${schoolName}: ${reply}`);
    }
  });
};

// Call the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
