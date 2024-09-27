// 6-job_creator.js
const kue = require('kue');
const queue = kue.createQueue();

// Create a job data object
const jobData = {
  phoneNumber: '123-456-7890',
  message: 'Hello, this is a notification!',
};

// Create a job in the queue
const job = queue.create('push_notification_code', jobData).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  } else {
    console.error(`Error creating job: ${err}`);
  }
});

// Job completion and failure handlers
job.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', (errorMessage) => {
  console.log(`Notification job failed: ${errorMessage}`);
});

