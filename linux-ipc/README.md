# 🧵 IPC + Synchronization Cheat Sheet (Ultimate Revision)

## 🧠 Inter-Process Communication (IPC) Mechanisms

### 1. Pipes
- Stream-based communication  
- Usually between parent and child processes  
- One-way (by default)  

👉 Use: Simple data transfer  

---

### 2. Named Pipes (FIFO)
- Pipe with a filename  
- Works between unrelated processes  

👉 Use: Simple local IPC  

---

### 3. Message Queues
- Message-based communication  
- Supports priorities  

👉 Use: Structured communication  

---

### 4. Shared Memory
- Fastest IPC mechanism  
- Processes share the same memory  

👉 Use: High-performance systems  

---

### 5. Semaphores
- Synchronization mechanism  
- Controls access to shared resources  

👉 Use: Limit concurrent access  

---

### 6. Signals
- Asynchronous notifications  
- No data transfer  

👉 Use: Process control (interrupt, terminate)  

---

### 7. Sockets
- Works locally and over networks  
- Client–server communication  

👉 Use: Distributed systems  

---

### 8. Memory-Mapped Files (mmap)
- File mapped into memory  
- Shared + persistent  

👉 Use: Fast file access + IPC  

---

## 🧩 IPC Comparison Table

| IPC | Speed | Data Type | Scope | Complexity |
|-----|------|----------|-------|------------|
| Pipes | Medium | Stream | Local | Low |
| FIFO | Medium | Stream | Local | Low |
| Message Queue | Medium | Messages | Local | Medium |
| Shared Memory | 🚀 Fastest | Raw memory | Local | High |
| Signals | ⚡ Very Fast | Notification | Local | Low |
| Sockets | Medium | Stream/Messages | Local + Network | Medium |
| mmap | 🚀 Very Fast | Memory/File | Local | High |

---

## 🔐 Synchronization Tools

### 1. Lock
- Only ONE process at a time  

👉 Use: Critical section protection  

---

### 2. Semaphore
- Allows N processes  

👉 Use: Resource pools  

---

### 3. Event
- Waits for a signal  

👉 Use: Execution ordering  

---

## 🧩 Synchronization Comparison

| Tool | Controls | Use Case |
|------|---------|----------|
| Lock | Mutual exclusion | Shared data |
| Semaphore | Access count | Limited resources |
| Event | Execution order | Coordination |

---

## ⚠️ Common Problems

### 🔥 Race Condition
- Multiple processes modify shared data simultaneously  

👉 Fix: Lock / Semaphore  

---

### 🔥 Deadlock
- Processes wait on each other indefinitely  

👉 Fix:
- Lock ordering  
- Avoid circular wait  

---

## 🧠 Deadlock Conditions (Coffman)

1. Mutual Exclusion  
2. Hold and Wait  
3. No Preemption  
4. Circular Wait  

👉 Break any one → Prevent deadlock  

---

## 🚀 Key Design Patterns

### ✔ Producer–Consumer
- Queue / Shared Memory / mmap  

### ✔ Client–Server
- Sockets  

### ✔ Publish–Subscribe
- Message Queues  

### ✔ Shared State
- Shared Memory + Lock  

---

## 🧠 When to Use What

| Scenario | Best Choice |
|---------|------------|
| Parent-child communication | Pipe |
| Independent processes | FIFO |
| Structured messaging | Message Queue |
| High performance | Shared Memory |
| Notifications | Signal |
| Network communication | Socket |
| File + performance | mmap |

---

## 🔥 Golden Rules

- Always synchronize shared data  
- Avoid `sleep()` for ordering  
- Prefer `with lock:` over manual lock  
- Use Event for sequencing  
- Maintain consistent lock ordering  

---

## 🧠 Mental Models

- Pipe → 🚰 Stream  
- Message Queue → 📬 Mailbox  
- Shared Memory → 🧠 Shared brain  
- Signal → 🔔 Notification  
- Socket → 📞 Communication  
- mmap → 📓 File as memory  
- Lock → 🔐 One at a time  
- Semaphore → 🚦 Limited access  
- Event → ⏳ Wait for signal  

---

## 🎯 Interview Quick Answers

**Q: Fastest IPC?**  
→ Shared Memory  

**Q: Pipe vs Message Queue?**  
→ Stream vs Messages  

**Q: Lock vs Semaphore?**  
→ 1 vs N processes  

**Q: What causes deadlock?**  
→ Circular wait  

**Q: mmap vs Shared Memory?**  
→ File-backed vs memory-only  

---

## 🚀 Final Summary

> IPC enables processes to communicate, while synchronization ensures safe and correct access to shared resources.