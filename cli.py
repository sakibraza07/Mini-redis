from mini_redis import MiniRedis

def repl():
    r = MiniRedis()
    print("🚀 Mini-Redis started (type 'EXIT' to quit)")

    while True:
        r._cleanup_expired()
        user_input = input("mini-redis> ").strip()
        if not user_input:
            continue

        command = user_input.split()
        cmd = command[0].upper()

        # ---------- KEY-VALUE COMMANDS ----------
        if cmd == "SET":
            if len(command) < 3:
                print("❌ Usage: SET key value [EX seconds]")
                continue
            key, value = command[1], command[2]
            ex = int(command[4]) if len(command) == 5 and command[3].upper() == "EX" else None
            print(r.set_key(key, value, ex))

        elif cmd == "GET":
            if len(command) < 2:
                print("❌ Usage: GET key")
                continue
            print(r.get_key(command[1]))

        elif cmd == "DEL":
            if len(command) < 2:
                print("❌ Usage: DEL key")
                continue
            print(r.del_key(command[1]))

        elif cmd == "EXISTS":
            if len(command) < 2:
                print("❌ Usage: EXISTS key")
                continue
            print(r.exists_key(command[1]))

        # ---------- LIST COMMANDS ----------
        elif cmd == "LPUSH":
            if len(command) < 3:
                print("❌ Usage: LPUSH key value")
                continue
            print(r.lpush(command[1], command[2]))

        elif cmd == "RPUSH":
            if len(command) < 3:
                print("❌ Usage: RPUSH key value")
                continue
            print(r.rpush(command[1], command[2]))

        elif cmd == "LPOP":
            if len(command) < 2:
                print("❌ Usage: LPOP key")
                continue
            print(r.lpop(command[1]))

        elif cmd == "RPOP":
            if len(command) < 2:
                print("❌ Usage: RPOP key")
                continue
            print(r.rpop(command[1]))

        elif cmd == "LRANGE":
            if len(command) < 4:
                print("❌ Usage: LRANGE key start end")
                continue
            start, end = int(command[2]), int(command[3])
            print(r.lrange(command[1], start, end))

        # ---------- SET COMMANDS ----------
        elif cmd == "SADD":
            if len(command) < 3:
                print("❌ Usage: SADD key member [member ...]")
                continue
            print(r.sadd_key(command[1], *command[2:]))

        elif cmd == "SMEMBERS":
            if len(command) < 2:
                print("❌ Usage: SMEMBERS key")
                continue
            print(r.smembers_key(command[1]))

        elif cmd == "SREM":
            if len(command) < 3:
                print("❌ Usage: SREM key member [member ...]")
                continue
            print(r.srem_key(command[1], *command[2:]))

        elif cmd == "SCARD":
            if len(command) < 2:
                print("❌ Usage: SCARD key")
                continue
            print(r.scard_key(command[1]))

        elif cmd == "SISMEMBER":
            if len(command) < 3:
                print("❌ Usage: SISMEMBER key member")
                continue
            print(r.sismember_key(command[1], command[2]))

        # ---------- EXIT ----------
        elif cmd == "EXIT":
            print("👋 Bye!")
            break

        else:
            print("❌ Unknown or invalid command")

if __name__ == "__main__":
    repl()
