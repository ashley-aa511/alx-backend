// 5-subscriber.js
const redis = require('redis');

// Create a Redis client
const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${ERROR.MESSAGE}`);
});

// Subscribe to the channel
client.subscribe('holberton school channel');

// Listen for messages on the subscribed channel
client.on('message', (channel, message) => {
  console.log(`Message received on ${channel}: ${message}`);

  // If the message is KILL_SERVER, unsubscribe and quit
  if (message === 'KILL_SERVER') {
    client.unsubscribe('holberton school channel');
    client.quit();
  }
});
