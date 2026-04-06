### Step-by-step
1. Reader starts → waits (event.wait())
2. Writer runs → writes data
3. Writer calls event.set()
4. Reader wakes up → reads data ✅