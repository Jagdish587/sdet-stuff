import posix_ipc

mq = posix_ipc.MessageQueue("/priority_queue", flags=posix_ipc.O_CREAT)

# Send messages with different priorities
mq.send("Low priority message", priority=1)
mq.send("Medium priority message", priority=5)
mq.send("HIGH PRIORITY message", priority=10)

print("Messages sent with priorities!")

mq.close()
