//6-job_processor.js
const kue = require('kue');
const queue = kue.createQueue();

//Function to send notificaion
function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message ${message}`);
}

//Process jobs from queue
queue.process('push_notification_code', (job, done) => {
    const { phoneNumber, message} = job.data;
    sendNotification(phoneNumber, message);
    done();
});
