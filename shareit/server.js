const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

app.use(express.static('public'));

let senderId = null;

io.on('connection', (socket) => {
    console.log('A user connected');

    socket.on('register-as-sender', () => {
        if (senderId) {
            socket.emit('registration-failed', 'A sender is already registered.');
            return;
        }
        console.log('Sender registered:', socket.id);
        senderId = socket.id;
        socket.emit('registered-as-sender');
        io.emit('sender-ready');
    });

    socket.on('register-as-receiver', () => {
        if (!senderId) {
            socket.emit('registration-failed', 'No sender is currently registered.');
            return;
        }
        console.log('Receiver registered:', socket.id);
        socket.emit('registered-as-receiver');
    });

    socket.on('offer', (offer) => {
        if (senderId) {
            console.log('Offer sent to:', senderId);
            io.to(senderId).emit('offer', offer, socket.id);
        } else {
            console.log('No sender registered');
        }
    });

    socket.on('answer', (answer, receiverId) => {
        console.log('Answer sent to:', receiverId);
        io.to(receiverId).emit('answer', answer);
    });

    socket.on('ice-candidate', (candidate, peerId) => {
        console.log('ICE candidate sent to:', peerId);
        io.to(peerId).emit('ice-candidate', candidate);
    });

    socket.on('disconnect', () => {
        console.log('User disconnected');
        if (socket.id === senderId) {
            senderId = null;
            io.emit('sender-disconnected');
        }
    });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});