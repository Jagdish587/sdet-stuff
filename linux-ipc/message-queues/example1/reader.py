import posix_ipc

# Open existing queue
mq = posix_ipc.MessageQueue("/my_queue")

# Receive messages
msg, priority = mq.receive()
print("Received:", msg.decode())

msg, priority = mq.receive()
print("Received:", msg.decode())

mq.close()

# Optional: remove queue from system
posix_ipc.unlink_message_queue("/my_queue")
