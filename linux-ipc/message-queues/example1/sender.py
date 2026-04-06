import posix_ipc

# Create or open a message queue
mq = posix_ipc.MessageQueue("/my_queue", flags=posix_ipc.O_CREAT)

# Send messages
mq.send("Hello from POSIX MQ!")
mq.send("Second message")

print("Messages sent!")

mq.close()
