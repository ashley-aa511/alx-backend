// 4-redis_advanced_op.js

import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

// Store hash values using hset
const storeHash = () => {
  client.hset('HolbertonSchools', 'Portland', 50, redis.print);
  client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
  client.hset('HolbertonSchools', 'New York', 20, redis.print);
  client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
  client.hset('HolbertonSchools', 'Cali', 40, redis.print);
  client.hset('HolbertonSchools', 'Paris', 2, redis.print);
};

// Retrieve and display the hash values
const displayHash = () => {
  client.hgetall('HolbertonSchools', (error, result) => {
    if (error) {
      console.error(`Error retrieving hash: ${error}`);
    } else {
      console.log(result);
    }
  });
};

// Call the functions to store the hash and then display it
storeHash();
displayHash();
