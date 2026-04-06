import posix_ipc

mq = posix_ipc.MessageQueue("/priority_queue")

# Receive messages (highest priority comes first)
for _ in range(3):
    msg, priority = mq.receive()
    print(f"Received: {msg.decode()} | Priority: {priority}")

mq.close()
posix_ipc.unlink_message_queue("/priority_queue")
